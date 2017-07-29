#Make two functions
#Both of them accept an integer input "n" and return a list of the first "n" Fibonacci numbers.
#The catch:
#One function does this by recursion. The other uses no recursion.
#This function uses recursion
def F(n):
    for n in range(0,100)
        if n==0
            return 0
        elif n==1 or n==2
            return 1
        else:
            return F(n-1)+F(n-2)
        print F(5)

from math import sqrt
def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

def interface():
    n  = int(input("How many Fibonacci numbers would you like to see? "))
    print("The first ", n,"Fibonacci numbers are: ", F)

UI()
