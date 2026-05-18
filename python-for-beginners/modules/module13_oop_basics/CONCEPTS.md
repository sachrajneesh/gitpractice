# Module 13 Concepts: OOP Basics

> This is a stub. Full content will be added in a future revision.

---

## What is a class?

A class is a blueprint for creating objects. An object bundles together related
data (attributes) and behaviour (methods).

Think of a class as a cookie cutter. You define the shape once. Every cookie
(object) you make from it has the same shape but its own distinct content.

---

## Defining a class

```python
class Dog:
    """Represents a dog."""

    def __init__(self, name, breed, age):
        """Initialise a new Dog."""
        self.name = name       # instance attribute
        self.breed = breed
        self.age = age

    def bark(self):
        """Make the dog bark."""
        print(f"{self.name} says: Woof!")

    def describe(self):
        """Print a description of this dog."""
        print(f"{self.name} is a {self.age}-year-old {self.breed}.")

    def __str__(self):
        """Return a readable string representation."""
        return f"Dog({self.name}, {self.breed}, age={self.age})"


# Creating objects (instances)
dog1 = Dog("Rex", "Labrador", 3)
dog2 = Dog("Bella", "Poodle", 5)

dog1.bark()         # Rex says: Woof!
dog2.describe()     # Bella is a 5-year-old Poodle.
print(dog1)         # Dog(Rex, Labrador, age=3)   — uses __str__
```

- `__init__` is called automatically when you create an object.
- `self` refers to the specific object being created or used.
- Every method must have `self` as its first parameter.

---

## Inheritance

Inheritance lets one class (the subclass) build on top of another (the parent class).
The subclass inherits all attributes and methods of the parent.

```python
class Animal:
    """A generic animal."""

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}!")


class Cat(Animal):
    """A cat — inherits from Animal."""

    def __init__(self, name):
        super().__init__(name, "Meow")   # call the parent __init__

    def purr(self):
        print(f"{self.name} purrs contentedly.")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")


fluffy = Cat("Fluffy")
rex = Dog("Rex")

fluffy.speak()    # Fluffy says Meow!   — inherited from Animal
fluffy.purr()     # Fluffy purrs contentedly.  — unique to Cat
rex.speak()       # Rex says Woof!
```

---

## Next steps

Run the exercise. Then move to Module 14: Mini Projects.
