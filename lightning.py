#Write a program to calculate the distance to a lightning strike based on the time lapsed
#between the flash and the sound of thunder. The speed of sound is approx. 1100 ft/sec
#and 1 mile is 5280 ft.

def main():
    print("This program finds the distance to a lightning strike in miles.")
    print()
    light = eval(input("Please enter the time in seconds from the lightning strike till you heard the thunder "))
    dis = light * 1100 / 5280

    print("The lightning strike was", dis, "miles away")

main()
