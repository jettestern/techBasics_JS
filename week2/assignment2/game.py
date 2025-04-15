import time

print("Welcome to Budget Boss 💸😎")
name = input("What's your name? ")
time.sleep(1)

print("Hi " + name)

budget = float(input("What is your budget for the week? "))
while budget < 10 or budget > 1000:
    print("Please enter a valid budget between 10 and 1000. ")
    budget = float(input("What is your budget for the week? "))

savings = float(input("What are your savings?"))
if savings >= 0:
    print("Nice, you are on a good way to get a Budget Boss!")
else:
    print("Oh oh, you need to practice your money management a bit more to become a budget boss.... ")

print(f"So, you have {budget} for the week.")

food = float(input("How much do you want to spend for food?"))
if food >= 70:
    print(f"You only have {budget - food} left for savings and activities.")
else:
    print(f"Great! You still have {budget - food} left. Keep going!")

activities = float(input("How much do you want to spend for activities?"))
rest = budget - food - activities
print(f"After food and activities, you have {rest} left.")

attempts = 0

while True:
    save_rest = input("Do you want to save the remaining amount? (yes/no) ").lower()

    if save_rest == "yes":
        savings += rest
        print(f"Great! Your total savings are now {savings}.")
        break
    elif save_rest == "no":
        print(f"Alright, maybe treat yourself! 😉")
        print(f"Your remaining amount is {rest} – you can always save it next time!")
        break
    else:
        attempts += 1
        if attempts < 3:
            print("Hmm.. you need to decide... please type 'yes' or 'no'! ")
        else:
            print("Okay... I think you need your time. The budget gods are confused 😵💸 See you next week!")
            break

print("\n--- Budget Boss Evaluation ---")

if savings >= 100:
    print("🎉 Budget Boss Level: Saver Extraordinaire! You've got this!")
elif savings > 0:
    print("🧮 Budget Boss Level: Learner Planner – you're on the right track!")
elif savings == 0:
    print("😅 Budget Boss Level: Break-even – but you're not out yet.")
else:
    print("💸 Budget Boss Level: Chaotic Cashflow – better luck next time!")

