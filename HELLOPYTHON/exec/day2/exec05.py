# Q5
# 첫 숫자를 입력하시오 1
# 끝 숫자를 입력하시오 4
# 홀수의 합은 5입니다.

first = input("첫 숫자를 입력하시오 >> ")
last = input("끝 숫자를 입력하시오 >> ")

arr = range(int(first), int(last) + 1)

sum = 0

for i in arr:
    if i % 2 == 1:
        sum += i
    
print("홀수의 합은 {} 입니다".format(sum))
