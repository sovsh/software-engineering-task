from simple_factorial import fact

def test_1():
    assert fact(3) == 6

def test_2():
    assert fact(-3) == 0

def test_3():
    assert fact(0) == 1

def test_4():
    assert fact(10) == 3628800