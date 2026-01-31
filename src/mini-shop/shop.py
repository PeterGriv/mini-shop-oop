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
        item = CartItem(product, qty)
        self.items.append(item)


def main():
    p1 = Product("S7R8", "Arturia Minilab Mk III", 119.99) 
    p2 = Product("BG33", "Arturia MiniFuse II", 99.99) 
    print(p1)
    print(p2)
    i = CartItem(p1,4)
    cart = Cart()
    cart.add_product(p1,4)
    cart.add_product(p2,3)
    print(cart.items[0].line_total())
    for item in cart.items:
        print(item.line_total())



if __name__ == "__main__":
    main()