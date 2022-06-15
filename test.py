import random

numbers = random.randint(1,100)
user_number = int(input())

while numbers != user_number:
    if numbers < user_number:
        print("Your number is less")
    elif user_number < numbers:
        print("Your number is greater")