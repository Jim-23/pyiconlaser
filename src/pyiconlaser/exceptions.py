# src/pyiconlaser/exeptions.py


class IconLaserError(Exception):
    """Base exception for all pyiconlaser errors."""
    pass


class IconLaserConnectionError(IconLaserError):
    """Raised when connection to ICON interface fails."""
    pass


class InvalidResponseError(IconLaserError):
    """Raised when API returns unexpected response."""
    pass


class JobLoadError(IconLaserError):
    """Raised when a job cannot be loaded."""
    pass


class JobEnableError(IconLaserError):
    """Raised when a job cannot be enabled."""
    pass


class SetIDError(IconLaserError):
    """Raised when an ID value cannot be set."""
    pass


class StartMarkingError(IconLaserError):
    """Raised when marking cannot be started."""
    pass


class StopMarkingError(IconLaserError):
    """Raised when marking cannot be stopped"""
    pass