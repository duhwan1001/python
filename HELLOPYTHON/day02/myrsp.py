import random
mine = input("가위 바위 보 입력 >>  ")
com = ""
result = ""

rnd = random.random()

if rnd < 0.33:
    com = "가위"
elif rnd < 0.66:
    com = "바위"
else:
    com = "보"

if mine == com:
    result = "비김"
    
elif mine == "가위" and com == "바위":
    result = "패배"
elif mine == "가위" and com == "보":
    result = "이김"
    
elif mine == "바위" and com == "가위":
    result = "이김"
elif mine == "바위" and com == "보":
    result = "패배"
    
elif mine == "보" and com == "가위":
    result = "패배"
elif mine == "보" and com == "바위":
    result = "이김"
    
# 자바처럼 + 쓴다면 변수들의 형이 다를경우 형변환을 요청하게 된다. 따라서 형변환 작업을 거치지 않으려면 , 를 쓰는게 편함
print("com : ", com)
print("mine : ", mine) 
print("result :", result)

# arr = range(100)
# for i in arr:
#     print(random.random())
