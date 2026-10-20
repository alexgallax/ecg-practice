import allure
import pytest

from ecg_practice.ecg import interpret_ecg


@allure.epic("Автоматическая интрпретация ЭКГ")
class TestHrEcg:

    def test_float(self):
        assert 0.1 + 0.2 == pytest.approx(0.3, abs=0.01)


    def test_ecg_none(self):
        with pytest.raises(ValueError, match="Данные ЭКГ не могут быть пустыми"):
            interpret_ecg(None)
