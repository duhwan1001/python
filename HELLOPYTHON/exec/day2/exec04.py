# Q4
# 첫 숫자를 입력하시오 1
# 끝 숫자를 입력하시오 4
# 짝수의 합은 6입니다.

first = input("첫 숫자를 입력하시오 >> ")
last = input("끝 숫자를 입력하시오 >> ")

arr = range(int(first), int(last) + 1)

sum = 0

for i in arr:
    if i % 2 == 0:
        sum += i
    
print("합", sum)
