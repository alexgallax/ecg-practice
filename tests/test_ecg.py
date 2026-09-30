import pytest

from ecg_practice.ecg import interpret_ecg
from ecg_practice.models.ecg_data import ECGData
from ecg_practice.models.interpretation import Interpretation, Diagnosis, Urgency


def test_interpret_ecg_normal(normal_data: ECGData):
    result = interpret_ecg(normal_data)
    expected = Interpretation(diagnosis=Diagnosis.NORMAL, urgency=Urgency.NONE)

    assert result == expected


def test_interpret_ecg_infarction(infarction_data: ECGData):
    result = interpret_ecg(infarction_data)
    expected = Interpretation(diagnosis=Diagnosis.INFARCTION, urgency=Urgency.URGENT)

    assert result == expected


def test_interpret_ecg_arrhythmia(arrhythmia_data: ECGData):
    result = interpret_ecg(arrhythmia_data)
    expected = Interpretation(diagnosis=Diagnosis.ARRHYTHMIA, urgency=Urgency.PLANNED)

    assert result == expected


@pytest.mark.parametrize("fixture_name, expected", [
    pytest.param(
    "normal_data",
Interpretation(diagnosis=Diagnosis.NORMAL, urgency=Urgency.NONE),
        id="normal diagnosis",
    ),
    pytest.param(
        "infarction_data",
Interpretation(diagnosis=Diagnosis.INFARCTION, urgency=Urgency.URGENT),
        id="infarction with urgency",
    )
])
def test_interpret_ecg(request: pytest.FixtureRequest, fixture_name: str, expected: Interpretation):
    data = request.getfixturevalue(fixture_name)
    result = interpret_ecg(data)
    assert result == expected
