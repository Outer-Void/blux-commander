"""Authentication primitives for the BLUX Commander dashboard."""

from __future__ import annotations

import hashlib
import json
import secrets
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from fastapi import HTTPException, status

from .storage import default_storage_dir


@dataclass
class KeyPair:
    """Simple representation of a local authentication keypair."""

    public_key: str
    private_key: str


class AuthManager:
    """Manage creation and validation of the dashboard authentication keys."""

    def __init__(self, base_dir: Optional[Path] = None) -> None:
        self.base_dir = base_dir or default_storage_dir()
        self.base_dir.mkdir(parents=True, exist_ok=True)
        self.keypair_file = self.base_dir / "keypair.json"
        self._keypair: Optional[KeyPair] = None

    # ------------------------------------------------------------------
    def ensure_keypair(self) -> KeyPair:
        if self._keypair is None:
            if self.keypair_file.exists():
                self._keypair = self._load_keypair()
            else:
                self._keypair = self._generate_keypair()
                self._persist_keypair(self._keypair)
        return self._keypair

    def verify(self, token: Optional[str]) -> bool:
        if not token:
            return False
        keypair = self.ensure_keypair()
        return secrets.compare_digest(keypair.private_key, token)

    def require(self, token: Optional[str]) -> KeyPair:
        if not self.verify(token):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return self.ensure_keypair()

    # ------------------------------------------------------------------
    def _generate_keypair(self) -> KeyPair:
        private_key = secrets.token_hex(32)
        public_key = hashlib.sha256(private_key.encode("utf-8")).hexdigest()
        return KeyPair(public_key=public_key, private_key=private_key)

    def _persist_keypair(self, keypair: KeyPair) -> None:
        payload = {"public_key": keypair.public_key, "private_key": keypair.private_key}
        self.keypair_file.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def _load_keypair(self) -> KeyPair:
        data = json.loads(self.keypair_file.read_text(encoding="utf-8"))
        return KeyPair(public_key=data["public_key"], private_key=data["private_key"])


def authenticate_header(token: Optional[str], manager: AuthManager) -> KeyPair:
    """FastAPI dependency that validates the provided header token."""

    return manager.require(token)
