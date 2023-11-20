class PointClass:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self):
        print("Move")

    def draw(self):
        print("draw")


# constractor is a function that gets called at the time of creating the object
point = PointClass(10,20)

print(point.y)


'''

Class - Person
Name - Attribute
Talk - Method

'''

class Person:

    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


person = Person("Yeabsira")
person.talk()

bob = Person("Bob")
bob.talk()
