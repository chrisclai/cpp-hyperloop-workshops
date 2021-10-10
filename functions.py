# Reoccuring amazon order: I want to buy 3 arudino nanos every 4 months

from shop import order

def Main():
    print("Enter the number of arduinos you would like to purchase: ")
    number = int(input())
    print(f"Your total order cost is: ${round(order(number), 2)}") # Number is an integer!!

# This will run on startup!
if __name__ == '__main__':
    Main()