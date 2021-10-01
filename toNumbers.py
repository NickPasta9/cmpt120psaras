# toNumbers.py
# This function will use strings to count entries converting them
# into certain numbers

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])

def squareEach(nums):
    nums = []
    for i in nums:
        nums = nums.append(i**2)
    return nums

def sumList(x):
    return (x[0] + sumList(x[1:])) if x else 0

def main():
    file = input("Please enter a file name: ")
    fobj = open(file, "r")
    strList = fobj.readlines()
    fobj.close()
    nums = toNumbers(strList)
    x = squareEach(nums)
    result = sumList(x)
    print("The sum of the squares of the values in the file is", result)
main()
