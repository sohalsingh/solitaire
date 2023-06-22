import random

# Define card ranks and suits
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["♠", "♣", "♦", "♥"]

# Create a deck of cards
deck = [(rank, suit) for rank in ranks for suit in suits]

# Shuffle the deck
random.shuffle(deck)

# Initialize the foundation piles
foundations = {suit: [] for suit in suits}

# Initialize the tableau piles
tableau = [[] for _ in range(7)]

# Deal cards to tableau
for i in range(7):
    tableau[i] = [deck.pop() for _ in range(i + 1)]

# Initialize the stock and waste piles
stock = deck
waste = []

# Function to display the game state
def display_game():
    print("Foundations:")
    for suit, pile in foundations.items():
        print(f"{suit}: {' '.join(pile)}")
    print("\nTableau:")
    for pile in tableau:
        print(' '.join(card[0] + card[1] for card in pile))
    print("\nStock:", len(stock), "cards left")
    print("Waste:", ' '.join(card[0] + card[1] for card in waste))


# Function to check if a move is valid
def is_valid_move(card, destination):
    if destination == "F":
        suit = card[1]
        if len(foundations[suit]) == 0:
            return card[0] == "A"
        else:
            last_rank = foundations[suit][-1][0]
            return ranks.index(card[0]) == ranks.index(last_rank) + 1
    elif destination == "T":
        pile = tableau[int(card)]
        if len(pile) == 0:
            return True
        else:
            last_card = pile[-1]
            return card[0] == ranks[ranks.index(last_card[0]) - 1] and card[1] != last_card[1]
    return False

# Function to make a move
def make_move(card, destination):
    if destination == "F":
        foundations[card[1]].append(card)
    elif destination == "T":
        tableau[int(card)].append(card)
    elif destination == "W":
        waste.append(card)

# Function to check if the game is won
def is_game_won():
    return all(len(pile) == 13 for pile in foundations.values())

# Main game loop
while True:
    display_game()
    if is_game_won():
        print("\nCongratulations! You won!")
        break

    command = input("\nEnter a command (e.g., 'W 2', 'T 4'): ")
    parts = command.split()
    if len(parts) == 2:
        destination, source = parts
        if destination in ("F", "T", "W") and source.isdigit() and 1 <= int(source) <= 7:
            source = int(source) - 1
            if destination == "W" and source == -1:
                if len(stock) > 0:
                    card = stock.pop()
                    make_move(card, "W")
                else:
                    stock = waste
                    waste = []
            else:
                source_pile = waste if source == -1 else tableau[source]
                if len(source_pile) > 0:
                    card = source_pile[-1]
                    if is_valid_move(card, destination):
                        source_pile.pop()
                        make_move(card, destination)

    elif command == "R":
        random.shuffle(waste)
        stock += waste
        waste = []

    elif command == "Q":
        print("\nThanks for playing! Goodbye!")
        break

    else:
        print("\nInvalid command. Please try again.")
