"""Demonstrates: the text adventure pattern — room dict + command loop"""

# ---------------------------------------------------------------
# This is a simplified version of Project 3 (Text Adventure).
# It shows the core patterns:
#   - Rooms stored as nested dicts (map/data, not logic)
#   - A command loop that parses player input
#   - Inventory and item pickup
# ---------------------------------------------------------------

# The game world is just a dictionary of room dicts.
# Each room has a description, list of exits, and list of items.
ROOMS = {
    "entrance": {
        "description": "You stand at the entrance of a mysterious cave. It smells damp.",
        "exits": {"north": "tunnel"},    # key=direction, value=room name to go to
        "items": ["torch"],
    },
    "tunnel": {
        "description": "A narrow tunnel. You can hear water dripping. There's a door to the north.",
        "exits": {"south": "entrance", "north": "treasure_room"},
        "items": ["key"],
    },
    "treasure_room": {
        "description": "A glittering room full of gold! You win!",
        "exits": {},   # no exits — this is the end
        "items": [],
        "win": True,
    },
}


def describe_room(room_id):
    """Print the current room's description, exits, and items."""
    room = ROOMS[room_id]
    print(f"\n{room['description']}")

    if room["items"]:
        print(f"Items here: {', '.join(room['items'])}")

    if room["exits"]:
        exit_list = ", ".join(room["exits"].keys())
        print(f"Exits: {exit_list}")
    else:
        print("No exits.")


def handle_command(command, current_room_id, inventory):
    """
    Parse and execute a player command.
    Returns (new_room_id, inventory, game_over).
    """
    words = command.lower().strip().split()   # split input into words
    if not words:
        return current_room_id, inventory, False

    action = words[0]   # first word is the action

    # --- go <direction> ---
    if action == "go" and len(words) > 1:
        direction = words[1]
        room = ROOMS[current_room_id]
        if direction in room["exits"]:
            new_room_id = room["exits"][direction]
            return new_room_id, inventory, False
        else:
            print("You can't go that way.")

    # --- pick up <item> ---
    elif action in ("pick", "take", "get") and len(words) > 1:
        item = words[-1]   # last word is the item name
        room_items = ROOMS[current_room_id]["items"]
        if item in room_items:
            inventory.append(item)
            room_items.remove(item)
            print(f"You pick up the {item}.")
        else:
            print(f"There's no {item} here.")

    # --- look ---
    elif action == "look":
        describe_room(current_room_id)

    # --- inventory ---
    elif action in ("inventory", "inv", "i"):
        if inventory:
            print(f"You are carrying: {', '.join(inventory)}")
        else:
            print("You're not carrying anything.")

    # --- quit ---
    elif action == "quit":
        print("You leave the cave. Better luck next time.")
        return current_room_id, inventory, True

    else:
        print("I don't understand that. Try: go north, pick up key, look, inventory, quit")

    return current_room_id, inventory, False


# ---------------------------------------------------------------
# Main game loop
# ---------------------------------------------------------------
print("=== Cave Adventure Demo ===")
print("Commands: go <direction>, pick up <item>, look, inventory, quit")

current_room = "entrance"
inventory = []
game_over = False

describe_room(current_room)

while not game_over:
    command = input("\n> ").strip()
    current_room, inventory, game_over = handle_command(command, current_room, inventory)

    # Check for win condition
    if ROOMS[current_room].get("win"):
        describe_room(current_room)
        print("\nCongratulations! You found the treasure!")
        break

    elif not game_over:
        describe_room(current_room)
