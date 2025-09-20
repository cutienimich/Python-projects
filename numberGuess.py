import random

i = random.randint(1,5)

while True:
    number = int(input('Gess the number: '))
    if number == i:
        print('Congrats You Got it!')
        break #if nakakuha na sya ng tama, magbebreak na para di paulit -ulit
    elif number > 5:
        print('Number above 5 is not allowed. Try Again!')
    else:
        print('You got it wrong! Try again')