from dataclasses import dataclass, field
from typing import List


class User:
    user_name: str
    age: int

    def __init__(self, user_name: str, age: int) -> None:
        self.user_name = user_name
        self.age = age


@dataclass
class Product:
    name: str
    price: float
    tags: List[str] = field(default_factory=list)


p = Product(name="laptop", price=99.99)
print(p)
