# BeverageGame
A python script that enables N users to play a game, whilst consuming beverages

The owner of this repository does not condone the use of alcohol by those under the legal drinking age in their state.

## Use ##

``bash
python3 main.py
``
The program will then prompt for a number of players, and their names

Several rounds are defined for play and the program will continually randomly select and play a round

## Contributing rounds ##

If you have any ideas for a new round, it can be added to the rounds directory in the form of a single python function inside a single file.

The function must take a Players object.

Once written it can be added to the list of rounds in rounds.txt
