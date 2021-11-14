import pytest
from app1.models import Product

@pytest.mark.parametrize(
    "title, category, description, slug, regular_price, discount_price, validity",
    [
        ("NewTitle", 1, "NewDescription", "slug", "4.99", "3.99", True), # 첫번째 parameter는 pass함
        #("NewTitle", 1, "NewDescription", "slug", "", "3.99", False), # 두번째 parameter는 regular_price 데이터가 없으므로 에러 발생
    ],
)
#@pytest.mark.django_db
def test_product_instance(
    db, product_factory, title, category, description, slug, regular_price, discount_price, validity
):

    test = product_factory(
        title=title,
        category_id=category,
        description=description,
        slug=slug,
        regular_price=regular_price,
        discount_price=discount_price,
    )

    item = Product.objects.all().count()
    print(item)
    assert item == validity
