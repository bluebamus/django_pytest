import pytest

@pytest.mark.skip
def test_example():
    print("mark skip!!!")
    assert 1 == 1


@pytest.mark.xfail
def test_example1():
    print("mark xfail!!!")
    assert 1 == 1


# pytest -s -v -m "slow"
@pytest.mark.slow
def test_example2():
    print("mark slow!!!")
    assert 1 == 1


def test_example3():
    assert 1 == 2