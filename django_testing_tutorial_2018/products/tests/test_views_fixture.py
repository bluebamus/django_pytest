from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser, User
from mixer.backend.django import mixer
from products.views import product_detail
import pytest


@pytest.fixture(scope='module')
def factory():
    print("FACTORY INSTANTIATE")
    return RequestFactory()


@pytest.fixture
def product(db):
    return mixer.blend('products.Product')

# @pytest.mark.django_db
# def test_product_detail_authenticated(factory, db):
def test_product_detail_authenticated(factory, product):    
    path = reverse('detail',kwargs={'pk':1})
    request = factory.get(path)
    request.user = mixer.blend(User)

    response = product_detail(request, pk=1)
    assert response.status_code == 200

# @pytest.mark.django_db
# def test_product_detail_unauthenticated(factory, db):
def test_product_detail_unauthenticated(factory, product):    
    
    path = reverse('detail',kwargs={'pk':1})
    request = factory.get(path)
    request.user = AnonymousUser()

    response = product_detail(request, pk=1)
    # assert response.status_code == 200
    assert 'accounts/login' in response.url