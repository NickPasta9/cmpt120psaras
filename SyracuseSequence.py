# SyracuseSequence.py
#   This program will ask for a starting value and print the Syracuse sequence
#   for that value

def main():
    num = eval(input("Enter a positive integer: "))
    print(str(num) + ", ", end="")
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3*num + 1
        if num != 1:
            print(str(num) + ", ", end= "")
        else:
            print(1)
