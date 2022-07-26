import random

def factors(n):
    for k in range(1, n+1):
        if n % k == 0:
            yield k

def is_multiple(n, m):
    if (n % m == 0):
        print(True)
    else:
        print(False)

def is_even(k):
    while(k>0):
        k-=2
    return bool(k+1)

def minmax(data):
    data.sort()
    return data[0], data[-1]

def sumsquares(n):
    sum = 0
    while (n != 0):
        sum += (n-1) ** 2
        n -= 1
    return sum

def compressedsum(n):
    return sum(i**2 for i in range(n))

def sumsquaresodd(n):
    sum = 0
    while (n!=0):
        n -= 1
        if n % 2 == 1:
            sum += (n ** 2)
    return sum

def compressedsumodd(n):
    return sum(i**2 for i in range(n) if i % 2 == 1)

def sameElement(s):
    for k in range(-1, -len(s)-1, -1):
        j = k + len(s)
        print(s[k], s[j]) #should be similar

def rangeconstruct():
    for i in range(50,90,10):
        print(i)

def rangeconstruct2():
    for i in range(8,-10, -2):
        print(i)

def compressedListDoubling():
    l = [2**i for i in range(0,9)]
    return l

def choice(data):
    return data[random.randrange(len(data))]

