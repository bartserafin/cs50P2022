from twttr import shorten

def test_shorten():
    assert shorten("Hello") == "Hll"
    assert shorten("ABCDE") == "BCD"
    assert shorten("123ab") == "123b"
    assert shorten("ab,cde!?") == "b,cd!?"