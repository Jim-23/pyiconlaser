"""Integration tests that run against a real laser running ICON Interface.

These tests require physical hardware and are skipped by default. They drive a
single physical laser and must be run serially (do not use ``pytest-xdist``).
Run them with:

    pytest --run-integration

Hardware is configured through environment variables (see ``conftest.py``):

    ICON_LASER_HOST, ICON_LASER_PORT, ICON_LASER_TIMEOUT,
    ICON_LASER_JOB, ICON_LASER_ID_NAME, ICON_LASER_ID_VALUE
"""

from pyiconlaser.enums import JobStatus

import pytest

pytestmark = pytest.mark.integration


@pytest.fixture(autouse=True)
def _clear_after(laser):
    """Best-effort cleanup that leaves the laser in a clean state after each test."""
    yield
    try:
        laser.clear_job()
    except Exception:
        # Cleanup is best-effort: a failure here must not mask the test result.
        pass


def test_load_job(laser, job_name):
    laser.load_job(job_name)

    assert laser.loaded_job() == job_name
    assert laser.job_status() == JobStatus.LOADED


def test_prepare_job(laser, job_name):
    laser.prepare_job(job_name)

    assert laser.loaded_job() == job_name
    assert laser.job_status() == JobStatus.LOADED


def test_set_id(laser, job_name, id_name, id_value):
    laser.prepare_job(job_name)

    laser.set_id(id_name, id_value)

    assert laser.all_ids().get(id_name) == id_value


def test_enable_job(laser, job_name, id_name, id_value):
    laser.prepare_job(job_name)
    laser.set_id(id_name, id_value)

    laser.enable_job()

    assert laser.job_status() == JobStatus.ENABLED


def test_start(laser, job_name, id_name, id_value):
    laser.prepare_job(job_name)
    laser.set_id(id_name, id_value)
    laser.enable_job()

    laser.start()

    assert laser.job_status() == JobStatus.MARKED


def test_clear_job(laser, job_name):
    laser.prepare_job(job_name)

    laser.clear_job()

    assert laser.job_status() == JobStatus.NOT_LOADED
