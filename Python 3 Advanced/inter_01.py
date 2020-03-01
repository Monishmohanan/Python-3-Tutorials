# Inheritance

class Pet:
	def __init__(self, name, age):
		self.name = name
		self.age = age


class Cat(Pet):
	def __init__(self, name, age):
		super().__init__(name, age) # you can run your super class methods


def main():
	thePet = Pet("Pet", 1)
	jesse = Cat("jesse", 3)

	print("Is jesse a cat? " + str(isinstance(jesse, Cat)))
	print("Is jesse a pet?" + str(isinstance(jesse, Pet)))
	print("Is thePet a Pet?" + str(isinstance(thePet, Pet)))
	print("Is thePet a Cat?" + str(isinstance(thePet, Cat)))

	print(jesse.name)


if __name__ == "__main__":
	main()