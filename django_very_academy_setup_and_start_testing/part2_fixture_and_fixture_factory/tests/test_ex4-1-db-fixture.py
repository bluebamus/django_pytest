import pytest
from django.contrib.auth.models import User


@pytest.fixture()
def user_1(db):
    user = User.objects.create_user("test-user")
    return user


def test_set_check_password_true(user_1):
    assert user_1.username == "test-user"
