import random

def format_fixed(text):
    fixed_width = 9
    return text.center(fixed_width)

def format_fixed(decorations):
    fixed_width = 9
    return decorations.center(fixed_width)

repeat = int(input("How many bunnies should your rabbit gang have? (1-10): "))
space = int(input("How close together should your rabbits hop? (1-5): "))
name = input("What is the name of your rabbit gang? ")

repeat = max(1, min(repeat, 10))
space = max(1, min(space, 5))

decorations = ['🌸', '🌻', '🍀', '🌼']

for bunny in range(repeat):
    flower = random.choice(decorations)
    flower = " " + flower + " "
    print(format_fixed(flower), end=" " * space)
print()

bunny_template = [
    r"(\ (\)",
    r"( -.-)",
    r'o_(")(")'
]

for line in range(3):
    for bunny in range(repeat):
        part = bunny_template[line]
        print(format_fixed(part), end=" " * space)
    print()

total_width = (9 + space) * repeat
print("\n" + " " * (total_width // 2 - len(name)//2) + f"---> {name}'s colourful flower meadow 🌸🐰")
