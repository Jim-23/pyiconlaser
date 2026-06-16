# Public API

## Client

```python
from pyiconlaser import IconLaserClient

laser = IconLaserClient(host="localhost")

```
### Methods
- version() -> str
- load_job(job_name: str) -> None
- prepare_job(job_name: str) -> None
- clear_job() -> None
- job_status() -> JobStatus
- loaded_job() -> str | None
- all_ids() -> dict[str, str]
- set_id(id_name: str, value: str) -> None
- limits_on() -> None
- limits_off() -> None
- enable_job() -> None
- start() -> None
- stop() -> None
- get_preview() -> bytes
