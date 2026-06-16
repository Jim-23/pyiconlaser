# src/pyiconlaser/enums.py

from enum import Enum


class JobStatus(Enum):
    NOT_LOADED = "not_loaded"
    LOADED = "loaded"
    DATA_SET = "data_set"
    ENABLED = "enabled"
    MARKED = "marked"
    STOPPED = "stopped"

class MachineState(Enum):
    IDLE = "idle"
    BUSY = "busy"