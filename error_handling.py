'''

try:
    condition

except typeoferror:
    print(error message)
'''

try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print('Invalid input')
except ZeroDivisionError:
    print("You cant use zero")