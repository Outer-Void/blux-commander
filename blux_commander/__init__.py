"""BLUX Commander package initialization."""

from importlib import metadata

__all__ = ["__version__"]

try:
    __version__ = metadata.version("blux-commander")
except metadata.PackageNotFoundError:  # pragma: no cover
    __version__ = "0.1.0"


def get_version() -> str:
    """Return the current package version."""

    return __version__
