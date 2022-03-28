#Write a small program to ask for a name and age
#When both values have been entered, check if the person is the right age to go on an 18-30
#holiday(must be over 18 and under 31)
#If they are, welcome them to the holiday, otherwise print a (polite) message refusing
#them entry

name = input("Please enter your name: ")
age = input("Please enter your age: ")


if 18 <= int(age) < 31:
	print("Welcome {}! Enjoy your holiday!".format(name))
else:
	print("Sorry {}! You're not allowed to enjoy the holiday".format(name))

print( "-" * 80)

if int(age) in range (18, 31):
	print("Welcome {}! Enjoy your holiday!".format(name))
else:
	print("Sorry {}! You're not allowed to enjoy the holiday".format(name))