#import random
#num=random.randint(1,20)
num=18
for i in range(5):
    guess=int(input('guess a number= '))
    if guess==num:
     print('You Win')
     break
    # else:
    #  print('Your guess is wrong')
    if i==4:
     print('Game Over')
     print('The Number is',num)
