# src/pyiconlaser/client.py


from .enums import JobStatus, MachineState


class IconLaserClient:
    def __init__(self, host: str = "localhost", port: int = 5287, timeout: int = 5) -> None:
        self.host = host
        self.port = port
        self.timeout = timeout
    
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
