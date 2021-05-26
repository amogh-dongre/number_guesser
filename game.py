# !/usr/bin/env python3
# Hiya this is a program to guess and win
import random
import math

ll=int(input("Enter the lower limit "))

ul=int(input("Enter the upper limit "))

random=random.randint(ll,ul)
print(f'\n you have  got {round(math.log(ul - ll + 1 , 2))} number of chances to guess the correct number!')

count=0
while count<math.log(ul-ll+1,2):
   count+=1
   guess=int(input("Enter your guess! "))
   if random == guess:
          print(f"Congratulations you have guessed the correct answer in {count} guesses")
          break
   elif random<guess:
      print(f"youre guess is too low guess again :) ")
   elif random>guess:
      print(f"youre guess is too high guess again :) ")

if count>=math.log(ul-ll+1,2):
    print(f"The number is {random} better luck next time")
