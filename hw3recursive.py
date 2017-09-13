#Make two functions
#Both of them accept an integer input "n" and return a list of the first "n" Fibonacci numbers.
#The catch:
#One function does this by recursion. The other uses no recursion.
#This function uses recursion (using F to find itself)

lower = 1
upper = 10000000000

def F(n):
    for n in range(lower,upper+1):
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        while n>2:
            print F(n)
            return (F(n-2) + F(n-3)) + (F(n-3) + F(n-4))
            # using F to compute itself:
            # F(n) = F(n-1) + F(n-2)
            # F(n-1) = F(n-2) + F(n-3)
            # F(n-2) = F(n-3) + F(n-4)

def UI():
    print("The first 5 Fibonacci numbers are: ", F(5))
    n  = int(input("How many Fibonacci numbers would you like to see? "))
    print("The first ", n,"Fibonacci numbers are: ", F(n))

UI()
