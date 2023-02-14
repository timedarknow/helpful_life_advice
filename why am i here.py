from time import sleep 
import os
print('hit 1 or 2')
userchoice = input(':')

while (userchoice != '1') | (userchoice != '2'):
    if userchoice == '1':
        print('you hit the number one, do you feel acomplished yet?')
        sleep(10)
        break
    
    elif userchoice == '2':
        print('you hit the number 2, congratulations.')
        sleep(10)
        break

    elif userchoice >= '3':
        print('great job dumbass, you cant read apperently.')
        sleep(10)
        break