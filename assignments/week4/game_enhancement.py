import time

#  Define Constants
MIN_BUDGET = 10
MAX_BUDGET = 1000
SAVINGS = 100

# User number input with verification
def get_float(prompt, min_value=None, max_value=None): # None means: no check for min/max
    while True:
        try:
            value = float(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Please enter a number between {min_value} and {max_value}.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")

# Handles savings decision
def update_savings(savings, rest):
    attempts = 0
    while True:
        choice = input("Do you want to save the remaining amount? (yes/no) ").lower()
        if choice == "yes":
            savings += rest
            print(f"Great! Your total savings are now {savings:.2f}.") # Returns savings with two decimal digits
            return savings
        elif choice == "no":
            print("Alright, maybe treat yourself! 😉")
            print(f"You have {rest:.2f} left – you can always save it next time!")
            return savings
        else:
            attempts += 1
            if attempts >= 3:
                print("Okay... I think you need your time. The budget gods are confused 😵💸 See you next week!")
                return savings
            print("Hmm... please type 'yes' or 'no'.")

# Budget evaluation with different levels depending on savings
def evaluate_savings(savings):
    print("\n--- Budget Boss Evaluation ---")
    if savings >= SAVINGS:
        print("🎉 Budget Boss Level: Saver Extraordinaire! You've got this!")
    elif savings > 0:
        print("🧮 Budget Boss Level: Learning Planner – you're on the right track!")
    elif savings == 0:
        print("😅 Budget Boss Level: Cost-Coverer – but you're not out yet.")
    else:
        print("💸 Budget Boss Level: Chaotic-Spender – better luck next time!")

# Define main function
def main():
    print("Welcome to Budget Boss 💸😎")
    name = input("What's your name? ")
    time.sleep(1)
    print(f"Hi {name}!")

    budget = get_float("What is your budget for the week? ", MIN_BUDGET, MAX_BUDGET)
    savings = get_float("What are your savings? ")

    if savings >= 0:
        print("Nice, you're on your way to becoming a Budget Boss!")
    else:
        print("Oh oh, you need to practice your money management a bit more...")

    print(f"So, you have {budget:.2f} for the week.")

    food = get_float("How much do you want to spend on food? ")
    remaining_after_food = budget - food

    if food >= 70:
        print(f"You only have {remaining_after_food:.2f} left for savings and activities.")
    else:
        print(f"Great! You still have {remaining_after_food:.2f} left. Keep going!")

    activities = get_float("How much do you want to spend on activities? ")
    rest = budget - food - activities
    print(f"After food and activities, you have {rest:.2f} left.")

    savings = update_savings(savings, rest)
    evaluate_savings(savings)

# Only run main function if this file is executed directly
if __name__ == "__main__":
    main()
