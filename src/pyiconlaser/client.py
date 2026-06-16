# src/pyiconlaser/client.py

import requests

from .enums import JobStatus, MachineState
from .exceptions import (ConnectionError, InvalidResponseError, )


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
            raise ConnectionError(f"Failed to connect to ICON Interface: {e}") from e

    def _expect_ok(self, endpoint: str, expected: str) -> None:
        response = self._request(endpoint)

        if response.lower() != expected.lower():
            raise InvalidResponseError(f"Expected '{expected}', got '{response}'")
    
    # --- INFO ---

    def version(self) -> str: ...

    def job_status(self) -> JobStatus: ...

    def loaded_job(self) -> str | None: ...

    def state(self) -> MachineState: ...

    # --- JOB MANAGEMENT ---

    def load_job(self, job_name: str) -> None: ...

    def prepare_job(self, job_name: str) -> None: ...

    def clear_job(self) -> None: ...

    def enable_job(self) -> None: ...

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
