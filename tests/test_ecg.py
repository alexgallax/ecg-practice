import pytest

from ecg_practice.ecg import interpret_ecg
from ecg_practice.models.interpretation import Interpretation, Diagnosis, Urgency


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
