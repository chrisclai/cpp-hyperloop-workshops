# This calculator divides two numbers and returns us the whole number and its remainder in a formatted string

print("Please enter the numerator: ")
numerator = int(input())
print("Please enter the denominator: ")
denominator = int(input())

wholenumber = numerator // denominator
remainder = numerator % denominator

#print(f"The whole number is {wholenumber} and our remainder is {remainder}")

print(f"The answer is {wholenumber}R{remainder}")