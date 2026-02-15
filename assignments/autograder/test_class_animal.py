import shell 
import unittest
import os
from gradescope_utils.autograder_utils.decorators import weight, number
from gradescope_utils.autograder_utils.files import check_submitted_files
from random import randint, shuffle

class TestClassAnimal(shell.TestShell):

	def setUp(self):
		self.py_asg_file = 'animal.py'
		super().setUp()

	@weight(3)
	@number("1")
	def test_abstract(self):
		"""Test Animal"""
		try:
			from animal import Animal as stud_Animal
			a = stud_Animal("Abstract")
			self.fail("Animal class must be abstract and not instantiable.")
		except TypeError:
			# Doesn't work because __repr__ is always inherited
			#if not hasattr(stud_Animal, "__repr__"):
			#	self.fail("Class Animal does not have a __repr__ method.")
			pass
		except ImportError:
			self.fail("Can't find class Animal.")

	@weight(3)
	@number("2")
	def test_dog(self):
		"""Test Dog"""
		try:
			from animal import Dog as stud_Dog
			a = stud_Dog("Scooter", "corgi")
			self.assertEqualShellOutput(a.name, "Scooter", msg="Name mismatch!")
			self.assertEqualShellOutput(a.breed, "corgi", msg="Breed mismatch!")
		except TypeError:
			self.fail("Can't instantiate Dog(\"Scooter\", \"corgi\").")
		except ImportError:
			self.fail("Can't find class Dog.")

	@weight(2)
	@number("3")
	def test_repr(self):
		"""Test repr"""
		try:
			from animal import Dog as stud_Dog
			a = stud_Dog("Scooter", "corgi")
			b = Dog("Scooter", "corgi")
			self.assertEqualShellOutput(a.__repr__(), b.__repr__(),
                                                    msg="__repr__ output mismatch.")
		except:
			raise

	@weight(3)
	@number("4")
	def test_all_animals(self):
		"""Test all animals"""
		try:
			from animal import Dog as stud_Dog
			from animal import Animal as stud_Animal
			stud_Animal.all_animals = {}
			Animal.all_animals = {}
			a1 = stud_Dog("Scooter", "corgi")
			a2 = stud_Dog("X", "y")
			b1 = Dog("Scooter", "corgi")
			b2 = Dog("X", "y")
			self.assertEqualShellOutput(str(a1.all_animals), str(b1.all_animals),
                                                    msg="all_animals dictionary mismatch.")
		except:
			raise

	@weight(3)
	@number("5")
	def test_cat(self):
		"""Test cat"""
		try:
			from animal import Cat as stud_Cat
			a = stud_Cat("Yellow", "Black")
			b = Cat("Yellow", "Black")
			self.assertEqualShellOutput(a.__repr__(), b.__repr__(),
                                                    msg="Cat __repr__ output mismatch.")
		except:
			raise

	@weight(3)
	@number("6")
	def test_list(self):
		"""Test list"""
		try:
			from animal import Animal as stud_Animal
			from animal import Cat as stud_Cat
			from animal import Dog as stud_Dog
			stud_Animal.all_animals = {}
			Animal.all_animals = {}
			a1 = stud_Cat("Mike", "White")
			a2 = stud_Dog("Boxer", "Doberman")
			b1 = Cat("Mike", "White")
			b2 = Dog("Boxer", "Doberman")
			self.assertEqualShellOutput(stud_Animal.listAnimals(), Animal.listAnimals(),
                                                    msg="listAnimals() output mismatch.")
		except:
			raise

	@weight(3)
	@number("7")
	def test_kennel(self):
		"""Test kennel"""
		try:
			from animal import Kennel as stud_Kennel
			from animal import Cat as stud_Cat
			from animal import Dog as stud_Dog
			a1 = stud_Cat("Yellow", "Black")
			a2 = stud_Kennel()
			for i in range(5): a2.add(a1)
			stud = self.get_eval_output("a2.add(a1)", locals())
			self.assertEqualShellOutput(stud, "Error: Kennel has 5 cats already!",
                                                    msg="Kennel() output mismatch.")
		except:
			raise

#SOLUTION BELOW (note students do not need if main statement)
from abc import ABC, abstractmethod

class Animal(ABC):
    all_animals = {}  # class attribute to store all animals

    def __init__(self, name):
        self.name = name

        # Use __repr__ to generate unique key
        base_key = self.__repr__()
        key = base_key
        counter = 1

        # Ensure unique key
        while key in Animal.all_animals:
            key = f"{base_key}_{counter}"
            counter += 1

        Animal.all_animals[key] = self

    @abstractmethod
    def __repr__(self):
        pass

    @staticmethod
    def listAnimals():
        if not Animal.all_animals:
            return "All animals: "
        animals = ", ".join(Animal.all_animals.keys())
        return f"All animals: {animals}"


class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed
        super().__init__(name)

    def __repr__(self):
        return f"Dog({self.name}, {self.breed})"


class Cat(Animal):
    def __init__(self, name, breed):
        self.breed = breed
        super().__init__(name)

    def __repr__(self):
        return f"Cat({self.name}, {self.breed})"


class Kennel:
    def __init__(self):
        self.animals = []
        self.cat_count = 0
        self.dog_count = 0

    def add(self, animal):
        if isinstance(animal, Cat):
            if self.cat_count >= 5:
                print("Error: Kennel has 5 cats already!")
                return
            self.cat_count += 1

        elif isinstance(animal, Dog):
            if self.dog_count >= 10:
                print("Error: Kennel has 10 dogs already!")
                return
            self.dog_count += 1

        else:
            print("Error: Only Cats and Dogs allowed!")
            return

        self.animals.append(animal)

if __name__ == "__main__":
    # Example usage:

    # This should raise an error (cannot instantiate abstract class)
    # a = Animal("Generic")

    a = Dog("Scooter", "Corgi")
    b = Cat("Meow", "Siamese")

    print(Animal.listAnimals())
    # All animals: Dog(Scooter, Corgi), Cat(Meow, Siamese)

    c = Kennel()
    c.add(b)
    c.add(b)
    c.add(b)
    c.add(a)  # Dog, doesn't count toward cat limit
    c.add(b)
    c.add(b)  # This should trigger the cat limit error
		
