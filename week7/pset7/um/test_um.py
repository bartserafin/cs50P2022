from um import count

def test_um_case():
    assert count("UM") == 1
    assert count("Um") == 1
    assert count("Hello, Um... um... um...") == 3
    assert count("Hello, uM.") == 1
    assert count("Hello, um.") == 1
    assert count("Hello, uhm, my name is human.") == 0


def test_um_positions():
    assert count("um, Hello") == 1
    assert count("Um hello") == 1
    assert count("hello Um") == 1
    assert count(" hello um?") == 1
    assert count("UM ...hello") == 1
    assert count("UMM ...hello??.") == 0


def test_um_edge_cases():
    assert count("Um? Hello, um, hello.") == 2
    assert count("UM!, um, hello?") == 2
    assert count("Hello! hello? Um?") == 1
    assert count("Snake? Snake? SNAKEE!!! U.m?") == 0
    assert count("Snake? Snake? SNAKEE!!! U m!") == 0