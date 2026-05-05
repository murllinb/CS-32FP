# CS-32FP
CS32 FP by [Murllin Bender]

Project Background: 
Dice Tic-Tac-Toe is a variation of the classic game that maintains the traditional 3×3 grid and objective of aligning three symbols in a row, column, or diagonal. However, this version introduces an element of chance and strategy by allowing players to choose between placing their symbol or rolling a die on each turn.

At the start of the game, players select a die with fixed odds that determine special actions. Rolling the die can result in abilities such as removing one of the player’s own symbols or an opponent’s symbol from the board. This adds a new dynamic layer of gameplay to game, while also allowing for online play with the local networking system with a server and 2 clients.

Instructions:
In order to play Dice Tic-Tac-Toe, you first need to install socket32.py, dice.py, TTT_server.py, TTT_client1.py, and TTT_client2.py.
In order to play this game, there must be 3 split terminals running.
1. Initialize basegame_server.py in one of the terminals. 
2. Initialize basegame_client1.py in one of the other terminals.
3. Initialize basegame_client2.py in the last terminal.
4. Have the player in basegame_client1.py pick which dice they would like to use.
5. Have the player in basegame_client2.py pick which dice they would like to use.
  * Extreme Dice: 1/2 odds of removing your opponents piece or your piece
  * Intermediate Dice: 1/4 odds of removing your opponents piece or your piece and 1/2 odds of nothing happening.
  * Beginnner Dice:  1/6 odds of removing your opponents piece or your piece and 2/3 odds of nothing happening.
6. At the start of each round pick whether you want to roll the dice or place your symbol.
7. If dice was rolled proceed with whatever attribute you were given.
8. If you chose to place you piece then place it on the board.
9. Repeat steps 6-8 until there is a draw or a winner.
10. Select whether you would like to play another round.

Future Project Plans:
There are a lot of areas that could be improved on in the game, some issues with networking like broadcasts for the waiting player to await the active player's decision could be improved on, and the overall structure could be broken down more into a cleaner formatting. Moving forward it would be best to clean the code for cleaner understanding, but also to expand on the server client codes by allowing for multiple connections to the server, potentially setting up lobbies that could be accessed by a custom password. The dice element of this game could also be expanded upon by adding more abilities to the dice, allowing for a more diverse player experience.


Resources Used:
* ChatGPT: Used to refine formatting issues and troubleshoot issues with server logic(i.e. find a way to clear the terminal to avoid clutter and format text to appear more visibly clear in the terminal). Commented parts where ChatGPT was used/helped.
* Pset 3 (copied socket32.py)
* Modified socket logic for 2 clients: https://www.youtube.com/watch?v=5G_bNVKdECk
* Threading logic used for 2 clients: https://docs.python.org/3/library/threading.html

FP Submission Video Link:
