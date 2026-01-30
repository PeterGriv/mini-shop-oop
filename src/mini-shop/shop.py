class Product:
    def __init__(self, sku: str, name: str, price: float):
        self.sku = sku
        self.name = name
        self.price = price

        pass

    def __str__(self):
        return f"{self.name} (SKU: {self.sku}) –> {self.price} €"
        pass



def main():
    p = Product(7255,"Pergola", 198)
    print(p.name, p.price)
    print(p)

if __name__ == "__main__":
    main()