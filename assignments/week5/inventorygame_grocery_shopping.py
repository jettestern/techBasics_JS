# --- Game State ---
inventory = []
items_in_room = [
    {"name": "Apple", "type": "fruit", "description": "A sweet red apple."},
    {"name": "Broccoli", "type": "vegetable", "description": "A healthy green vegetable."},
    {"name": "Chips", "type": "snack", "description": "Tasty but not very healthy."},
    {"name": "Salmon", "type": "protein", "description": "Fresh Atlantic salmon."},
    {"name": "Banana", "type": "fruit", "description": "High in potassium."},
    {"name": "Soda", "type": "drink", "description": "Full of sugar and bubbles."}
]  # More than 5 items available in store
MAX_INVENTORY_SIZE = 5

# --- Functions ---

def show_inventory():
    if not inventory:
        print("Your basket is empty.")
    else:
        print("Your basket contains:")
        for item in inventory:
            print(f"- {item['name']} ({item['type']})")

def show_room_items():
    if not items_in_room:
        print("The supermarket shelf is empty.")
    else:
        print("Available in the supermarket:")
        for item in items_in_room:
            print(f"- {item['name']} ({item['type']})")

def pick_up(item_name):
    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("Your basket is full. Remove something first.")
        return

    for item in items_in_room:
        if item["name"].lower() == item_name.lower():
            inventory.append(item)
            items_in_room.remove(item)
            print(f"You added {item['name']} to your basket.")
            return

    print(f"{item_name} is not available on the shelf.")

def drop(item_name):
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            inventory.remove(item)
            items_in_room.append(item)
            print(f"You removed {item['name']} from your basket.")
            return

    print(f"{item_name} is not in your basket.")

def use(item_name):
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            if item["type"] in ["fruit", "vegetable", "protein"]:
                print(f"You eat the {item['name']}. It's healthy and delicious!")
                inventory.remove(item)
            elif item["type"] == "snack":
                print(f"You eat the {item['name']}. Tasty but maybe not the best choice.")
                inventory.remove(item)
            elif item["type"] == "drink":
                print(f"You drink the {item['name']}. Refreshing!")
                inventory.remove(item)
            else:
                print(f"You used the {item['name']}.")
                inventory.remove(item)
            return

    print(f"{item_name} is not in your basket.")

def examine(item_name):
    for item in inventory + items_in_room:
        if item["name"].lower() == item_name.lower():
            print(f"{item['name']}: {item['description']}")
            return
    print(f"{item_name} is not found to examine.")

# --- Game Loop ---

def game_loop():
    print("🛒 Welcome to the Supermarket!")
    print("Type 'help' for a list of commands.")

    while True:
        command = input("\n> ").strip().lower()
        if command == "help":
            print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], quit")
        elif command == "inventory":
            show_inventory()
        elif command == "look":
            show_room_items()
        elif command.startswith("pickup "):
            item_name = command[7:]
            pick_up(item_name)
        elif command.startswith("drop "):
            item_name = command[5:]
            drop(item_name)
        elif command.startswith("use "):
            item_name = command[4:]
            use(item_name)
        elif command.startswith("examine "):
            item_name = command[8:]
            examine(item_name)
        elif command == "quit":
            print("Thanks for shopping! Goodbye.")
            break
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    game_loop()
