'''

a dictionary is a data structure that stores a collection of key-value pairs. It is also known as an associative array, map, or hash map in other programming languages.

Here are some key characteristics of dictionaries in Python:

Unordered: Unlike lists, which are ordered by index, dictionaries are unordered. This means that the order of elements in a dictionary is not fixed.

Mutable: You can modify the contents of a dictionary after it has been created. You can add, remove, or update key-value pairs.

Keys are Unique: Each key in a dictionary must be unique. If you try to assign a value to an existing key, it will overwrite the previous value.

Keys are Immutable: Keys must be of an immutable data type, such as strings, numbers, or tuples. This means that you cannot use mutable types like lists as keys.

Values Can Be Any Data Type: The values in a dictionary can be of any data type, including numbers, strings, lists, other dictionaries, etc.

Access by Key: You retrieve the value associated with a particular key by using the key itself. This allows for fast look-up operations.

'''

customer = {
    "name": "Yeabsira",
    "age" : 25,
    "is_verfied": True
}

customer["name"] = "jack"
customer["birthdate"] = "oct 13 2001"
print(customer.get("birthdate", "Your name"))