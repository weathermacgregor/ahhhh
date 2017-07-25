f = open("C:/Users/macgr/Desktop/ahhhh/prime.txt", "w+")
lower = 1
upper = 1000

for x in range(lower,upper + 1):
    if x > 2:
        for i in range(2,x):
            if (x % i) == 0:
                break
        else:
            f.write(str(x)+', ')

f.close()
