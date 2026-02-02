class Product:
    def __init__(self, sku: str, name: str, price: float):
        self.sku = sku
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}  |  (SKU: {self.sku}) -> {self.price} €"
    

class CartItem:
    def __init__(self, product, qty: int):
        self.product = product
        self.qty = qty

    def line_total(self):
        return self.product.price * self.qty 


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, qty: int):
        for item in self.items:
            if item.product == product:  
                item.qty += qty
                return
        self.items.append(CartItem(product, qty))

    def remove_product(self, product, qty: int):
        for item in self.items:
            if item.product == product:
                item.qty -= qty 
                if item.qty <= 0:
                    self.items.remove(item)
                return

    def total(self):
        total_sum = 0
        for item in self.items:
            total_sum += item.line_total()
        return total_sum


def main():
    p1 = Product("S7R8", "Arturia Minilab Mk III", 119.99) 
    p2 = Product("BG33", "Arturia MiniFuse II", 99.99) 
    print(p1)
    print(p2)
    cart = Cart()
    cart.add_product(p1,4)
    cart.add_product(p2,3)
    for item in cart.items:
        print(item.line_total())
    print(f"Total cost of all products is: {cart.total()} €")


if __name__ == "__main__":
    main()