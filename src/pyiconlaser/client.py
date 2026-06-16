# src/pyiconlaser/client.py

import requests

from .enums import JobStatus, MachineState
from .exceptions import (IconLaserConnectionError, InvalidResponseError, JobLoadError, JobEnableError, )


class IconLaserClient:
    def __init__(self, host: str = "localhost", port: int = 5287, timeout: int = 5) -> None:
        self.host = host
        self.port = port
        self.timeout = timeout

        self.base_url = f"http://{host}:{port}"

    def _request(self, endpoint: str) -> str:
        try:
            response = requests.get(f"{self.base_url}/{endpoint}", timeout=self.timeout,)
            response.raise_for_status()

            return response.text.strip()

        except requests.RequestException as e:
            raise IconLaserConnectionError(f"Failed to connect to ICON Interface: {e}") from e

    def _expect_ok(self, endpoint: str, expected: str) -> None:
        response = self._request(endpoint)

        if response.lower() != expected.lower():
            raise InvalidResponseError(f"Expected '{expected}', got '{response}'")


    # --- INFO ---

    def version(self) -> str:
        return self._request("version")

    def job_status(self) -> JobStatus:
        response = self._request("job_status")

        _, value = response.split(":", 1)

        return JobStatus(value)

    def loaded_job(self) -> str | None:
        response = self._request("loaded_job")

        _, value = response.split(":", 1)

        return value if value else None

    def state(self) -> MachineState:
        response = self._request("state")

        _, value = response.split(":", 1)

        return MachineState(value)


    # --- JOB MANAGEMENT ---

    def load_job(self, job_name: str) -> None:
        response = self._request(f"load_job?{job_name}")

        if response.lower() != "job_load:ok":
            raise JobLoadError(f"Failed to load job '{job_name}': {response}")

    def prepare_job(self, job_name: str) -> None:
        self.load_job(job_name)
        self.limits_off()


    def clear_job(self) -> None:
        self._expect_ok("clear_job", "clear:ok")

    def enable_job(self) -> None:
        response = self._request("enable_job")

        if response.lower() != "enable_job:ok":
            raise JobEnableError(f"Failed to enable job: {response}")


    # --- ID MANAGEMENT ---

    def all_ids(self) -> dict[str, str]: ...

    def set_id(self, id_name: str, value: str) -> None: ...

    # --- LASER CONTROL ---

    def start(self) -> None: ...

    def stop(self) -> None: ...

    def limits_on(self) -> None: ...

    def limits_off(self) -> None: ...

    # --- PREVIEW ---

    def get_preview(self) -> bytes: ...
