weight = float(input("Weight: "))
measurement = input("(L)bs or (K)g: ")
measure = measurement.lower()

if measure == 'l':
    weight_in_kg = 0.453 * (weight)
    print(f'You are {weight_in_kg} kilos')

elif measure == 'k':
    weight_in_lbs = 2.2 * (weight)
    print(f'You are {weight_in_lbs} Lbs')

else:
    print("Invalid char")