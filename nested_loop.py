# nested loop is a loop inside of a loop
x = [5,2,5,2,2]
for n in x:
    print( n *'x')


for n in x:
    output = ''
    for count in range(n):
        output += 'x'
    print(output)