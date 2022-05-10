# 2022 May 09 Monty Hall Problem by Python
# Version 0.2 - changed at 2022-09-May 21:30
# source from Instructor
# Sanghyun add test!

print('Monty Hall Problem - Offline 6')
print('2022-May-09 21:30 changed')

import random


stay = 0
switch = 0
trial = 100000

for _ in range(trial):
    doors = ['car','goat','goat']
    random.shuffle(doors)
    # print(doors)
    choice = random.randrange(3)
    user = doors.pop(choice) # => doors[choice]
    # print(user)
    doors.pop(doors.index('goat'))
    # print(doors, user)
    
    if user == 'car':
        stay += 1
    else:
        switch += 1
    
print("stay: {} {}, switch: {} {}".format(stay, stay/trial, switch, switch/trial))

print('finish')
