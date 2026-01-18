# -------------------------------------------------
# File Name: Baez_Module_07_Lab.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming 
# Professor: Mauricio Quiroga
# Date: Module 07 Lab
# Description: Programming exercises including:
#              1. Deck Cards Program
#              2. Names and Birthdays Program
# -------------------------------------------------

import random

# =============================================================================
# EXERCISE 1: Deck Cards Program
# =============================================================================
# Description: Write a program that uses a dictionary to simulate a standard 
#              deck of poker cards, where the cards are assigned numeric values 
#              similar to those used in Blackjack. The cards are given the 
#              following numeric values:
#              • Numeric cards are assigned the value they have printed on them. 
#                For example, the value of the 2 of spades is 2, and the value 
#                of the 5 of diamonds is 5.
#              • Jacks, queens, and kings are valued at 10.
#              • Aces are valued at either 1 or 11, depending on the player's 
#                choice. In the program, assign the value 1 to all aces.
#              The key-value pairs use the name of the card as the key, and the 
#              card's numeric value as the value. For example, the key-value 
#              pair for the Queen of Hearts is 'Queen of Hearts': 10, and the 
#              key-value pair for the 8 diamonds is '8 of Diamonds': 8. 
#              The program prompts the user for the number of cards to deal 
#              with, and it randomly deals a hand of that many cards from the 
#              deck. The names of the cards are displayed, as well as the total 
#              numeric value of the hand. The program is divided into three 
#              functions: main, create_deck, and deal_cards.
# =============================================================================

def create_deck():
    """
    Create a dictionary representing a standard deck of poker cards.
    
    Returns:
        dict: Dictionary with card names as keys and numeric values as values
    """
    # Define suits and ranks
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
             'Jack', 'Queen', 'King']
    
    # Initialize empty deck
    deck = {}
    
    # Loop (for): Iterate through each suit
    for suit in suits:
        # Loop (for): Iterate through each rank
        for rank in ranks:
            # Create card name
            card_name = f"{rank} of {suit}"
            
            # Assign numeric value based on rank
            if rank == 'Ace':
                value = 1  # Aces are valued at 1
            elif rank in ['Jack', 'Queen', 'King']:
                value = 10  # Face cards are valued at 10
            else:
                value = int(rank)  # Numeric cards have their printed value
            
            # Add card to deck dictionary
            deck[card_name] = value
    
    return deck


def deal_cards(deck, num_cards):
    """
    Deal a specified number of cards randomly from the deck.
    
    Args:
        deck (dict): Dictionary representing the deck of cards
        num_cards (int): Number of cards to deal
        
    Returns:
        tuple: (list of card names, total numeric value of the hand)
    """
    # Convert deck dictionary keys to a list for random selection
    card_list = list(deck.keys())
    
    # Randomly select cards (without replacement)
    hand = random.sample(card_list, min(num_cards, len(card_list)))
    
    # Calculate total value of the hand
    total_value = sum(deck[card] for card in hand)
    
    return hand, total_value


def main():
    """
    Main function to run the deck cards program.
    """
    print("=" * 60)
    print("EXERCISE 1: Deck Cards Program")
    print("=" * 60)
    
    # Create the deck
    deck = create_deck()
    print(f"Deck created with {len(deck)} cards.")
    
    # Get number of cards to deal
    # Try-except block: Handles exceptions that may occur during input conversion
    try:
        num_cards = int(input("\nEnter the number of cards to deal: "))
        
        # Validate input
        if num_cards < 1:
            print("Error: Number of cards must be at least 1.")
        elif num_cards > len(deck):
            print(f"Error: Cannot deal more than {len(deck)} cards.")
        else:
            # Deal cards
            hand, total_value = deal_cards(deck, num_cards)
            
            # Display results
            print("\n" + "=" * 60)
            print("DEALT HAND")
            print("=" * 60)
            print("Cards dealt:")
            for i, card in enumerate(hand, 1):
                print(f"  {i}. {card} (value: {deck[card]})")
            
            print(f"\nTotal numeric value of the hand: {total_value}")
            
    except ValueError:
        # Handle invalid numeric input (e.g., non-numeric characters)
        print("Error: Please enter a valid integer.")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Error: {e}")


# Run Exercise 1
main()

print()

# =============================================================================
# EXERCISE 2: Names and Birthdays Program
# =============================================================================
# Description: Write a program that keeps your friends' names and birthdays in 
#              a dictionary. Each entry in the dictionary uses a friend's name 
#              as the key, and that friend's birthday as the value. You can 
#              use the program to look up your friends' birthdays by entering 
#              their names. The program displays a menu that allows the user 
#              to make one of the following choices:
#              1. Look up a birthday
#              2. Add a new birthday
#              3. Change a birthday
#              4. Delete a birthday
#              5. Quit the program
#              The program initially starts with an empty dictionary, so you 
#              have to choose item 2 from the menu to add a new entry. Once 
#              you have added a few entries, you can choose item 1 to look up 
#              a specific person's birthday, item 3 to change an existing 
#              birthday in the dictionary, item 4 to delete a birthday from the 
#              dictionary, or item 5 to quit the program.
#              The program is divided into six functions: main, get_menu_choice, 
#              look_up, add, change, and delete.
# =============================================================================

# Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def get_menu_choice():
    """
    Display the menu and get the user's choice.
    
    Returns:
        int: User's menu choice
    """
    print("\n" + "=" * 60)
    print("BIRTHDAY MENU")
    print("=" * 60)
    print(f"{LOOK_UP}. Look up a birthday")
    print(f"{ADD}. Add a new birthday")
    print(f"{CHANGE}. Change a birthday")
    print(f"{DELETE}. Delete a birthday")
    print(f"{QUIT}. Quit the program")
    print("=" * 60)
    
    # Get user's choice
    # Try-except block: Handles exceptions that may occur during input conversion
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in [LOOK_UP, ADD, CHANGE, DELETE, QUIT]:
                return choice
            else:
                print(f"Error: Please enter a number between {LOOK_UP} and {QUIT}.")
        except ValueError:
            # Handle invalid numeric input (e.g., non-numeric characters)
            print("Error: Please enter a valid integer.")


def look_up(birthdays):
    """
    Look up a birthday in the dictionary.
    
    Args:
        birthdays (dict): Dictionary containing names and birthdays
    """
    name = input("Enter a name to look up: ")
    
    # Check if name exists in dictionary
    if name in birthdays:
        print(f"{name}'s birthday is {birthdays[name]}.")
    else:
        print(f"Sorry, {name} is not found in the dictionary.")


def add(birthdays):
    """
    Add a new birthday to the dictionary.
    
    Args:
        birthdays (dict): Dictionary containing names and birthdays
    """
    name = input("Enter a name: ")
    
    # Check if name already exists
    if name in birthdays:
        print(f"{name} already exists in the dictionary.")
        print(f"Current birthday: {birthdays[name]}")
        response = input("Do you want to change it? (yes/no): ").lower()
        if response == 'yes':
            birthday = input("Enter the birthday: ")
            birthdays[name] = birthday
            print(f"{name}'s birthday has been updated to {birthday}.")
    else:
        birthday = input("Enter the birthday: ")
        birthdays[name] = birthday  # Add new entry to dictionary
        print(f"{name}'s birthday ({birthday}) has been added to the dictionary.")


def change(birthdays):
    """
    Change an existing birthday in the dictionary.
    
    Args:
        birthdays (dict): Dictionary containing names and birthdays
    """
    name = input("Enter a name: ")
    
    # Check if name exists in dictionary
    if name in birthdays:
        print(f"Current birthday for {name}: {birthdays[name]}")
        new_birthday = input("Enter the new birthday: ")
        birthdays[name] = new_birthday  # Update birthday in dictionary
        print(f"{name}'s birthday has been changed to {new_birthday}.")
    else:
        print(f"Sorry, {name} is not found in the dictionary.")


def delete(birthdays):
    """
    Delete a birthday from the dictionary.
    
    Args:
        birthdays (dict): Dictionary containing names and birthdays
    """
    name = input("Enter a name: ")
    
    # Check if name exists in dictionary
    if name in birthdays:
        print(f"{name}'s birthday ({birthdays[name]}) will be deleted.")
        response = input("Are you sure? (yes/no): ").lower()
        if response == 'yes':
            del birthdays[name]  # Delete entry from dictionary
            print(f"{name}'s birthday has been deleted from the dictionary.")
        else:
            print("Deletion cancelled.")
    else:
        print(f"Sorry, {name} is not found in the dictionary.")


def main_birthdays():
    """
    Main function to run the names and birthdays program.
    """
    print("=" * 60)
    print("EXERCISE 2: Names and Birthdays Program")
    print("=" * 60)
    
    # Initialize empty dictionary
    birthdays = {}
    
    # Loop (while True): Continuously display menu until user chooses to quit
    while True:
        choice = get_menu_choice()
        
        # Process user's choice
        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)
        elif choice == QUIT:
            print("\nThank you for using the Birthday Dictionary program!")
            print(f"Total entries in dictionary: {len(birthdays)}")
            if birthdays:
                print("\nFinal dictionary contents:")
                for name, birthday in birthdays.items():
                    print(f"  {name}: {birthday}")
            break  # Exit the loop


# Run Exercise 2
main_birthdays()

print()
print("=" * 60)
print("All exercises completed!")
print("=" * 60)

# =============================================================================
# CITATIONS
# =============================================================================
print("\nCitations:")
print("1. Dictionary Operations in Python:")
print("   - Dictionary creation, access, update, and deletion")
print("   - Dictionary methods: keys(), values(), items()")
print("   Source: Python Documentation - Dictionaries")
print("   https://docs.python.org/3/tutorial/datastructures.html#dictionaries")
print()
print("2. Random Module:")
print("   - random.sample() for random selection without replacement")
print("   Source: Python Documentation - Random Module")
print("   https://docs.python.org/3/library/random.html")
print()
print("3. Card Game Values:")
print("   - Blackjack card values: numeric cards (2-10), face cards (10), aces (1 or 11)")
print("   Source: Standard Blackjack card values")
print()
print("4. Menu-Driven Programs:")
print("   - Design pattern for interactive programs with multiple options")
print("   Source: Common programming design pattern")
