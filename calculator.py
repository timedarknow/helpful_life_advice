from time import sleep

print('options 1, 2, 3, 4')

userchoice = input('enter choice 1 add 2 sub 3 multiply 4 divide:')



while (userchoice != '1') and (userchoice != '2') and (userchoice != '3') or (userchoice != '4'):
    if userchoice == '1':
      add1 = int(input('enter first num: '))
      add2 = int(input('enter second num: '))
      print(add1 + add2)
      userchoice = '5'
    
    
    elif userchoice == '2':
      sub1 = int(input('second num to sub: '))
      sub2 = int(input('second num to sub: '))
      print(sub1 - sub2)
      userchoice = '5'
    
    elif userchoice == '3':
      mul1 = int(input('second num to multiply: '))
      mul2 = int(input('second num to multiply: '))
      print(mul1 * mul2)
      userchoice = '5'

    elif userchoice == '4':
      div1 = int(input('second num to divide: '))
      div2 = int(input('second num to divide: '))
      print(div1 / div2)
      userchoice = '5'

    elif userchoice >= "6":
       print('not a choice')
       
       sleep(30)

       break

    elif userchoice == '5':
      sleep(120)
    
      break


    


