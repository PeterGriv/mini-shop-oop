# Mini Shop OOP (Python)

A small Python project that demonstrates object-oriented programming (OOP) through a simple shopping cart domain model.

The goal is not to build a full e-shop, just to model core shopping cart logic:
- products
- cart items (product + quantity)
- cart operations (add/remove with quantity handling)
- cart total calculation

---

## What it does

- Creates `Product` objects (SKU, name, price)
- Adds products to a cart:
  - if the product already exists in the cart, it increases quantity
  - otherwise it creates a new cart item
- Removes products from a cart:
  - decreases quantity
  - removes the item completely if quantity < 1 
- Calculates the cart total by summing line totals

---

## Why this project

Project demonstrates:
- basic OOP design (classes, objects, methods, `self`)
- separation of responsibilities:
  - `Product` holds product data
  - `CartItem` represents a product + quantity and computes line totals
  - `Cart` manages a collection of items and implements cart behavior
- working with state (updating quantities)
- simple, readable Python code without external dependencies

---

## Requirements

- Python 3.9+
- No other dependencies (just standard library)

---

## Usage

Run the script:

```bash
python shop.py
```

The main() function contains a simple demo:
•	create products
•	add/remove items in the cart
•	print line totals and cart total 


## Project structure 

shop.py    # OOP model + demo main() 
README.md 

