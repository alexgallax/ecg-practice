import pytest

from ecg_practice.models.ecg_data import ECGData, Rhythm, STSegment

@pytest.fixture
def normal_data() -> ECGData:
    return ECGData(
        heart_rate=75,
        rhythm=Rhythm.REGULAR,
        st_segment=STSegment.NORMAL,
        q_wave=False,
    )


@pytest.fixture
def infarction_data() -> ECGData:
    return ECGData(
        heart_rate=75,
        rhythm=Rhythm.REGULAR,
        st_segment=STSegment.ELEVATION,
        q_wave=True,
    )


@pytest.fixture
def arrhythmia_data() -> ECGData:
    return ECGData(
        heart_rate=75,
        rhythm=Rhythm.IRREGULAR,
        st_segment=STSegment.NORMAL,
        q_wave=False,
    )
