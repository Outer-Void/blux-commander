"""Read-only authentication stubs for the BLUX Commander dashboard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

@dataclass
class KeyPair:
    """Simple representation of a local authentication keypair."""

    public_key: str
    private_key: str


class AuthManager:
    """Provide read-only authentication placeholders without tokens."""

    def __init__(self) -> None:
        self._keypair: Optional[KeyPair] = None

    # ------------------------------------------------------------------
    def ensure_keypair(self) -> KeyPair:
        if self._keypair is None:
            self._keypair = KeyPair(public_key="read-only", private_key="")
        return self._keypair

    def require(self, token: Optional[str]) -> KeyPair:
        _ = token
        return self.ensure_keypair()


def authenticate_header(token: Optional[str], manager: AuthManager) -> KeyPair:
    """FastAPI dependency for read-only access."""

    return manager.require(token)
