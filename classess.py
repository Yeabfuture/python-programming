# we use classess to define new types of data in python
# Simple data types {Numbers, strings, bool} and Complex data types { Lists and dictioneries}

class PointClass:
    def move(self):
        print("Move")

    def draw(self):
        print("draw")


# Object is an instance of a class(the blue print of creating objects)

point1 = PointClass() # This is the object we created for our class

point1.draw()

# These objects can also have attributes belonging to a particular object

point1.x = 10
point1.y = 20

print(point1.x)

point2 = PointClass()