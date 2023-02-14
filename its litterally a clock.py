from datetime import datetime

from time import sleep

print('get the exact time down to the milisecond')

userchoice = input("1 to continue, 2 to close:")

while (userchoice != '1') | (userchoice != '2'):
    if (userchoice == "2"):
      print('closing in 15 seconds...')
      sleep(15)
      break

    if (userchoice == "1"):
      datevar = (str(datetime.now()))
      print("it is:" + datevar)
      sleep(15)
      break

    if (input >= '3'):
       print('not an option')
       sleep(10)
       break

