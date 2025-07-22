import random, sys, time
print("ROCK, PAPER, SCISSORS")

wins = 0
losses = 0 
ties = 0

while True:
    print("%s Wins, %s Losses, %s Ties " % (wins, losses, ties))
    while True:
        print("Enter your move. Rock (r), Paper (p), Scissors(s) or Quit (q).")
        players_input = input(">").lower()
        if players_input == 'q':
            sys.exit()
        if players_input == 'r' or 'p' or 's':
            break
        print("Type 'r' or 'p' or 's' or 'q'.")

    if players_input == 'r':
        print("ROCK versus ...")
    elif players_input == 'p':
        print("PAPER versus ...")
    elif players_input == 's':
        print("SCISSORS versus ...")

    move_number = random.randint(1,3)
    time.sleep(1)
    if move_number == 1:
        computer_move = 'r'
        print("-----ROCK-----")
    elif move_number == 2:
        computer_move = 'p'
        print("-----PAPER-----")
    else:
        computer_move = 's'
        print("-----SCISSORS-----")

    if players_input == computer_move:
        print("IT'S A TIE!")
        ties += 1
    elif players_input == 'r' and computer_move == 's':
        print("YOU WON!!!")
        wins += 1
    elif players_input == 's' and computer_move == 'p':
        print("YOU WON!!!")
        wins += 1
    elif players_input == 'p' and computer_move == 'r':
        print("YOU WON!!!")
        wins += 1
    elif players_input == 's' and computer_move == 'r':
        print("YOU LOOOOOSSSTTT!")
        losses += 1
    elif players_input == 'p' and computer_move == 's':
        print("YOU LOOOOOSSSTTT!")
        losses += 1
    elif players_input == 'r' and computer_move == 'p':
        print("YOU LOOOOOSSSTTT!")
        losses += 1
