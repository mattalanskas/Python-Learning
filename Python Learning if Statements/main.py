# If statements - if/else statements to decide what to do

age = int(input("Enter your age: "))

if 18 <= age < 100:
    print("You are now signed up")
elif age < 0:
    print("You have not been born yet...")
elif age >= 100:
    print("You are too old to sign up!")
else:
    print("You are not eligible")

for_sale = True

if for_sale:
    print("This item is for sale.")
else:
    print("This item is not for sale")
