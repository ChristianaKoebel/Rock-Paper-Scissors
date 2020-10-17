# Rock-Paper-Scissors-Python

This program prints a game of rock, paper, scissors played between the computer and a human player, who inputs their next move after reading a printed prompt asking them how they want to proceed (either "r" for rock, "p" for paper, "s" for scissors, or "q" for quit). If the user enters "q", the game ends. 

Each round, a line is printed indicating what was played and who won. At the end of the game, total game statistics are printed.

The computer's move is determined by an equation involving the n-th round of the game and the n-th Fibonacci number. For the n-th round (n = 1 for the first round), the computer computes F_n modulo 3 where F_n is the n-th Fibonacci number. If the result is 0, the computer’s move is "r"; if the result is 1, the computer's move is “p”; otherwise, the computer's move is “s”.

Click [here](https://github.com/ChristianaKoebel/Rock-Paper-Scissors/blob/master/rock_paper_scissors.py) for the Python program (rock_paper_scissors.py) and [here](https://github.com/ChristianaKoebel/Rock-Paper-Scissors/blob/master/check.py) for the check.py module, which is used for running the tests in rock_paper_scissors.py.
