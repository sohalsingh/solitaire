# solitaire

This is a text-based implementation of the Solitaire game in Python. It provides a command-line interface for playing the game. The game follows the standard rules of Solitaire, where the goal is to build up the foundations piles from Ace to King for each suit.

## Getting Started

To run the game, make sure you have Python installed on your system. The code is compatible with both Python 2 and Python 3.

1. Download the `solitaire.py` file from this repository.

2. Open a terminal or command prompt and navigate to the directory where the `solitaire.py` file is located.

3. Run the following command to start the game:
    ```
    python solitaire.py
    ```

4. Follow the on-screen instructions to play the game. Enter commands to move cards between the tableau piles, foundations, and waste pile. The commands are in the format `Destination Source`, where `Destination` can be `F` (foundations), `T` (tableau), or `W` (waste), and `Source` is the number of the tableau pile (1-7) or `-1` for the waste pile.

## Game Controls

- To move a card from the waste pile to a tableau pile, enter a command in the format `W <Tableau Pile Number>`. For example, `W 2` will move a card from the waste pile to tableau pile 2.

- To move a card within the tableau piles, enter a command in the format `T <Tableau Pile Number>`. For example, `T 4` will move a card within tableau pile 4.

- To restart the game and reshuffle the waste pile, enter the command `R`.

- To quit the game, enter the command `Q`.

## Game State Display

The game state is displayed after each move. It includes the current state of the foundations, tableau piles, stock pile (remaining cards), and waste pile.

## Winning the Game

The game is won when all the foundation piles have all 13 cards in ascending order, from Ace to King, for each suit. Once you win, a congratulatory message will be displayed.

---

Feel free to customize the README file further and add any additional information you find necessary.
