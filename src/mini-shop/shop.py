class Product:
    def __init__(self, name):
        self.name = name
        pass


def main():
    p = Product("Pergola")
    print(p.name)

if __name__ == "__main__":
    main()