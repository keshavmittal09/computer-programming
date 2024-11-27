class Person:
    def __init__(self, name):
        self.name = name

def greet_person(person):
    print(f"Hello, {person.name}!")

p = Person("Alice")
greet_person(p)
