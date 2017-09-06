#20171661 Lee DaEun

mul = 1
run = True

while run:
    num = int(input("Enter your number: "))
    #입력값이 0일 때
    if num ==0:
        print(num, "! = ", mul)
    #입력값이 -1일 때
    elif num == -1:
        print("종료되었습니다.")
        run = False
    #입력값이 음수인 정수일 때
    elif num <-1:
        print("양수인 정수를 입력해주세요.")
    #입력값이 양수인 정수일 때
    else:
        for i in range(1,num+1):
            mul *= i
        print(num,"! = ", mul)
    mul =1