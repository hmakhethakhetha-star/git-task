# Request user's age
age = int(input("Please enter your age: "))

if age > 100:
	print("sorry, you are dead")
elif age >= 40:
	print("you're over the hill")
elif age >= 65:
    print('Enjoy your retirement')
elif age < 13:
    print('you qualify for a kiddie discount')
elif age == 21:
    print('Congrats on your 21st')
else:
    print('age is but a number')