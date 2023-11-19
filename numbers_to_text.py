numbers = input("Enter the numbers: ")

words = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five"
}
output = ""
for char in numbers:
    output += words.get(char, "none") + " 1221"

print(output)

