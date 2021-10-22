# gcd.py
#   This program finds the greatest common divisor of two values
#   entered by the user

def gcd(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        t = b
        b = a % t
        a = t
    return a

def main():
    m = eval(input("Enter m: "))
    n = eval(input("Enter n: "))
    print("GCD(",m,",",n,") = ",gcd(m,n))
main()

