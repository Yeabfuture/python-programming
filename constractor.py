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

    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, my name is {self.name}")


name1 = Person("Yeabsira")

print(name1.name)
name1.talk()


bob = Person("Bob Smit")

print(bob.name)
bob.talk()