from week7.pset7.numb3rs.numb3rs import validate


def test_lentgh():
    assert validate('127.123.123.123') == True
    assert validate('127.123.123') == False

def test_chars():
    assert validate("abc.def.abc.def") == False
    assert validate("123.def.abc.def") == False
    assert validate("abc.123.abc.def") == False
    assert validate("abc.def.123.def") == False
    assert validate("abc.def.abc.123") == False

def test_range():
    assert validate("300.123.123.123") == False
    assert validate("123.300.123.123") == False
    assert validate("123.123.300.123") == False
    assert validate("123.123.123.300") == False
