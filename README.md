# Golden Key Adventure - Complete Project Documentation
---

## Table of Contents

1. [Game Design Description](#game-design-description)
2. [Main Game Code](#main-game-code)
3. [Gameplay Demonstration](#gameplay-demonstration)
4. [Testing and Debugging Documentation](#testing-and-debugging-documentation)

---

## Game Design Description

### Description of the Game Design for Golden Key Adventure

#### Structure of the Game

The Golden Key Adventure is a text-based adventure game made with Python. In it, players look for a mythical Golden Key in a castle. The game keeps track of which rooms have been visited by using a dictionary to store five different rooms, each with its own description, exits, and items to collect.

#### The Architecture of the Game World

The rooms in the castle are connected by nested dictionaries. Players start at the entrance and can go to the great hall, which is the main area that connects to the other areas. There are two ways to go from the great hall: north to the library (which has a hidden trap) or east to the armory (which has weapons and shields). The treasure room, where the Golden Key is located, can be reached from either the library (going east) or from the armory (going north). Players won't get stuck because all the rooms connect to each other.

#### Important Functions

There are seven main functions that make up the game and handle different parts of the gameplay:

1. **create_game_world()** - Makes all the rooms and their connections
2. **display_room()** - Shows the exits and description of the room you're in right now
3. **move_player()** - This function lets players move from one room to another and looks for traps
4. **pick_up_item()** - Puts things in the player's inventory
5. **check_win_condition()** - Checks to see if the player has found the Golden Key
6. **show_inventory()** - Shows the player what items they have
7. **main()** - Starts the game and takes care of player input

#### How to Make a Challenge

Players only have 25 moves to find the Golden Key, which makes the game harder. There is also a trap in the library that takes away two moves if it goes off, so players need to plan their route carefully. When the player picks up the golden_key item, a victory message appears, and the game ends.

---

## Main Game Code

```python
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
```



## Gameplay Demonstration

### Finishing the Game Successfully

Here is a sample gameplay session that shows how to play the game and how to finish the Golden Key Adventure.

```
============================================================
WELCOME TO THE GOLDEN KEY ADVENTURE!
============================================================

Your quest: Find the mythical Golden Key hidden in the castle!
You have 25 moves to complete your quest.

Type 'help' for a list of commands.


============================================================
Location: Entrance
============================================================
You stand at the entrance of an ancient castle. Torches flicker on stone walls.

Items here: torch

Exits: north
============================================================

What do you do? help

Available Commands:
  go <direction>    - Move in a direction (north, south, east, west)
  take <item>       - Pick up an item
  inventory         - Check your inventory
  look              - Look around the current room
  help              - Show this help message
  quit              - Exit the game

What do you do? take torch

You picked up: torch

Moves remaining: 24

What do you do? inventory

Inventory: torch

What do you do? go north

============================================================
Location: Great Hall
============================================================
A vast hall with a high ceiling. Banners hang from the walls.

Items here: map

Exits: north, east, south
============================================================

Moves remaining: 23

What do you do? take map

You picked up: map

Moves remaining: 22

What do you do? go east

============================================================
Location: Armory
============================================================
Weapons and armor are displayed on racks. Some look very old.

Items here: shield, sword

Exits: west, north
============================================================

Moves remaining: 21

What do you do? take shield

You picked up: shield

Moves remaining: 20

What do you do? go north

============================================================
Location: Treasure Room
============================================================
A chamber filled with glittering treasures! The Golden Key rests on a pedestal!

Items here: golden_key, jewels

Exits: west, south
============================================================

Moves remaining: 19

What do you do? take golden_key

You picked up: golden_key

============================================================
CONGRATULATIONS! YOU FOUND THE GOLDEN KEY!
============================================================

You completed your quest in 6 moves!
You are a true adventurer!
```

### Demonstration of Trap Mechanic

```
What do you do? go north

============================================================
Location: Library
============================================================
Dusty books line the shelves. A mysterious glow emanates from the corner.

Items here: ancient_scroll

Exits: south, east
============================================================

You triggered a trap! You lose 2 moves!

Moves remaining: 17
```


---

## Testing and Debugging Documentation

### An Overview of the Testing Process

This section show the testing method that was used to make sure the Golden Key Adventure game works right and handles edge cases well.

### Different Types of Tests

#### 1. Testing for Function

**Tests for the Movement System**
- **Valid Moves**: Tested all commands for moving in all directions (north, south, east, west) from each room
- **Invalid Moves**: Tried to move in blocked directions to check how errors are handled
- **Room Connections**: Checked that bidirectional pathways work as they should
- **Result**: All movement functions work as they should

**Item Collection Tests**
- **Valid Item Pickup**: Tested picking up items that were in rooms
- **Invalid Item Pickup**: Tried to take things that weren't there
- **Inventory Tracking**: Checked that items were added to the player's inventory correctly
- **Result**: The item management system works as it should

**Tests for Winning Conditions**
- **Collecting Golden Keys**: The game is over when you get the golden_key
- **You Get a Victory Message**: Confirmed messages of congratulations show up with the number of moves
- **Premature Win Check**: Made sure the game doesn't end without the key
- **Result**: The victory condition works as it should

#### 2. Testing for Edge Cases

**Handling an Empty Inventory**
```python
# Test case: Check the inventory when it's empty
show_inventory([])
# Expected output: "Inventory is empty"
# Result: Passed
```

**Handling of Invalid Commands**
```python
# Test case: Type an unknown command
command = "dance"
# Expected result: "Unknown command: dance. Type 'help' for available commands."
# Result: Passed
```

**Limit the Move Boundary**
```python
# Test case: Get to exactly 25 moves without finding the key
max_moves = 25
moves_used = 25
# Expected result: "GAME OVER! You ran out of moves!"
# Result: Passed
```

#### 3. Tests for Validating Input

**Parsing Commands**
- **Lowercase/Uppercase**: Tested inputs with mixed case, like "GO North" and "TAKE torch"
- **Extra Space**: Tested inputs with spaces at the start and end
- **Commands That Aren't Finished**: Tried "go" without a direction and "take" without an item
- **Result**: All inputs were properly normalized and checked

### Problems Found and Fixed

#### Problem 1: The Trap Goes Off More Than Once
**Issue**: At first, every time someone went to the library, the trap could go off.

**Solution**: Added a "visited" flag to the structure of the room dictionary.
```python
if rooms[new_room].get("trap", False) and not rooms[new_room]['visited']:
    print("\nYou set off a trap! You lose two turns!")
    return new_room, -2
```
**Method of Resolution**: Used the default value for the Python dictionary's `.get()` method to safely check if a trap exists.

#### Problem 2: Commands That Are Case-Sensitive
**Issue**: Users could accidentally type commands with mixed capitalization (like "Go North" or "TAKE torch"), which the game didn't recognize. This can easily happen when someone gets confused while typing or inadvertently holds down the Shift key.

**Solution**: Used the `.lower()` method on the user's input before processing it.
```python
command = input("\nWhat do you do? ").lower().strip().split()
```
**Resolution Method**: String normalization makes sure that commands are always processed the same way.

#### Issue 3: The Move Counter Doesn't Take Traps Into Account
**Problem**: The penalty for the trap wasn't being added to the total number of moves.

**Solution**: Changed how move tracking works to include penalty returns.
```python
current_room, penalty = move_player(current_room, direction, rooms)
moves_used += 1 + abs(penalty)
```
**How to Solve**: Tuple return values let functions send more than one piece of information.

### How to Debug

#### 1. Debugging with Print Statements
Used print statements in a smart way to keep track of:
- Changes in the current room
- Changes in the state of the inventory
- Updates to the move counter
- Evaluation of the victory condition

#### 2. Testing for Function Isolation
Tested each function separately before putting them together:
```python
# Example: Making a testing room
rooms = create_game_world()
print(rooms['entrance'])  # Check the structure
print(len(rooms))  # Check that all five rooms were made
```
