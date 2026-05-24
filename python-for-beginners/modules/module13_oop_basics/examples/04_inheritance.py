"""Demonstrates: simple inheritance, method override, and super()"""

# ---------------------------------------------------------------
# INHERITANCE lets one class (child) automatically get all the
# attributes and methods of another class (parent).
# The child can then:
#   - USE the parent's methods as-is
#   - OVERRIDE a parent method (replace it with a new version)
#   - EXTEND a method (call the parent version PLUS add more)
#
# Syntax: class ChildClass(ParentClass):
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# --- Parent class ---
# ---------------------------------------------------------------

class Animal:
    """A generic animal."""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.energy = 100

    def eat(self, food):
        """Eat food to restore energy."""
        self.energy += 20
        print(f"{self.name} eats {food}. Energy: {self.energy}")

    def sleep(self):
        """Sleep to restore energy fully."""
        self.energy = 100
        print(f"{self.name} has a nap. Energy restored.")

    def speak(self):
        """Make a sound — subclasses will override this."""
        print(f"{self.name} makes a sound.")

    def __str__(self):
        return f"{self.name} (age {self.age})"


# ---------------------------------------------------------------
# --- Child classes that inherit from Animal ---
# ---------------------------------------------------------------

class Dog(Animal):
    """A dog — inherits from Animal."""

    def __init__(self, name, age, breed):
        # super().__init__() calls the PARENT's __init__
        # so we don't duplicate the name/age/energy setup
        super().__init__(name, age)
        self.breed = breed   # extra attribute specific to Dog

    def speak(self):
        """Override Animal's speak — dogs bark."""
        print(f"{self.name} says: Woof!")

    def fetch(self, item):
        """Dog-specific method — doesn't exist in Animal."""
        self.energy -= 10
        print(f"{self.name} fetches the {item}! Energy: {self.energy}")


class Cat(Animal):
    """A cat — also inherits from Animal."""

    def __init__(self, name, age, indoor=True):
        super().__init__(name, age)
        self.indoor = indoor

    def speak(self):
        """Override Animal's speak — cats meow."""
        print(f"{self.name} says: Meow!")

    def purr(self):
        """Cat-specific method."""
        print(f"{self.name} purrs contentedly...")


# ---------------------------------------------------------------
# --- Using the classes ---
# ---------------------------------------------------------------

print("=== Dog ===")
rex = Dog("Rex", 3, "Labrador")
print(rex)             # uses Animal's __str__
rex.eat("dog biscuits")  # inherited from Animal
rex.speak()            # overridden in Dog → Woof!
rex.fetch("ball")      # Dog-specific
rex.sleep()            # inherited from Animal

print("\n=== Cat ===")
whiskers = Cat("Whiskers", 5)
print(whiskers)
whiskers.eat("tuna")   # inherited from Animal
whiskers.speak()       # overridden in Cat → Meow!
whiskers.purr()        # Cat-specific

# ---------------------------------------------------------------
# --- isinstance() checks work up the inheritance chain ---
# ---------------------------------------------------------------
print("\n=== Type checks ===")
print(f"rex is Dog:    {isinstance(rex, Dog)}")      # True
print(f"rex is Animal: {isinstance(rex, Animal)}")  # True! Dog inherits from Animal
print(f"rex is Cat:    {isinstance(rex, Cat)}")     # False

# ---------------------------------------------------------------
# --- Polymorphism — calling speak() on a mix of animals ---
# ---------------------------------------------------------------
print("\n=== Polymorphism ===")
animals = [Dog("Buddy", 2, "Poodle"), Cat("Luna", 4), Dog("Max", 6, "Husky")]

for animal in animals:
    animal.speak()   # Python calls the RIGHT speak() for each type automatically!
