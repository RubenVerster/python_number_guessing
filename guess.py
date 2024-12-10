import random

print("\033[32m🎉 Welcome to the number guessing game! 🎉\033[0m\n") 
print("You will be giving me a minimum and maximum number you want to guess between.\n")
print("I will then think of a random number between those two numbers... ")
print("You will then have to use your mind reading skills to guess the number I am thinking of!\n")

def get_number(prompt):
    while True:
        user_input = input(prompt).strip()
        try:
            return int(user_input)
        except ValueError:
            print("Please enter a valid number! ")

min_number = get_number("What is the minimum number you want to guess between? ")
max_number = get_number("What is the maximum number you want to guess between? ")
num_guesses = 0

if min_number > max_number:
    print("The minimum number is greater than the maximum number! Swapping the numbers...")
    min_number, max_number = max_number, min_number

print(f"The range is now {min_number} to {max_number}. Good luck!")

machine_number = random.randint(int(min_number), int(max_number))
guessed_correctly = False

print(f"I am thinking of a number from {str(min_number)} to {str(max_number)}, can you guess it? ")

while(not guessed_correctly):
    user_guess = get_number("\033[36mTake a guess! What's the number? \033[0m")  
    num_guesses += 1
    if(user_guess == machine_number):
        guessed_correctly = True
        print(f"\033[32m🎉 Congratulations! You nailed it with {num_guesses} guesses! 🎉\033[0m")
    elif(user_guess == "?"):
        print(f"\033[33mHint: The number I'm thinking of is {machine_number}. 😉\033[0m")  
    elif(user_guess < machine_number):
        print("\033[31mOops! Your guess is a bit too \033[1mlow\033[0m\033[31m. Try again!\033[0m")  
    elif(user_guess > machine_number):
        print("\033[31mWhoa! That guess is too \033[1mhigh\033[0m\033[31m. Give it another shot!\033[0m")  
    else:
        print("\033[35mHmm, how did you manage this? Are you a wizard? 🪄\033[0m")  
        break
