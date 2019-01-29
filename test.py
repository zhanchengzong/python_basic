if 5 > 3 and 2 < 6:
    print(True)

for i in set([3, 2, 1]):
    print(i)

x = [1, 2, 3]
y = iter(x)
for i in y:
    print(i)

import numpy as np

isinstance(999, int)
isinstance(999, float)





def enter_number():
    while True:
        num = input('Please enter a integer number between 0 and 9.  ')
        try:
            float(num)
            try:
                num = int(num)
                if 0 <= num <= 9:
                    print('Well done!')
                    return num
                else:
                    print('The number must between 0 and 9.')
            except ValueError:
                print('The number must between an integer.')
        except ValueError:
            print('It\'s not a integer number! Please enter your number again.')


import random

rewards = ['first', 'second', 'third']

while True:
    rand_ls = random.sample(range(0, 10), 3)
    num = enter_number()
    for i in range(4):
        try:
            if int(num) == rand_ls[i]:
                answer = input('The random list is {}. Congratulations! You win the {} prize!\nDo you want to start a new game? Please enter 1 if you want or enter 2 if you don\'t.'.format(rand_ls, rewards[i]))
                break
        except:
            answer = input('The random list is {}, but your guess is {}, no prize for you.\nDo you want to start a new game? Please enter 1 if you want or enter 2 if you don\'t.'.format(rand_ls, num))

    try:
        answer = int(answer)
        if answer == 1:
            continue
        elif answer == 2:
            break
    except:
        answer = input('Do you want to start a new game? Please enter 1 if you want or enter 2 if you don\'t.')

for i, n in enumerate(rand_ls):
    print(type(n))

    3 == rand_ls[2]