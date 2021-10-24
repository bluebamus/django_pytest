"""
This module contains basic unit tests for the accum module.
Their purpose is to show how to use the pytest framework by example.
"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import pytest
from stuff.accum import Accumulator

# --------------------------------------------------------------------------------
# Fixtures
# --------------------------------------------------------------------------------

# scope 옵션을 통해 해당 fixture가 생성 후 사용될 범위 설정 가능 module, session 등
@pytest.fixture
def accum():
  return Accumulator() 
# yield

"""
pytest는 fixtrue의 범위를 벗어 났을 때 특정 fixtuer의 종료 코드 실행을 지원합니다. 
return 대신 yield문을 사용하면 yield문 다음의 모든 코드가 teardown 코드로 사용됩니다.
"""


# --------------------------------------------------------------------------------
# Tests
# --------------------------------------------------------------------------------

def test_accumulator_init(accum):
  assert accum.count == 0


def test_accumulator_add_one(accum):
  accum.add()
  assert accum.count == 1


def test_accumulator_add_three(accum):
  accum.add(3)
  assert accum.count == 3


def test_accumulator_add_twice(accum):
  accum.add()
  accum.add()
  assert accum.count == 2


def test_accumulator_cannot_set_count_directly(accum):
  with pytest.raises(AttributeError, match=r"can't set attribute") as e:
    accum.count = 10