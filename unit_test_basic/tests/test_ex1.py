# https://dev-jacob.tistory.com/entry/Django-%EC%9C%A0%EB%8B%9B-%ED%85%8C%EC%8A%A4%ED%8A%B8-with-Pytest-1

import pytest 

@pytest.mark.slow
@pytest.mark.xfail
def test_example():
    print("1 테스트 코드 입니다") 
    assert 1 ==1

@pytest.mark.xfail
def test_example1():
    print("2 테스트 코드 입니다") 
    assert 1 ==2

@pytest.mark.xfail
def test_example2():
    print("3 실패 테스트 코드 입니다") 
    assert 1 ==1

@pytest.mark.xfail
def test_example3():
    print("4 실패 테스트 코드 입니다") 
    assert 1 ==2

@pytest.mark.skip
def test_failed_example1(): 
    print("메인 서브 코드 입니다")
    assert 1 == 1
