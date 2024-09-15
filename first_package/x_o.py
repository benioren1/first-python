import random

options = ["a", "n", "m"]
computer = 0
user = 0
while user < 3 and computer < 3:
    user_input = input("Enter: ")
    computer_choice = random.choice(options)
    if user_input == "a" and computer_choice == "n":
        user += 1
    elif user_input == "a" and computer_choice == "m":
        computer += 1
    elif user_input == "m" and computer_choice == "a":
        computer += 1
    elif user_input == "m" and computer_choice == "n":
        user += 1
    elif user_input == "n" and computer_choice == "m":
        user += 1
    elif user_input == "n" and computer_choice == "a":
        computer += 1


