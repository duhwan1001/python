import random
mine = input("홀/짝을 선택하세요")
com = ""
result = ""

rnd = random.random()

if rnd < 0.5:
    com = "홀"
else:
    com = "짝"
    
if mine == com:
    result = "이김"
else:
    result = "패배"
    
# 자바처럼 + 쓴다면 변수들의 형이 다를경우 형변환을 요청하게 된다. 따라서 형변환 작업을 거치지 않으려면 , 를 쓰는게 편함
print("com : ", com)
print("mine : ", mine) 
print("result :", result)

# if mine == "홀":
#     hole = rnd / 2
#     if hole == 0:
#         print("정답!") 
#
# elif mine == "짝":
#     hole = rnd / 2
#     if hole == 1:
#         print("정답!") 