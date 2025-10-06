"""
Golden Key Adventure Game
A text-based adventure game implementation using Python dictionaries and functions.
"""

def create_game_world():
    """
    Creates the game world structure as a dictionary.
    Each room connects to adjacent rooms and contains descriptions and items.
    """
    rooms = {
        'entrance': {
            'description': 'You stand at the entrance of an ancient castle. Torches flicker on stone walls.',
            'north': 'great_hall',
            'items': ['torch'],
            'visited': False
        },
        'great_hall': {
            'description': 'A vast hall with a high ceiling. Banners hang from the walls.',
            'north': 'library',
            'east': 'armory',
            'south': 'entrance',
            'items': ['map'],
            'visited': False
        },
        'library': {
            'description': 'Dusty books line the shelves. A mysterious glow emanates from the corner.',
            'south': 'great_hall',
            'east': 'treasure_room',
            'items': ['ancient_scroll'],
            'visited': False,
            'trap': True  # Hidden trap that costs moves
        },
        'armory': {
            'description': 'Weapons and armor are displayed on racks. Some look very old.',
            'west': 'great_hall',
            'north': 'treasure_room',
            'items': ['shield', 'sword'],
            'visited': False
        },
        'treasure_room': {
            'description': 'A chamber filled with glittering treasures! The Golden Key rests on a pedestal!',
            'west': 'library',
            'south': 'armory',
            'items': ['golden_key', 'jewels'],
            'visited': False
        }
    }
    return rooms

def display_room(room_name, rooms):
    """
    Display the current room description and available exits.
    
    Args:
        room_name (str): The key for the current room in the rooms dictionary
        rooms (dict): The complete game world dictionary structure
    
    The function formats and prints room information including description,
    items present, and available navigation directions.
    """
    room = rooms[room_name]
    
    print(f"\n{'='*60}")
    print(f"Location: {room_name.replace('_', ' ').title()}")
    print(f"{'='*60}")
    print(room['description'])
    
    # Show items in room
    if room['items']:
        print(f"\nItems here: {', '.join(room['items'])}")
    
    # Show available exits
    exits = [direction for direction in ['north', 'south', 'east', 'west'] if direction in room]
    print(f"\nExits: {', '.join(exits)}")
    print(f"{'='*60}")

def move_player(current_room, direction, rooms):
    """
    Move the player to a new room if the direction is valid.
    
    Args:
        current_room (str): Current room key
        direction (str): Direction to move (north/south/east/west)
        rooms (dict): Game world structure
    
    Returns:
        tuple: (new_room_name, move_penalty) where penalty is negative for traps
    
    Uses dictionary lookups to verify valid moves and implements trap detection
    logic as part of the game challenge mechanics.
    """
    if direction in rooms[current_room]:
        new_room = rooms[current_room][direction]
        
        # Check for trap BEFORE marking room as visited
        trap_penalty = 0
        if rooms[new_room].get('trap', False) and not rooms[new_room]['visited']:
            print("\nYou triggered a trap! You lose 2 moves!")
            trap_penalty = -2
        
        # Mark room as visited after checking for trap
        rooms[new_room]['visited'] = True
        
        return new_room, trap_penalty
    else:
        print("\nYou can't go that way!")
        return current_room, 0

def show_inventory(inventory):
    """Display the player's inventory."""
    if inventory:
        print(f"\nInventory: {', '.join(inventory)}")
    else:
        print("\nInventory is empty")

def pick_up_item(room_name, item, rooms, inventory):
    """Pick up an item from the current room."""
    if item in rooms[room_name]['items']:
        rooms[room_name]['items'].remove(item)
        inventory.append(item)
        print(f"\nYou picked up: {item}")
        return True
    else:
        print(f"\nThere is no {item} here!")
        return False

def check_win_condition(inventory):
    """Check if the player has won by obtaining the Golden Key."""
    return 'golden_key' in inventory

def show_help():
    """Display available commands."""
    print("\nAvailable Commands:")
    print("  go <direction>    - Move in a direction (north, south, east, west)")
    print("  take <item>       - Pick up an item")
    print("  inventory         - Check your inventory")
    print("  look              - Look around the current room")
    print("  help              - Show this help message")
    print("  quit              - Exit the game")

def main():
    """Main game loop."""
    # Initialize game state
    rooms = create_game_world()
    inventory = []
    current_room = 'entrance'
    max_moves = 25
    moves_used = 0
    
    # Mark starting room as visited
    rooms[current_room]['visited'] = True
    
    # Welcome message
    print("\n" + "="*60)
    print("WELCOME TO THE GOLDEN KEY ADVENTURE!")
    print("="*60)
    print("\nYour quest: Find the mythical Golden Key hidden in the castle!")
    print(f"You have {max_moves} moves to complete your quest.")
    print("\nType 'help' for a list of commands.\n")
    
    # Display starting room
    display_room(current_room, rooms)
    
    # Main game loop
    while moves_used < max_moves:
        # Get player input
        command = input("\nWhat do you do? ").lower().strip().split()
        
        if not command:
            continue
        
        action = command[0]
        
        # Process commands
        if action == 'quit':
            print("\nThanks for playing! Goodbye!")
            break
        
        elif action == 'help':
            show_help()
            continue
        
        elif action == 'look':
            display_room(current_room, rooms)
            continue
        
        elif action == 'inventory':
            show_inventory(inventory)
            continue
        
        elif action == 'go':
            if len(command) < 2:
                print("\nGo where? (north, south, east, west)")
                continue
            
            direction = command[1]
            current_room, penalty = move_player(current_room, direction, rooms)
            moves_used += 1 + abs(penalty)
            display_room(current_room, rooms)
            
            # Check if player found the key
            if check_win_condition(inventory):
                print("\n" + "="*60)
                print("CONGRATULATIONS! YOU FOUND THE GOLDEN KEY!")
                print("="*60)
                print(f"\nYou completed your quest in {moves_used} moves!")
                print("You are a true adventurer!\n")
                break
        
        elif action == 'take':
            if len(command) < 2:
                print("\nTake what?")
                continue
            
            item = command[1]
            pick_up_item(current_room, item, rooms, inventory)
            moves_used += 1
            
            # Check if player just picked up the key
            if check_win_condition(inventory):
                print("\n" + "="*60)
                print("CONGRATULATIONS! YOU FOUND THE GOLDEN KEY!")
                print("="*60)
                print(f"\nYou completed your quest in {moves_used} moves!")
                print("You are a true adventurer!\n")
                break
        
        else:
            print(f"\nUnknown command: {action}. Type 'help' for available commands.")
            continue
        
        # Display remaining moves
        remaining = max_moves - moves_used
        if remaining <= 5:
            print(f"\nWarning: Only {remaining} moves remaining!")
        else:
            print(f"\nMoves remaining: {remaining}")
    
    # Check if player ran out of moves
    if moves_used >= max_moves and not check_win_condition(inventory):
        print("\n" + "="*60)
        print("GAME OVER! You ran out of moves!")
        print("="*60)
        print("\nBetter luck next time, adventurer!\n")

# Run the game
if __name__ == "__main__":
    main()
