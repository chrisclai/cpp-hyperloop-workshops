import time

'''
While loop
counter = 0

while True:
    if counter == 30:
        print("Ending code!")
        break

    counter += 1
    print(f"Hello {counter}")
    time.sleep(0.2)
'''

listofstuff = [0,1,2,3,4,5]

for x in range(0, len(listofstuff)):
    print(f"Hello World! {listofstuff[x]}")
    time.sleep(0.05)

