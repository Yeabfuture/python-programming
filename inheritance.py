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
