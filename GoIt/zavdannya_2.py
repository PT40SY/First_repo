import random

def get_numbers_ticket(min, max, quantity):
   if min < 1 or max > 1000 or quantity < min or quantity > max:
      return []
   
   numbers_set = set()
   while len(numbers_set) < quantity:
      number = random.randint(min, max)
      numbers_set.add(number)

   numbers_list = sorted(numbers_set)
   return numbers_list

print(get_numbers_ticket(1, 49, 6))
