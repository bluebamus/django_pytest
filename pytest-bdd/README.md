# django_pytest
[동영상 강의 https://testautomationu.applitools.com/behavior-driven-python-with-pytest-bdd/](https://testautomationu.applitools.com/behavior-driven-python-with-pytest-bdd/)

[github : https://github.com/AndyLPK247/tau-pytest-bdd ](https://github.com/AndyLPK247/tau-pytest-bdd)

[pytest-bdd pypl](https://pypi.org/project/pytest-bdd/)

# BDD TEST의 정의
[참고 사이트 www.popit.kr](https://www.popit.kr/bdd-behaviour-driven-development%EC%97%90-%EB%8C%80%ED%95%9C-%EA%B0%84%EB%9E%B5%ED%95%9C-%EC%A0%95%EB%A6%AC/)
## TDD 는
- 흔히 알려진 것처럼 TDD는 테스트를 먼저 작성하고 그 테스트를 통과시키는 코드를 작성하는 흐름을 기본으로 한다. 
- 게다가 테스트 단위도 함수 단위로 매우 작아서 작성하는 거의 모든 함수가 테스트 대상에 포함된다. 
- 이상적으로 보일 수 있지만 그만큼 현업에서 사용하기에는 괴리감이 있다.
   

> 프로젝트 초기에 야심 차게 TDD를 도입하여 거의 모든 함수에 대한 테스트 케이스를 준비했더라도 개발 중후반에 수정되는 내용에 대해서 깨지는 테스트 케이스를 계속 유지하면서 가져가기란 쉽지 않다. 게다가 로우 레벨의 함수를 나누고 합치고 시그니쳐를 변경하는 리팩토링이라도 하는 날에는 관련 테스트는 모두 깨지며 이를 일일이 맞춰간다는 건 쉽지 않다. 이 말이 어떤 의미인지 실제 TDD를 현업에서 사용해본 사람은 욕지기와 함께 감이 올 것이다.

## 그렇다면 BDD는
- 이제 BDD를 살짝 보자. 참고로 여기서 이야기하는 BDD는 내가 사용하면서 이해하고 있는 것이라서 진정한 BDD와 차이가 있을 수도 있다.

- BDD가 TDD와 엄청난 차이를 보이지는 않는다고 위에 언급했지만, 개인적인 생각은 다음과 같다.

## TDD와는 다르다 TDD와는! (이 뉘앙스를 아는가?)

> BDD는 시나리오를 기반으로 테스트 케이스를 작성하며 함수 단위 테스트를 권장하지 않는다. 이 시나리오는 개발자가 아닌 사람이 봐도 이해할 수 있을 정도의 레벨을 권장한다. 하나의 시나리오는 Given, When, Then 구조를 가지는 것을 기본 패턴으로 권장하며 각 절의 의미는 다음과 같다.

- Feature : 테스트에 대상의 기능/책임을 명시한다.
- Scenario : 테스트 목적에 대한 상황을 설명한다.

- Given : 시나리오 진행에 필요한 값을 설정한다.

- When : 시나리오를 진행하는데 필요한 조건을 명시한다.

- Then : 시나리오를 완료했을 때 보장해야 하는 결과를 명시한다.

### bug fix
- https://stackoverflow.com/questions/65084044/pytest-fixture-not-found-pytest-bdd
  - pytest.fixture 데코레이터를 선언해 줘야 동작함 (버전 차이로 보임) 
- https://github.com/pytest-dev/pytest-bdd/issues/293
- https://moduscreate.com/blog/python-automation-testing/