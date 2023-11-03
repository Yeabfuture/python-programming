# We can count the length of a string by using a function called Len

text = "This is a text I wanted to count on"

print(len(text))

# methods are functions that are associated to an object
# methods don't actially change the original value and it actually create a new one
# find method is used to indicate the first occurance of a cracter in a string and here is the syntax.
#find method is case sensetive

print(text.find('I'))
print(text.find('i'))

# replace is a method thats is used to replace a char or a sequence of characters in a string
# this is also case sensetive
print(text.replace('text', 'font'))

# We also have a method that can check the existance of a char or a value in a string and respond a bool
# this is also a case sensetive
course = 'I am learning python as a new language '

print('python' in course)