from customer import Customer
from coffee import Coffee
from order import Order

# Create instances
alice = Customer("Alice")
bob = Customer("Bob")

latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create orders
alice.create_order(latte, 4.5)
alice.create_order(latte, 5.0)
bob.create_order(latte, 4.0)
bob.create_order(espresso, 3.5)

print("Most Aficionado for Latte:", Customer.most_aficionado(latte).name)
print("Latte Average Price:", latte.average_price())
print("Alice Coffees:", [c.name for c in alice.coffees()])