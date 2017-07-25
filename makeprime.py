def make_prime_list(upper):
    if upper<2:
        return []
    if upper==2:
        return [2]
    ou = [2]
    for test in range(3,upper+1):
        isGood = True
        for challange in ou:
            if (test%challange)==0:
                isGood = False
                break
        if isGood:
            ou.append(test)
    return ou

def make_writeable(lst):
    ou = []
    for x in lst:
        s = str(x)
        for c in s:
            ou.append(ord(c))
        ou.append(13)
        ou.append(10)
    bdata = bytes(ou)
    return bdata

def save_bytes(bdata,filename):
    outfile = open(filename,"wb")
    outfile.truncate(0)
    outfile.seek(0,0)
    outfile.write(bdata)
    outfile.close()

def main():
    upper = 1000
    filename = "primes.txt"
    lst = make_prime_list(upper)
    bdata = make_writeable(lst)
    del(lst)
    save_bytes(bdata,filename)

main()
