# django_pytest
- 모든 프로젝트는 Blog Post Project, 온라인 강좌의 Project 별로 폴더 생성이 되어 있습니다.
- 각 폴더에는 README.md 파일이 있으며 학습으로 참고된 사이트의 URL 정보가 저장되어 있습니다.

# 학습 순서
> 학습 순서는 제가 임의로 정한 순서이며, 순서상 이전 학습으로 불필요하다 생각된 내용은 이후 프로젝트에서 code로 다루지 않았습니다.

# 라이브러리별 공식 사이트
1. [factoryboy](https://factoryboy.readthedocs.io/en/stable/reference.html)
2. [faker](https://faker.readthedocs.io/en/master/)
3. [pytest-django](https://pytest-django.readthedocs.io/en/latest/)
4. [pytest 1](https://docs.pytest.org/en/6.2.x/)
5. [pytest 2](https://docs.pytest.org/en/6.2.x/contents.html)
# pytest 기초
1. [unit_testing_with_pytest *](https://coursesfree.org/course/python-3-unit-testing-with-pytest/)
2. [unit_test_basic](https://dev-jacob.tistory.com/entry/Django-%EC%9C%A0%EB%8B%9B-%ED%85%8C%EC%8A%A4%ED%8A%B8-with-Pytest-1)
3. [introduction_to_pytest  ***](https://testautomationu.applitools.com/pytest-tutorial/chapter7.html)
4. pytest-bdd ( 학습 중지 )
### youtube :: pytest with django Study
1. [django_testing_tutorial_2018 *](https://www.youtube.com/watch?v=B-qYGeLpUtE&t=5s)
2. [django_very_academy_setup_and_start_testing ***](https://www.youtube.com/watch?v=LYX6nlECcro&list=PLOLrQ9Pn6caw3ilqDR8_qezp76QuEOlHY)
   1. [veryacademy/pytest-mastery-with-django](https://github.com/veryacademy/pytest-mastery-with-django)
   2. [veryacademy/selenium-mastery-with-django](https://github.com/veryacademy/selenium-mastery-with-django)
3. [django_besnard_consulting_testing](https://www.youtube.com/watch?v=6pYrwjAMXmE)
4. [django_kenyan_engineer_pytest_django_and_django_rest_framework](https://www.youtube.com/watch?v=KIIdbVs7e8I&list=PLP1DxoSC17LZTTzgfq0Dimkm6eWJQC9ki) * rest 프로젝트 이후 학습 예정
5. [Jonghyun Park: 파이썬에서 편하게 테스트 케이스 작성하기: pytest, Travis CI, 그리고 도커](https://www.youtube.com/watch?v=rxCjxX4tT1E&t=1696s)

### Blog/Site :: pytest with django Study
1. [Selenium WebDriver with Python](https://testautomationu.applitools.com/selenium-webdriver-python-tutorial/)
2. [PyTest 프레임워크 기초 사용법](https://jangseongwoo.github.io/test/pytest_basic/)
3. [PYTEST DOCUMENT](https://mjyoo2.github.io/pytest_document_KR/pytest%20document/installation-and-getting-start/)
4. [Effective Python Testing With Pytest](https://realpython.com/pytest-python-testing/)
5. [How to Provide Test Fixtures for Django Models in Pytest](https://realpython.com/django-pytest-fixtures/)
6.  [Pytest 소개](https://velog.io/@sangyeon217/pytest)
7. [단위 테스트 pytest-django 튜토리얼](https://jadehan.tistory.com/4)
8. [End-To-End Tutorial For Pytest Fixtures With Examples](https://www.lambdatest.com/blog/end-to-end-tutorial-for-pytest-fixtures-with-examples/)


# 옵션 기록
### durations
- pytest --durations=0 — Show all times for tests and setup and teardown
- pytest --durations=1 — Just show me the slowest
- pytest --durations=50 — Slowest 50, with times, … etc
- 참고 : https://stackoverflow.com/questions/27884404/printing-test-execution-times-and-pinning-down-slow-tests-with-py-test

### 추가 학습
1. [Python Faker - Generate Fake Data for a Database with Django Example](https://www.youtube.com/watch?v=8LHdbaV7Dvo)

* django_testing_tutorial_2018는 mixer.blend를 이용해 fixture를 구현, DB 데이터를 사용함
* django_very_academy_setup_and_start_testing는 conftest.py를 이용하여 fixture factory를 직접 구현, DB 데이터를 사용함 (한번 만든 데이터를 누적, 반복 사용할 수 있음[ini 파일에 옵션 설정이 필요함])