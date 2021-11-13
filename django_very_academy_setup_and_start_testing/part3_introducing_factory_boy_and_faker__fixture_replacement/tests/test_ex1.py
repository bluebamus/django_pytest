import pytest
from django.contrib.auth.models import User


# def test_new_user(new_user1):
#     print(new_user1.first_name)
#     assert new_user1.first_name == "MyName"


# def test_new_user1(new_user2):
#     print(new_user2.is_staff)
#     assert new_user2.is_staff


def test_new_user(user_factory):
    print(user_factory.username)
    assert True


@pytest.mark.django_db
def test_new_user1(user_factory):
    user=user_factory.create() # db에 데이터를 저장함
    count = User.objects.all().count()
    print('create - count : ',count)
    print('create - user.username : ',user.username)
    assert True


@pytest.mark.django_db
def test_new_user2(user_factory):
    user=user_factory.build() # db에 데이터를 저장하지 않음
    count = User.objects.all().count()
    print('build - count : ',count)
    print('build - user.username : ',user.username)
    assert True


def test_new_user3(new_user1):
    print('new_user1 - new_user1.username : ',new_user1.username)
    assert True


def test_product4(db, product_factory):
    product = product_factory.create() #category key가 없는 경우 build는 동작하지만 create는 에러가 발생함 
    print("product.description : " ,product.description)
    assert True