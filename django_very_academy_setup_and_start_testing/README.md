# django_pytest
[Pytest | Django | Gentle Introduction, Setup and Start Testing](https://www.youtube.com/watch?v=LYX6nlECcro&t=5s)
[github](https://github.com/veryacademy/pytest-mastery-with-django)
* github와 영상의 source code 내용이 차이가 있다. 비교하며 사용해도 득이 될듯
# python Testing Frameworks
- Robot
- PyTest
- Unittest
- DocTest
- Nose2
- Testify

1. [Pytest | Django | Gentle Introduction, Setup and Start Testing](https://www.youtube.com/watch?v=LYX6nlECcro&list=PLOLrQ9Pn6caw3ilqDR8_qezp76QuEOlHY&index=6&t=10s)
2. [Pytest | Django | Introducing Fixtures and Fixture Factory](https://www.youtube.com/watch?v=s8iPADSichU&list=PLOLrQ9Pn6caw3ilqDR8_qezp76QuEOlHY&index=3)
   1. conftest를 사용하면 반복해서 사용되는 fixture를 사전에 정의, 다양한 테스트 모듈에서 재활용하여 사용 가능함
3. [Pytest | Django | Introducing Factory Boy and Faker - Fixture Replacement](https://www.youtube.com/watch?v=qrvqNdCDKjM&list=PLOLrQ9Pn6caw3ilqDR8_qezp76QuEOlHY&index=4)
   1. 시나리오 : email, username + pwd1, pwd2 
      1. email format
      2. email unique
      3. username format
      4. username unique
      5. pwd1 == pwd2
4. [Towards Parametrizing Fixtures and Test Functions](https://www.youtube.com/watch?v=APhI43fyRHI&list=PLOLrQ9Pn6caw3ilqDR8_qezp76QuEOlHY&index=5)
   - mixer.blend, faker랑 비교해서 자동 생성에 대한 효율성에 대해 비교해볼 필요가 있음
5. [Pytest | Selenium | Python Django - Intro Testing with Pytest, Selenium and Django](https://www.youtube.com/watch?v=o_rubsSu-Ds&list=PLOLrQ9Pn6caw3ilqDR8_qezp76QuEOlHY&index=6)
   1. 
6. [Pytest | Selenium | Taking Screenshots](https://www.youtube.com/watch?v=SWBytYYVINE&list=PLOLrQ9Pn6caw3ilqDR8_qezp76QuEOlHY&index=7)

* chromedriver의 버전을 최신버전으로 받았더니 96버전이라서 현재 브라우저와 버전이 맞지 않는다고 에러가 발생함 이는 "--headless" 옵션을 주어도 마찬가지로 발생함