n = int(input())

if 5 < n < 2000:
    
    for e in range(1,n+1):
        if e % 2 == 0:
            print("{}^{} = {}".format(e,2,e**2))