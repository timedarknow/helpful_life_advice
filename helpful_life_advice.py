
from time import sleep

userchoice = input("1 or 2:")
while (userchoice == '1') or (userchoice == '2'):
    if userchoice == '1':
        print('die')
        sleep(20)
        break
    
    if userchoice == '2':
        print("why are you still here?")
        sleep(3)
        print("go home.")
        sleep (5)
        print('seriously dude, you have a life unlike me.')
        print ("go live it")
        sleep(3)
        print('this is why everyone says you are a failure.')
        print('you are talking to a computer program.')
        print ('why?')
        sleep(3)
        print("we're done here.")
        sleep(6)
        break