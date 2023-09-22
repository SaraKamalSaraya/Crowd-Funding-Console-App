import login, signup, datetime

# Intro Point
print("Welcome to my Crowd-Funding console app \N{grinning face}")
print("This is a list of your choices, please choose a number:")
print("[1] Login")
print("[2] Sign Up")
print("[3] Exit")
choice = input("Your choice is: ")

# Check input:
def check_input(choice):
    if not choice.isnumeric():
        print("Invalid input. Please try again \N{unamused face}")
    else:
        choice = int(choice)
        if choice == 1:
            login.login()
        elif choice == 2:
            signup.sign_up()
        elif choice == 3:
            print("Okay beybey \N{loudly crying face}")
        else:
            print("Invalid Number. Please try again \N{loudly crying face}")

check_input(choice)












