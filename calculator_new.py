from time import sleep

print('options 1, 2, 3, 4')

userchoice = input('enter choice 1 add 2 sub 3 multiply 4 divide:')

endfunc = 0

while (userchoice != '1') and (userchoice != '2') and (userchoice != '3') or (userchoice != '4'):
    if userchoice == '1':
      add1 = int(input('enter first num to add: '))
      add2 = int(input('enter second num to add: '))
      print(add1 + add2)
      endfunc = 1
    
    
    elif userchoice == '2':
      sub1 = int(input('first num to sub: '))
      sub2 = int(input('second num to sub: '))
      print(sub1 - sub2)
      endfunc = 1
    
    elif userchoice == '3':
      mul1 = int(input('first num to multiply: '))
      mul2 = int(input('second num to multiply: '))
      print(mul1 * mul2)
      endfunc = 1

    elif userchoice == '4':
      div1 = int(input('first num to divide: '))
      div2 = int(input('second num to divide: '))
      print(div1 / div2)
      endfunc = 1

    elif userchoice >= '5':
       print('not a choice')
       
       sleep(30)

       break

    elif endfunc == 1:
      sleep(30)
    
      break


    


