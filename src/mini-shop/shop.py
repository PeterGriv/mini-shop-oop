class Product:
    def __init__(self, sku: str, name: str, price: float):
        self.sku = sku
        self.name = name
        self.price = price
        pass

    def __str__(self):
        return f"{self.name} (SKU: {self.sku}) –> {self.price} €"
        pass

class Cart:
    def __init__(self):
        self.products = []
        pass

    def add_product(self, product):
        self.products.append(product)
        pass

    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price        
        return total

def main():
    p1 = Product(7255,"Pergola", 198)
    p2 = Product(2724,"Wingarden", 378)
    cart = Cart()
    cart.add_product(p1)
    cart.add_product(p2)

    for product in cart.products:
        print(product)
    
    print("Total price:", cart.total_price(), "€")
    

if __name__ == "__main__":
    main()