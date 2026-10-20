import allure
import pytest

from ecg_practice.ecg import interpret_ecg
from ecg_practice.models.ecg_data import ECGData
from ecg_practice.models.interpretation import Interpretation, Diagnosis, Urgency


@allure.epic("Автоматическая интрпретация ЭКГ")
@allure.feature("Интерпретация одиночных данных")
@allure.story("Норма, инфаркт")
class TestECGInterpretation:

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
    @pytest.mark.critical
    @allure.title("Данные ЭКГ с нормой и инфактом интерпретируются в диагноз и срочность")
    @allure.description("Передаем данные ЭКГ со значениями норма и инфакт и получаем объект с интерпретацией, "
                        "содержащий диагноз и срочность.")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("tag", "critical")
    @allure.link("https://...", name="Ссылка")
    @allure.issue("https://...", name="Не работает интерпретация инфаркта")
    @allure.testcase("TC-ECG-008", name="Интерпретация данных ЭКГ")
    def test_interpret_ecg(self, request: pytest.FixtureRequest, fixture_name: str, expected: Interpretation):
        data = request.getfixturevalue(fixture_name)
        result = interpret_ecg(data)
        assert result == expected


    @pytest.mark.parametrize("base_heart_rate_data, expected", [
        pytest.param(
            {"heart_rate": 75},
    Interpretation(diagnosis=Diagnosis.NORMAL, urgency=Urgency.NONE),
            id="normal heart rate",
        ),
        pytest.param(
        {"heart_rate": 50},
    Interpretation(diagnosis=Diagnosis.BRADYCARDIA, urgency=Urgency.PLANNED),
            id="bradycardia heart rate",
        ),
        pytest.param(
        {"heart_rate": 120},
    Interpretation(diagnosis=Diagnosis.TACHYCARDIA, urgency=Urgency.PLANNED),
            id="tachycardia heart rate",
        ),
    ], indirect=["base_heart_rate_data"])
    def test_ecg_heart_rate(self, base_heart_rate_data: ECGData, expected: Interpretation):
        result = interpret_ecg(base_heart_rate_data)
        assert result == expected
