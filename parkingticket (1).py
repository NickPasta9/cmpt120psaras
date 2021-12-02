# parkingticket.py
#   This program will determine the price of a speeding ticket based on the
#   fine policy in Podunksville

def main():
    limit = float(input("what was the speed limit? "))
    speed = float(input("What was your clocked speed? "))
    if speed > 90:
        bigfine = ((speed - limit) * 5 + 250)
        print("your fine is", bigfine)
    elif speed <= limit:
        print("you were traveling a legal speed")
    else:
        fine = ((speed - limit) * 5 + 50)
        print("your fine is", fine)

main()
