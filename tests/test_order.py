
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_init_and_properties():
    c = Customer('Test')
    coffee = Coffee('Latte')
    o = Order(c, coffee, 4.5)
    assert o.customer == c
    assert o.coffee == coffee
    assert o.price == 4.5

    with pytest.raises(ValueError):
        o.customer = 'not a customer'
    with pytest.raises(ValueError):
        o.coffee = 'not a coffee'
    with pytest.raises(ValueError):
        o.price = 0.5
    with pytest.raises(ValueError):
        o.price = 11.0

    # Test valid setters
    c2 = Customer('Test2')
    coffee2 = Coffee('Mocha')
    o.customer = c2
    o.coffee = coffee2
    o.price = 7.0
    assert o.customer == c2
    assert o.coffee == coffee2
    assert o.price == 7.0
