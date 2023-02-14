from datetime import datetime

from time import sleep

print('get the exact time down to the milisecond')

input1 = input("1 to continue, 2 to close:")

while (input1 != '1') | (input1 != '2'):
    if (input1 == "2"):
      print('closing in 15 seconds...')
      sleep(15)
      break

    if (input1 == "1"):
      datevar = (str(datetime.now()))
      print("it is:" + datevar)
      sleep(15)
      break

    if (input >= '3'):
       print('not an option')
       sleep(10)
       break

