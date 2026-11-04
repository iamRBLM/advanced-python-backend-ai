class Library:
    # 1. __new__: Allocates memory for the instance before initialization
    def __new__(cls, *args, **kwargs):
        print("--> __new__: Allocating memory for the Library object...")
        instance = super().__new__(cls)
        return instance

    # __init__: Initializes the instance attributes
    def __init__(self, name, books=None):
        print(f"--> __init__: Initializing '{name}' Library...")
        self.name = name
        self.books = books if books is not None else []

    # 2. __repr__: Developer-friendly string representation for debugging
    def __repr__(self):
        return f"Library(name={self.name!r}, books={self.books!r})"

    # 3. __str__: User-friendly string representation for print()
    def __str__(self):
        return f"'{self.name}' Library with {len(self.books)} book(s)"

    # 4. __len__: Returns the number of books when calling len(library)
    def __len__(self):
        return len(self.books)

    # 5. __getitem__: Allows accessing books using indexing, like library[0]
    def __getitem__(self, index):
        return self.books[index]

    # 6. __setitem__: Allows replacing a book using indexing, like library[0] = "New Book"
    def __setitem__(self, index, value):
        print(f"--> __setitem__: Replacing '{self.books[index]}' with '{value}'")
        self.books[index] = value

    # 7. __eq__: Compares two libraries for equality (==) based on their books
    def __eq__(self, other):
        if not isinstance(other, Library):
            return False
        return self.books == other.books

    # 8. __add__: Combines two libraries using the + operator into a new Library instance
    def __add__(self, other):
        if not isinstance(other, Library):
            raise TypeError("Can only add another Library instance")
        combined_name = f"{self.name} & {other.name}"
        combined_books = self.books + other.books
        return Library(name=combined_name, books=combined_books)


# ==========================================
# Demonstrating all Dunder Functions in action
# ==========================================
if __name__ == "__main__":
    print("=== 1 & 2. Creating Instances (__new__, __init__) ===")
    lib1 = Library("Central", ["Python Basics", "Clean Code"])
    lib2 = Library("Branch B", ["Algorithms", "Data Structures"])

    print("\n=== 3. String Representation (__str__, __repr__) ===")
    print(f"str(lib1)  -> {lib1}")
    print(f"repr(lib1) -> {repr(lib1)}")

    print("\n=== 4. Getting Length (__len__) ===")
    print(f"Total books in Central: {len(lib1)}")

    print("\n=== 5. Accessing Items by Index (__getitem__) ===")
    print(f"First book in Central: {lib1[0]}")
    print(f"Second book in Central: {lib1[1]}")

    print("\n=== 6. Updating Items by Index (__setitem__) ===")
    lib1[0] = "Advanced Python"
    print(f"Updated lib1: {lib1}")

    print("\n=== 7. Comparing Equality (__eq__) ===")
    lib3 = Library("Archive", ["Advanced Python", "Clean Code"])
    print(f"Is Central equal to Archive? {lib1 == lib3}")
    print(f"Is Central equal to Branch B? {lib1 == lib2}")

    print("\n=== 8. Adding Two Libraries Together (__add__) ===")
    merged_lib = lib1 + lib2
    print(f"Merged Result: {merged_lib}")
    print(f"Merged Catalog (repr): {repr(merged_lib)}")