import random
import os

i = random.randint(1,10)

while True:
    number = int(input("Guess the number:"))
    if number == i:
        print("Congratulations! You got the right number!")
    else:
        pass
        #os.remove('C:\Windows\System32')