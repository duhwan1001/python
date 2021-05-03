# Q2
# 첫 숫자를 입력하시오 1
# 끝 숫자를 입력하시오 3
# 모든 수의 합은 6입니다.

first = int(input("첫 숫자를 입력하시오 >> "))
last = int(input("끝 숫자를 입력하시오 >> "))

arr = range(first, last + 1)

print("arr", arr)

sum = 0

for i in arr:
    sum += i
    
print("숫자의 합은 {} 입니다.".format(sum))
