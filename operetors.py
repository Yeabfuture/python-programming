# Operator Presendence
# paranteses > Expon > mul > division > add > sub

# Logical operators

has_high_income = True
has_good_credit = True

if has_high_income or has_good_credit:
    print("You are eliggible to loan")

#AND - has to have both true
#OR - Atleast one true 
#NOT - change one bool value to another


#Comparsion Operator

 temp = int(input("What is the temp "))

if temp > 30:
    print("Its a hot day")
elif temp < 10:
    print("Its a cold day")
else:
    print("Its a lovely day") 


# Project about name validator

name = input("What is your name?")
leng = len(name)

if leng < 3:
    print("Name must be atleast 3 characters")
elif leng >50:
    print("Name can be max of 50 characters")
else:
    print("Name looks good!")

