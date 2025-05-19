#  Coffee Shop Domain Model

A beginner-friendly Python project that models the operations of a coffee shop using object-oriented programming (OOP). This simple simulation includes customers placing orders for different types of coffee, tracking purchases, and calculating spending statistics.

---
## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/shawn254ke/coffee_shop.git
cd coffee_shop
```
# Coffee Shop Domain Model (Beginner Version)

##  Project Overview

This project models a basic Coffee Shop system using object-oriented programming in Python.  
It simulates real-world entities such as `Customer`, `Coffee`, and `Order` with clear relationships.

Designed for learning and demonstrating:
- Object-oriented design principles
- Class relationships (many-to-many through intermediary)
- Property validation
- Simple data aggregation
- Unit testing with `pytest`

---

##  Project Structure

```
coffee_shop/
├── customer.py        # Customer class
├── coffee.py          # Coffee class
├── order.py           # Order class (many-to-many intermediary)
├── debug.py           # Manual test run
└── tests/             # Unit test directory
    ├── test_customer.py
    ├── test_coffee.py
    └── test_order.py
```

---

##  Features

- A `Customer` can place many `Orders`
- A `Coffee` can have many `Orders`
- Each `Order` belongs to one `Customer` and one `Coffee`
- Tracks all instances in class-level lists
- Validates:
  - Customer name: string, 1–15 characters
  - Coffee name: string, ≥ 3 characters
  - Order price: float between 1.0 and 10.0

---

##  Testing

Tests are written using `pytest`.

### Run all tests:
```bash
pytest
```

---


### Run the debug script

```bash
python debug.py
```

Expected Output:
```
Most Aficionado for Latte: Alice
Latte Average Price: 4.5
Alice Coffees: ['Latte']
```

---

##  Concepts Practiced

- Classes and objects
- Class methods and instance methods
- Encapsulation with properties
- Relationships between objects (1-to-many, many-to-many)
- Input validation and error handling
- List comprehensions and filtering
- Unit testing using `pytest`

---

##  Author

Shawn Otieno

---

