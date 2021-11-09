# import pytest
# from django.contrib.auth.models import User

# # fixture db 결과가 공유되지 않음, 각각의 테스트 후 데이터 플래쉬

# @pytest.mark.django_db
# def test_user_create():
#     User.objects.create_user('test','test@test.com','test')
#     count = User.objects.all().count()
#     print(count)
#     assert User.objects.count() == 1


# @pytest.mark.django_db
# def test_user_create1():    
#     count = User.objects.all().count()    
#     print(count)
#     assert User.objects.count() == 0