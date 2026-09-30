from dataclasses import dataclass
from enum import Enum


@dataclass
class Interpretation:
    diagnosis: Diagnosis
    urgency: Urgency


class Diagnosis(str, Enum):
    NORMAL = "normal"
    BRADYCARDIA = "bradycardia"
    TACHYCARDIA = "tachycardia"
    ARRHYTHMIA = "arrhythmia"
    ISCHEMIA = "ischemia"
    INFARCTION = "infarction"
    SUSPECTED_INFARCTION = "suspected infarction"
    PREVIOUS_INFARCTION = "previous infarction"


class Urgency(str, Enum):
    NONE = "none"
    PLANNED = "planned"
    URGENT = "urgent"
