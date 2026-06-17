import os

import pytest

from pyiconlaser import IconLaserClient


@pytest.fixture(scope="session")
def laser():
    """Client connected to a real laser, configured via environment variables.

    Environment variables:
        ICON_LASER_HOST: ICON Interface host (default: localhost)
        ICON_LASER_PORT: ICON Interface port (default: 5287)
        ICON_LASER_TIMEOUT: request timeout in seconds (default: 5)
    """
    host = os.environ.get("ICON_LASER_HOST", "localhost")
    port = int(os.environ.get("ICON_LASER_PORT", "5287"))
    timeout = int(os.environ.get("ICON_LASER_TIMEOUT", "5"))

    return IconLaserClient(host=host, port=port, timeout=timeout)


@pytest.fixture(scope="session")
def job_name():
    """Name of the marking job to use for integration tests.

    Configured via the ICON_LASER_JOB environment variable.
    """
    name = os.environ.get("ICON_LASER_JOB")

    if not name:
        pytest.skip("ICON_LASER_JOB environment variable is not set")

    return name


@pytest.fixture(scope="session")
def id_name():
    """ID field name to set during integration tests (default: SN)."""
    return os.environ.get("ICON_LASER_ID_NAME", "SN")


@pytest.fixture(scope="session")
def id_value():
    """ID value to set during integration tests (default: TEST123)."""
    return os.environ.get("ICON_LASER_ID_VALUE", "TEST123")
