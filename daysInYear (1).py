#leapCheck.py
#   This program will use a mathematical function to find leap year in Februrary

def main():
    date = input("Enter the date (dd/mm/yyyy: ")
    d = date.split("/")
    d0 = int(d[0])
    d1 = int(d[1])
    d2 = int(d[2])

    # JA: You should use the three steps described

    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    leapYear = [31,29,31,30,31,30,31,31,30,31,30,31]

    num = 0
    if d2%4 != 0:
        for i in range(d1 - 1):
            num = num + months[i]
        num = num + d0
    elif d2%4 ==0:
        for i in range(d1 - 1):
            num = num + d0
        print(num)

main()
