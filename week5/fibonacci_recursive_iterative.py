#2017.10.04
#20171661 이다은
#fibonacci_recursive_iterative_compare

import time


#recursive
def recurfibo(n):
    if n <= 1:
        return n
    else:
        return recurfibo(n - 1) + recurfibo(n - 2)


#iterative
def iterfibo(n):
    now = 0
    former = 1
    formerFormer = 0
    for i in range(n):
        formerFormer = former
        former = now
        now = former + formerFormer
    return now

while True:
    num = int(input("Enter a number: "))
    if num == -1:
        print("end.")
        break
    elif num < -1:
        continue
    time_count1 = time.time()
    fibonumber = iterfibo(num)
    time_count1 = time.time() - time_count1
    print("IterFibo(%d) = %d, time %.20f" %(num, fibonumber, time_count1))
    time_count2 = time.time()
    fibonumber = recurfibo(num)
    time_count2 = time.time() - time_count2
    print("RecurFibo(%d) = %d, time %.20f" %(num, fibonumber, time_count2))

    if time_count2 > time_count1:
        print("Comparison: iterFibo is faster than recursiveFibo.")

    elif time_count1 == time_count2:
        print("Comparison: Both of functions are same.")

    else:
        print("Comparison: recursiveFibo is faster than iterFibo.")
