#2017/09/25
#software_proj2_class04
#20171661 이다은
#조합

def factorial(N):
    if N <= 1:
        return 1
    else:
        return N*factorial(N-1)


def combination(n,m):
    if n == m:
        return 1
    elif n > m:
        return factorial(n)/(factorial(m)*factorial(n-m))
n = 0
run = True
while run:
    n = int(input("Enter n: "))
    if n < 0 and n != -1:
        print("양수인 정수를 입력해 주세요.")
        continue
    elif n == -1:
        print("종료")
        run = False
        break
    else:
        m = int(input("Enter m: "))
        if m < 0:
            print("양수인 정수를 입력해 주세요.")
        elif n > m:
            result = combination(n,m)
            print("C(",n,",",m,") = ", result)