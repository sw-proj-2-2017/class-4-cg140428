#2017.10.04
#20171661 이다은
#fibonacci_recursive_iterative_compare

import time


#recursive
def recurfibo(n):
    if n <= 1:
        return n
    return recurfibo(n -1) + recurfibo(n - 2)


#iterative
def iterfibo(n):
    fibonum = [0, 1]
    if n <= 1:
        return n
    else:
        for i in range(0, n - 1):
            next = fibonum[i] + fibonum[i+1]
            fibonum.append(next)
        return fibonum[n]

while True:
    num = int(input("Enter a number: "))
    if num == -1:
        break
    time_count = time.time()
    fibonumber = iterfibo(num)
    time_count = time.time() - time_count
    print("IterFibo(%d) = %d, time %.20f" %(num, fibonumber, time_count))
    time_count = time.time()
    fibonumber = recurfibo(num)
    time_count = time.time() - time_count
    print("RecurFibo(%d) = %d, time %.20f" %(num, fibonumber, time_count))