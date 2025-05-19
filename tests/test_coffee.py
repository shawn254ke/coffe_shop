
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee('A')
    with pytest.raises(ValueError):
        Coffee(123)
    c = Coffee('Latte')
    assert c.name == 'Latte'

def test_orders_and_customers():
    c1 = Customer('A')
    c2 = Customer('B')
    coffee = Coffee('Mocha')
    Order._all.clear()
    o1 = Order(c1, coffee, 4.0)
    o2 = Order(c2, coffee, 5.0)
    assert set(coffee.customers()) == {c1, c2}
    assert set(coffee.orders()) == {o1, o2}

def test_num_orders_and_average_price():
    c = Customer('C')
    coffee = Coffee('Espresso')
    Order._all.clear()
    assert coffee.num_orders() == 0
    assert coffee.average_price() == 0
    Order(c, coffee, 4.0)
    Order(c, coffee, 6.0)
    assert coffee.num_orders() == 2
    assert coffee.average_price() == 5.0
