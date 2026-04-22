from calculator import Calculator
import pytest

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(Exception):
        calc.divide(10, 0)

def test_average():
    calc = Calculator()
    calc.add(2, 3)
    calc.add(4, 6)
    assert calc.average() == 7.5

def test_empty_average():
    calc = Calculator()
    with pytest.raises(Exception):
        calc.average()

def test_last_result():
    calc = Calculator()
    calc.add(2, 3)
    assert calc.last_result() == 5

def test_clear_history():
    calc = Calculator()
    calc.add(2, 3)
    calc.clear_history()
    assert calc.history == []

def test_power():
    calc = Calculator()
    assert calc.power(2, 3) == 8

def test_percentage():
    calc = Calculator()
    assert calc.percentage(50, 200) == 25

def test_percentage_zero():
    calc = Calculator()
    with pytest.raises(Exception):
        calc.percentage(10, 0)

def test_max_value():
    calc = Calculator()
    assert calc.max_value([-10, -5, -1]) == -1

def test_min_value():
    calc = Calculator()
    assert calc.min_value([5, 10, 3]) == 3