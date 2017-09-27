#2017/09/25
#software_proj2_class04
#20171661 이다은
#factorial 재귀


def factorial(N):
    if N <= 1:
        return 1
    else:
        return N*factorial(N-1)

run = True

while run:
    N = int(input("Enter your number: "))
    if N >= 0:
        print(N,"! = ",factorial(N))
    elif N == -1:
        run = False
        print("end")
    else:
        N = int(input("Enter positive number: "))
