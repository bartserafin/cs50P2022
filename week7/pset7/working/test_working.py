import pytest
from working import convert


def test_time():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_midnight_noon():
    assert convert("12:00 PM to 12:00 PM") == "12:00 to 12:00"


def test_format():
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")


def test_no_times():
    with pytest.raises(ValueError):
        convert(" to ")


def test_hours_range():
    with pytest.raises(ValueError):
        convert("13:00 AM to 13:00 PM")

    with pytest.raises(ValueError):
        convert("0:00 AM to 0:00 PM")

    with pytest.raises(ValueError):
        convert("13 AM to 13 PM")

    with pytest.raises(ValueError):
        convert("0 AM to 0 PM")


def test_minutes_range():
    with pytest.raises(ValueError):
        convert("12:61 AM to 5:60 PM")


def test_empty_input():
    with pytest.raises(ValueError):
        convert("")


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9AM to 5PM")

    with pytest.raises(ValueError):
        convert("6:19 AM 4:20 PM")

    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")