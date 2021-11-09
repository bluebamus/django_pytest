# import pytest

# '''
# function    run once per test
# class       run once per class of tests
# module      run once per module
# session     run once per session  : 모든 테스트가 종료될때까지 한 번만 호출됨
# '''

# @pytest.fixture
# def yield_fixture():
#     print('Start Test Phase') 
#     yield 6
#     print('End Test Phase') # teardown 처럼 모든 작업 동작 후 종료


# def test_example(yield_fixture):
#     print('run-example-1')    
#     assert yield_fixture == 6