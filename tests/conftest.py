import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--run-integration",
        action="store_true",
        default=False,
        help="Run integration tests against a real laser running ICON Interface.",
    )


def pytest_collection_modifyitems(config, items):
    if config.getoption("--run-integration"):
        return

    skip_integration = pytest.mark.skip(
        reason="need --run-integration option to run (requires physical hardware)"
    )

    for item in items:
        if "integration" in item.keywords:
            item.add_marker(skip_integration)
