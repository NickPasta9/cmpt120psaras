# dice.py

from graphics import*
import random

def probability_five_of_a_kind(num_trials):
   sums = 0
   
   for _ in range(num_trials):
       roll_1 = random.randrange(1,6, 1)
       roll_2 = random.randrange(1,6, 1)
       roll_3 = random.randrange(1,6, 1)
       roll_4 = random.randrange(1,6, 1)
       roll_5 = random.randrange(1,6, 1)
       collection = roll_1 + roll_2 + roll_3 + roll_4 + roll_5
       if collection == 5:
           sums += 1
   prob = round(sums/7776, 8)
   print(f"The probability_five_of_a_kind is {prob}")

probability_five_of_a_kind(100)

probability_five_of_a_kind(10000)

probability_five_of_a_kind(1000000)
