# Q3
# 출력할 구구단은? == 3
# 3 * 1 = 3
# 3 * 2 = 6
# ..
# 3 * 9 = 27

num = input("숫자를 입력하시오 >> ")

back = range(1, 10)  # 시작, 끝

for i in back:
    print(str(num) + " * " + str(i) + " = " + str(int(num) * (i)))
