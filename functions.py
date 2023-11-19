def greet_user(name):
    print("hello", name)



greet_user(name = "Yeab")


# positional and key word arguments(prefixing the name with valies when passing the arguments)
# key word arguments always come after the positional arguments

# Return statement

def square(number):
    return number * number

print(square(3))

# the default value of a function is none


# reusable function

def emoji_convertor(message):
    words = message.split(" ")
    emojis = {
    ":)": "😃",   
    ":(": "😞"   
    }

    output = ""
    for word in words:
        output += emojis.get(word,word) + " "
    
    return output

message = input("> ")
print(emoji_convertor(message))
    

