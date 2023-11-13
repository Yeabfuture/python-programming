# Write a program that find the largest number in a list

numbers = [2,30,65,3,7]
largest_number = numbers[0]

for num in numbers:
    if num > largest_number:
        largest_number = num

print(f'the largest number in the list is {largest_number}')
    