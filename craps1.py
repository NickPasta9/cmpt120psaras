# craps.py
# This program will ask the user how many games of craps to simulate.

from random import randrange

def main():
    printIntro()
    n = eval (input("How many rolls should I simulate? >>"))
    wins, losses = SimNCraps(n)
    printSummary(wins, losses, n)

def printIntro():
    print("This program is designed to simulate (n) games of craps")
    print("and will return the probability of winning based on the")
    print("simulation.")

def sim_N_Amount_Craps(n):
    wins = 0
    losses = 0
    for i in range(n):
        if simOneGame() is True:
            wins = wins + 1
        else:
            losses = losses + 1
        return wins, losses

def simOneGame():
    x = randrange(2,12)
    if x == 2 or x == 3 or x == 12:
        return False
    elif x == 7 or x == 11:
        return True
    else:
        y = 0
        while x != y and x != 7:
            y = randrange(2,12)
            if y == 7:
                return False
            elif y == x:
                return True

def printSummary(wins, losses, n):
    print("\nGames simulated: ", n)
    print("Winning rolls: {0} ({1:0.1%})".format(wins, wins/n))
    print("Losing rolls: {0} ({1:0.1})".format(losses, losses/n))

if __name__ == ' __main__': main()


