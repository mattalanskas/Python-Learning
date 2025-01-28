# input() = A function that prompts the user to enter data
#           Returns data in a string

name = input("What is your name?: ")
age = int(input("How old are you?: "))

age += 1
print(f"Hello {name}. Happy Birthday! You are {age} years old!")

# Rectangle Area Calculator
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width
print(f"The area of the rectangle is {area} cm^2")

# Shopping Cart Practice Program
item = input("What item would you like to buy (In singular form)?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many do you need?: "))

total = price * quantity
if quantity == 0:
    print(f"{name} is not making a purchase today")
elif quantity == 1:
    print(f"{name} is buying {quantity} {item}")
else:
    print(f"{name} wants to buy {quantity} {item}s")

print(f"The total comes out to be ${total}")

