from dataclasses import dataclass
from enum import Enum


@dataclass
class ECGData:
    heart_rate: float
    rhythm: Rhythm
    st_segment: STSegment
    q_wave: bool


class Rhythm(str, Enum):
    REGULAR = "REGULAR"
    IRREGULAR = "IRREGULAR"


class STSegment(str, Enum):
    NORMAL = "NORMAL"
    ELEVATION = "ELEVATION"
    DEPRESSION = "DEPRESSION"
