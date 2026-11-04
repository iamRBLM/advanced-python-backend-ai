class Shopping_cart:
    def __init__(self):
        self.items = []

    def __new__(cls, *args, **kwargs):
        print("--> __new__: Allocating memory")
        return super().__new__(cls)

    def __repr__(self):
        return f"shopping_cart(items={self.items!r}) "

    def __str__(self):
        return f"shopping_Cart with {len(self.items)} items"

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __eq__(self, other):
        return isinstance(other, Shopping_cart) and self.items == other.items

    def __add__(self, other):
        new_cart = Shopping_cart()
        new_cart.items = self.items + other.items
        return new_cart


cart = Shopping_cart()
print(f"cart before adding: {cart}")
cart.items.append("Apple")
print(f"cart after adding: {cart}")