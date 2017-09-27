# 2017/09/25
# software_proj2_class04
# 20171661 이다은
# 조합

def factorial(N):
    if N <= 1:
        return 1
    else:
        return N * factorial(N - 1)


def combination1(n, m):
    if n == m or m == 0:
        return 1
    elif n > m:
        return factorial(n) / (factorial(m) * factorial(n - m))


def combination2(n, m):
    if n == m or m == 0:
        return 1
    else:
        return combination2(n - 1, m - 1) + combination2(n - 1, m)


n = 0
run = True
while run:
    n = int(input("Enter n: "))
    if n < 0 and n != -1:
        print("양수인 정수 n을 입력해 주세요.")
        continue
    elif n == -1:
        print("종료")
        run = False
    else:
        m = int(input("Enter m: "))
        if m < 0:
            print("양수인 정수 m을 입력해 주세요.")
        elif n >= m:
            result1 = combination1(n, m)
            result2 = combination2(n, m)
            print("공식: C(", n, ",", m, ") = ", int(result1))
            print("재귀적 함수: C(", n, ",", m, ") = ", result2)
        else:
            print("n보다 작은 정수 m을 입력해 주세요")
