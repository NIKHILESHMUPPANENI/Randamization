import random
number = random.randint(1,10)
for i in range(0,3):
    user = int(input("guess the number"))
    if user == number :
       print("<<HURRAY!!!>>")
       print(f" you guessed the number right {number}")
    break
if user != number :
 print(f" you guessed the number worng {number}")