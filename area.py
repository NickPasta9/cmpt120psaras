import math

def main():
    print("This program calculates the cost per square inch of a circular object.")

    diameter = eval(input("What is the diameter of the object? "))
    price = eval(input("What is the price of the whole object? "))

    cost_per_square = price / (math.pi * (diameter / 2)**2)

    print("The cost per square inch is $", round(cost_per_square, 2), sep="")

main()
