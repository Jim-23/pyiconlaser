from unittest.mock import patch

import pytest

from pyiconlaser import IconLaserClient
from pyiconlaser.enums import JobStatus
from pyiconlaser.exceptions import IconLaserConnectionError


def test_version():
    laser = IconLaserClient()

    with patch.object(laser, "_request", return_value="1.0.12.6"):
        assert laser.version() == "1.0.12.6"

def test_job_status():
    laser = IconLaserClient()

    with patch.object(laser, "_request", return_value="status:loaded"):
        assert laser.job_status() == JobStatus.LOADED


def test_all_ids():
    laser = IconLaserClient()

    with patch.object(
        laser,
        "_request",
        return_value="all_ids:SN:123,QR:ABC"
    ):
        assert laser.all_ids() == {
            "SN": "123",
            "QR": "ABC"
        }


def test_empty_ids():
    laser = IconLaserClient()

    with patch.object(
        laser,
        "_request",
        return_value="all_ids:"
    ):
        assert laser.all_ids() == {}


def test_connection_error():
    laser = IconLaserClient()

    with patch.object(
        laser,
        "_request",
        side_effect=IconLaserConnectionError("Failed")
    ):
        with pytest.raises(IconLaserConnectionError):
            laser.version()