import pytest

from legacy_processor import calc_stats, process_data, process_element


def test_process_element_above_threshold() -> None:
    assert process_element(15) == 30


def test_process_element_below_threshold() -> None:
    assert process_element(5) == 10


def test_process_data_applies_transformation() -> None:
    assert process_data([5, 15, 8]) == [10, 30, 13]


def test_calc_stats_returns_average() -> None:
    assert calc_stats([10, 20, 30]) == pytest.approx(20.0)


def test_calc_stats_empty_iterable_raises() -> None:
    with pytest.raises(ValueError):
        calc_stats([])
