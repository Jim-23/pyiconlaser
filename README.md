# pyiconlaser

![PyPI](https://img.shields.io/pypi/v/pyiconlaser)
![Python](https://img.shields.io/pypi/pyversions/pyiconlaser)
![License](https://img.shields.io/pypi/l/pyiconlaser)

Python wrapper for the TYKMA ICON Interface HTTP/TCPIP API used by industrial laser marking systems.

This library provides a simple Python API for controlling compatible laser marking systems through the ICON Interface software.

> This project is community-maintained and is not affiliated with or endorsed by any hardware manufacturer.

> This library was developed and tested against TYKMA ICON Interface software based on available API documentation and observed real-world behavior.

---

## Features

- Load marking jobs
- Read available IDs and modify their values
- Start and stop marking sequences
- Enable or clear jobs
- Control limits (tracing beam)
- Retrieve machine status
- Get template preview images

---

## Requirements

This library requires the vendor software **TYKMA ICON Interface** to be installed and running on the target machine.

The HTTP/TCPIP API must also be enabled manually in the `Config.xml` configuration file.

**Before using this library:**

- Install TYKMA ICON Interface software  
  - Vendor contact may be required to obtain the software and API documentation
- Enable HTTP/TCPIP communication in `Config.xml`
  - default path: `C:\tykma\custom\Tykma_Icon\config.xml`
  - see the vendor documentation for the software
- Verify the API is accessible (default port `5287`)
- Ensure the laser system is connected and recognised by ICON Interface

## Installation

```bash
pip install pyiconlaser
```

Or install locally:

```bash
pip install .
```

---

## Quick Start

```python
from pyiconlaser import IconLaserClient

laser = IconLaserClient()

laser.prepare_job("test_job")

laser.set_id("SN", "123456")
laser.set_id("QR", "PRODUCT001")

laser.enable_job()
laser.start()

laser.clear_job()
```

---

## Important Note

ICON Interface has undocumented behavior.

After loading a job:

```python
laser.load_job("test_job")
```

the software automatically enables limits mode internally.

This causes:

```text
all_ids -> empty response
set_id -> id_not_found
```

To fix this, limits must be disabled before modifying IDs:

```python
laser.load_job("test_job")
laser.limits_off()
```

For convenience:

```python
laser.prepare_job("test_job")
```

does both automatically.

---

python
sdk
laser
industrial-automation
automation
hardware
http-api
wrapper
## Basic Example

```python
from pyiconlaser import IconLaserClient

laser = IconLaserClient()

print(laser.version())
print(laser.job_status())
print(laser.all_ids())
```

---

## Supported API Methods

```python
version()
job_status()
loaded_job()
state()

load_job()
prepare_job()
clear_job()
enable_job()

all_ids()
set_id()

start()
stop()

limits_on()
limits_off()

get_preview()
```
---

## Tested Environment

- Python 3.14.4
- TYKMA ICON Interface 1.0.12.6 on Windows 11

---

## Testing

Unit tests run without any hardware:

```bash
pytest
```

Integration tests communicate with a **real laser** running ICON Interface and
are skipped by default. Enable them with the `--run-integration` flag:

```bash
pytest --run-integration
```

### Configuration

The target hardware is configured through environment variables. You can set them in two ways:

**Option 1: Using a `.env` file (recommended)**

Copy `.env.example` to `.env` and update with your hardware details:

```bash
cp .env.example .env
```

Then edit `.env` and set your values:

```
ICON_LASER_HOST=192.168.0.10
ICON_LASER_PORT=5287
ICON_LASER_TIMEOUT=5
ICON_LASER_JOB=test_job
ICON_LASER_ID_NAME=SN
ICON_LASER_ID_VALUE=TEST123
```

The `.env` file is automatically loaded during testing and is not committed to git.

**Option 2: Setting inline with the command**

```bash
ICON_LASER_HOST=192.168.0.10 ICON_LASER_JOB=test_job pytest --run-integration
```

### Environment Variables Reference

| Variable | Description | Default |
| --- | --- | --- |
| `ICON_LASER_HOST` | ICON Interface host | `localhost` |
| `ICON_LASER_PORT` | ICON Interface port | `5287` |
| `ICON_LASER_TIMEOUT` | Request timeout (seconds) | `5` |
| `ICON_LASER_JOB` | Marking job to run (required) | — |
| `ICON_LASER_ID_NAME` | ID field to set | `SN` |
| `ICON_LASER_ID_VALUE` | ID value to set | `TEST123` |

> Integration tests will physically operate the laser. Only run them on a
> system that is safe to mark.

---

## License

MIT License