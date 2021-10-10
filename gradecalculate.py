grade = int(input())

'''
If my grade is greater than 90, I have an A
If my grade is greater than 80, I have an B
If my grade is greater than 70, I have an C
If my grade is any lower than that, I have an F
'''

if grade > 90:
    print("You have an A!")
elif grade > 80:
    print("You have a B!")
elif grade > 70:
    print("You have a C!")
else:
    print("You have an F :(")