
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from customer import Customer
from coffee import Coffee

class DummyOrder:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer(123)
    with pytest.raises(ValueError):
        Customer('')
    with pytest.raises(ValueError):
        Customer('a'*16)
    c = Customer('Alice')
    assert c.name == 'Alice'

def test_customer_orders_and_coffees(monkeypatch):
    c = Customer('Bob')
    coffee1 = Coffee('Latte')
    coffee2 = Coffee('Mocha')
    # Patch Order._all
    class DummyOrder:
        def __init__(self, customer, coffee, price):
            self.customer = customer
            self.coffee = coffee
            self.price = price
    dummy_orders = [DummyOrder(c, coffee1, 4.0), DummyOrder(c, coffee2, 5.0)]
    monkeypatch.setattr('order.Order._all', dummy_orders)
    assert set(c.coffees()) == {coffee1, coffee2}
    assert len(c.orders()) == 2

def test_create_order():
    c = Customer('Eve')
    coffee = Coffee('Americano')
    order = c.create_order(coffee, 4.5)
    from order import Order
    assert isinstance(order, Order)
    assert order.customer == c
    assert order.coffee == coffee
    assert order.price == 4.5

def test_most_aficionado():
    c1 = Customer('A')
    c2 = Customer('B')
    coffee = Coffee('Cappuccino')
    from order import Order
    Order._all.clear()
    Order(c1, coffee, 5.0)
    Order(c2, coffee, 6.0)
    Order(c2, coffee, 2.0)
    assert Customer.most_aficionado(coffee) == c2
    assert Customer.most_aficionado(Coffee('Nonexistent')) is None
