# computeEaster.py
#    This program uses a formula to track the proper date on which easter will
#    fall on each year from 1900-2099

def computeEaster(year):
    # compute needed values for equation
    a = (year % 19)
    b = (year % 4)
    c  = (year % 7)
    d = ((19*a + 24) % 30)
    e = ((2*b + 4*c + 6*d + 5) % 7)

    day = 22 + d + e

    # check if one of four years in question
    if year in [1954, 1981, 2049, 2076]:
        day = day - 7

    if day > 31:
        return 'April ' + str(day - 31)
    else:
        return 'March ' + str(day)

def main():
    year = int(input('Enter a year (1900-2099): '))
    if 1900 <= year <= 2099:
        print('Easter will be on', computeEaster(year), 'in', year)
    else:
        print('Error: Value not in range. Exiting program...')

main()
