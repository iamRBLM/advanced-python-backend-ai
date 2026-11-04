from typing import Generic, TypeVar, List

T = TypeVar('T')


class Repository(Generic[T]):

    def __init__(self) -> None:
        self.items: List[T] = []

    def add(self, item: T) -> None:
        self.items.append(item)

    def get_by_index(self, index: int) -> T:
        return self.items[index]


string_repo = Repository[str]()
string_repo.add("Hello Generics!")
print(string_repo.get_by_index(0))
