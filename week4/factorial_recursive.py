#2017/09/25
#software_proj2_class04
#20171661 이다은
#factorial 재귀

N = int(input("Enter your number: "))


def factorial(N):
    if N <= 1:
        return 1
    else:
        return N*factorial(N-1)

print(N,"! = ",factorial(N))
