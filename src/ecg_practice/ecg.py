from ecg_practice.models.ecg_data import ECGData, STSegment, Rhythm
from ecg_practice.models.interpretation import Interpretation, Diagnosis, Urgency


def interpret_ecg(data: ECGData) -> Interpretation:
    if data.st_segment == STSegment.ELEVATION and data.q_wave:
        return Interpretation(
            diagnosis=Diagnosis.INFARCTION,
            urgency=Urgency.URGENT,
        )

    if data.st_segment == STSegment.ELEVATION:
        return Interpretation(
            diagnosis=Diagnosis.SUSPECTED_INFARCTION,
            urgency=Urgency.URGENT,
        )

    if data.st_segment == STSegment.DEPRESSION:
        return Interpretation(
            diagnosis=Diagnosis.ISCHEMIA,
            urgency=Urgency.PLANNED,
        )

    if data.q_wave:
        return Interpretation(
            diagnosis=Diagnosis.PREVIOUS_INFARCTION,
            urgency=Urgency.PLANNED,
        )

    if data.rhythm == Rhythm.IRREGULAR:
        return Interpretation(
            diagnosis=Diagnosis.ARRHYTHMIA,
            urgency=Urgency.PLANNED,
        )

    return analyze_heart_rate(data.heart_rate)


def analyze_heart_rate(heart_rate: float) -> Interpretation:
    if heart_rate < 60:
        return Interpretation(
            diagnosis=Diagnosis.BRADYCARDIA,
            urgency=Urgency.PLANNED,
        )
    elif heart_rate <= 100:
        return Interpretation(
            diagnosis=Diagnosis.NORMAL,
            urgency=Urgency.NONE,
        )
    else:
        return Interpretation(
            diagnosis=Diagnosis.TACHYCARDIA,
            urgency=Urgency.PLANNED,
        )
