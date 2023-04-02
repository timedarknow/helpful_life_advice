import random
from time import sleep
text1 = input("pick a number between one and 10 choose wisely:")
num1 = random.randint(1,10)
print("the number was "+str(num1))
if text1 == num1:
    print("you win. your system lives another day.")
    sleep(10)
else:
    print("oh well you lost")
    print("deleting sys32...")
    sleep(10)
    