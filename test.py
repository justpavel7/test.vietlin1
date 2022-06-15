import random

numbers = random.randint(1,100)
user_number = int(input("Enter the number: "))
count = 0

while numbers != user_number:
    count += 1
    if numbers < user_number:
        print("Your number is greater")
    elif user_number < numbers:
        print("Your number is less")
    user_number = int(input("Enter tne number: "))
print(f"Your try: {count}")