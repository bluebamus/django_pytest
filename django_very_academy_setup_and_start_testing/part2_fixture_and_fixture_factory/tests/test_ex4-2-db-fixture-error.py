import pytest
from django.contrib.auth.models import User


@pytest.fixture(scope="session")  # error
def user_1(db):
    user = User.objects.create_user("test-user")
    print("create-user")
    return user


def test_set_check_password1(user_1):
    print("check-user1")
    assert user_1.username == "test-user"


def test_set_check_password2(user_1):
    print("check-user2")
    assert user_1.username == "test-user"
