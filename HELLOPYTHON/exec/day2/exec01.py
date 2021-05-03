# Q1
# 첫 숫자를 입력하시오 1
# 끝 숫자를 입력하시오 3
# 숫자의 합은 4입니다.

first = input("첫 숫자를 입력하시오 >> ") # 미리 int로 받아도 됨 // input("첫 숫자를 입력하시오 >> ")
last = input("끝 숫자를 입력하시오 >> ")

print(first)
print(last)

sum = int(first) + int(last)

print("합", sum)
