message = input("> ")
splitted_words = message.split(' ')

emojis = {
    ":)": "😃",   
    ":(": "😞"   
}

output = ""
for word in splitted_words:
    output += emojis.get(word, word) + " "

print(output)
