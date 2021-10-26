from functools import partial
from pytest_bdd import scenario, scenarios , parsers, given, when, then
import pytest
from cucumbers import CucumberBasket

# @scenario('../features/cucumbers_basic.feature', 'Add cucumbers to a basket')
# def test_add():
#     pass

# @scenario('../features/cucumbers_basic.feature', 'Remove cucumbers to a basket')
# def test_remove():
#     pass

scenarios('../features/cucumbers_basic.feature')


EXTRA_TYPES = {
    'Number' : int,
}

parse_num = partial(parsers.cfparse,extra_types=EXTRA_TYPES)

@pytest.fixture
@given(parse_num('the basket has "{initial:Number}" cucumbers')) # extra_types=dict(Number=int)))
def basket(initial):
    return CucumberBasket(initial_count=initial)


#@when(parsers.cfparse('"{some:Number}" cucumbers are added to the basket', extra_types=EXTRA_TYPES)) # extra_types=dict(Number=int)))
@when(parse_num('"{some:Number}" cucumbers are added to the basket'))
def add_cucumbers(basket, some):
    basket.add(some)


# @when(parsers.cfparse('"{some:Number}" cucumbers are removed from the basket', extra_types=dict(Number=int)))
# def remove_cucumbers(basket, some):
#    basket.remove(some)

#@when(parsers.cfparse('"{some:Number}" cucumbers are removed from the basket', extra_types=EXTRA_TYPES)) # extra_types=dict(Number=int)))
@when(parse_num('"{some:Number}" cucumbers are removed from the basket'))
def step_impl(basket, some):
   basket.remove(some)

#@then(parsers.cfparse('the basket contains "{total:Number}" cucumbers', extra_types=EXTRA_TYPES)) # extra_types=dict(Number=int)))
@then(parse_num('the basket contains "{total:Number}" cucumbers'))
def basket_has_total(basket, total):
    assert basket.count == total