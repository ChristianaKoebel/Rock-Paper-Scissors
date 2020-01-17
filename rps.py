import check

# Helper function for fib_rec
# fib_acc(n,n0,last,prev) produces the nth Fibonacci number
#    using the n0th Fibonacci number (last) and the (n0-1)th Fibonacci number (prev)
# fib_acc: Nat Nat Nat Nat -> Nat
# requires: n0 <= n

def fib_acc(n,n0,last,prev):
    if n==n0:
        return last
    else:
        return fib_acc(n,n0+1,last+prev,last)
    
# fib_rec(n) produces the nth Fibonacci number
# fib_rec: Nat -> Nat
# Examples: 
# * fib_rec(0) => 0
# * fib_rec(10) => 55

def fib_rec(n):
    if n==0:
        return 0
    else:
        return fib_acc(n,1,1,0)
    
welcome_message = "Welcome to the Rock-Paper-Scissors game!"
prompt = "How would you like to play next [r/p/s/q]?\n"
goodbye_message = "Thank you for playing! Total game statistics:"

# play_rps() produces None and prints a game of rock, paper, scissors played
#    between the computer and a human player, who plays their next move after
#    reading a printed prompt asking them how they want to proceed (either r,p,s, or q).
# play_rps: None -> None
# Effects: prints a welcome message and a prompt asking the player what they
#    they want to play next, and reads in the choice. Each round, a line is 
#    printed indicating what was played and who won. At the end of the game,
#    total game statistics are printed.
# Examples:
# If the player chooses q right away, there will be zero tied games, zero player
#    wins, and zero computer wins.
# If the game lasts four rounds, with the player's choices: r,s,p,s,q (in that
#    order), there will be zero tied games, one player win, and three computer wins.

def play_rps():
    print(welcome_message)
    player_choice = input(prompt)
    tied_stats = 0
    player_win = 0
    computer_win = 0
    n = 1
    computer_choice = fib_rec(n)
    while player_choice != "q":
        computer_choice = fib_rec(n)
        if computer_choice%3 == 0:
            computer_move = "r"
        elif computer_choice%3 == 1:
            computer_move = "p"
        else:
            computer_move = "s"
        player_move = player_choice
        if player_move == computer_move:
            print("Player plays:"+" "+player_move+"."+" Computer plays:" + " "+\
                  computer_move+"."+" "+"Tied.")
            tied_stats = tied_stats + 1
            n = n + 1
            player_choice = input(prompt)
        if player_move == "r" and computer_move == "s":
            print("Player plays:"+" "+player_move+"."+" Computer plays:" + " "+\
                  computer_move+"."+" "+"Player won.")
            player_win = player_win + 1
            n = n + 1
            player_choice = input(prompt)
        if player_move == "r" and computer_move == "p":
            print("Player plays:"+" "+player_move+"."+" Computer plays:" + " "+\
                  computer_move+"."+" "+"Computer won.")
            computer_win = computer_win + 1
            n = n + 1
            player_choice = input(prompt)
        if player_move == "p" and computer_move == "r":
            print("Player plays:"+" "+player_move+"."+" Computer plays:" + " "+\
                  computer_move+"."+" "+"Player won.")
            player_win = player_win + 1
            n = n + 1
            player_choice = input(prompt)
        if player_move == "p" and computer_move == "s":
            print("Player plays:"+" "+player_move+"."+" Computer plays:" + " "+\
                  computer_move+"."+" "+"Computer won.")
            computer_win = computer_win + 1
            n = n + 1
            player_choice = input(prompt)
        if player_move == "s" and computer_move == "p":
            print("Player plays:"+" "+player_move+"."+" Computer plays:" + " "+\
                  computer_move+"."+" "+"Player won.")
            player_win = player_win + 1
            n = n + 1
            player_choice = input(prompt)
        if player_move == "s" and computer_move == "r":
            print("Player plays:"+" "+player_move+"."+" Computer plays:" + " "+\
                  computer_move+"."+" "+"Computer won.")
            computer_win = computer_win + 1
            n = n + 1
            player_choice = input(prompt)
    print(goodbye_message)
    print("Tied games:"+" "+str(tied_stats)+".")
    print("Player won"+" "+str(player_win)+" "+"times.")
    print("Computer won"+" "+str(computer_win)+" "+"times.") 
    
# Testing
# Test 1: Player enters "q" right away
check.set_input(["q"])
check.set_screen("0 tied games, 0 player wins, 0 computer wins")
check.expect("Q4T1", play_rps(), None)
# Test 2: One round, tie game
check.set_input(["p","q"])
check.set_screen("1 tie game, 0 player wins, 0 computer wins")
check.expect("Q4T2", play_rps(), None)
# Test 3: One round, player wins
check.set_input(["s","q"])
check.set_screen("0 tied games, 1 player win, 0 computer wins")
check.expect("Q4T3", play_rps(), None)
# Test 4: One round, computer wins
check.set_input(["r","q"])
check.set_screen("0 tied games, 0 player wins, 1 computer win")
check.expect("Q4T4", play_rps(), None)
# Test 5: Two rounds, all ties
check.set_input(["p","p","q"])
check.set_screen("2 tied games, 0 player wins, 0 computer wins")
check.expect("Q4T5", play_rps(), None)
# Test 6: Two rounds, 2 player wins
check.set_input(["s","s","q"])
check.set_screen("0 ties, 2 player wins, 0 computer wins")
check.expect("Q4T6", play_rps(), None)
# Test 7: Two rounds, 2 computer wins
check.set_input(["r","r","q"])
check.set_screen("0 ties, 0 player wins, 2 computer wins")
check.expect("Q4T7", play_rps(), None)
# Test 8: Two rounds, one win each
check.set_input(["s","r","q"])
check.set_screen("0 ties, 1 player win, 1 computer win")
check.expect("Q4T8", play_rps(), None)
# Test 9: Three rounds, all ties
check.set_input(["p","p","s","q"])
check.set_screen("3 ties 0 player wins, 0 computer wins")
check.expect("Q4T9", play_rps(), None)
# Test 10: Three rounds, all player wins
check.set_input(["s","s","r","q"])
check.set_screen("0 ties, 3 player wins, 0 computer wins")
check.expect("Q4T10", play_rps(), None)
# Test 11: Three rounds, all computer wins
check.set_input(["r","r","p","q"])
check.set_screen("0 ties, 0 player wins, 3 computer wins")
check.expect("Q4T11", play_rps(), None)
# Test 12: Three rounds, one tie, one player win, one computer win
check.set_input(["p","r","r","q"])
check.set_screen("1 tie, 1 player win, 1 computer win")
check.expect("Q4T12", play_rps(), None)
# Test 13: Four rounds, all ties
check.set_input(["p","p","s","r","q"])
check.set_screen("4 ties, 0 player wins, 0 computer wins")
check.expect("Q4T13", play_rps(), None)
# Test 14: Four rounds, all player wins
check.set_input(["s","s","r","p","q"])
check.set_screen("0 ties, 4 player wins, 0 computer wins")
check.expect("Q4T14", play_rps(), None)
# Test 15: Four rounds, all computer wins
check.set_input(["r","r","p","s","q"])
check.set_screen("0 ties 0 player wins, 4 computer wins")
check.expect("Q4T15", play_rps(), None)
# Test 16: Four rounds, 1 tie, 1 player win, 2 comuter wins
check.set_input(["p","s","p","s","q"])
check.set_screen("1 tie, 1 player win, 2 computer wins")
check.expect("Q4T16", play_rps(), None)
# Test 17: Four rounds, 0 ties, 1 player win, 3 computer wins
check.set_input(["r","s","p","s","q"])
check.set_screen("0 ties, 1 player win, 3 computer wins")
check.expect("Q4T17", play_rps(), None)