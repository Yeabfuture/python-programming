# Inheritance help us avoid reputation in our code by helping us to reuse methods and attributes form a parent class in our child class.

class Mammal:
    def walk():
        print("walk")

class Dog(Mammal):
    def bark():
        print("Barking")

class Cat(Mammal):
    def annoying():
        print("I am annoting")

booby = Dog
booby.bark()

stupid = Cat

stupid.annoying()
