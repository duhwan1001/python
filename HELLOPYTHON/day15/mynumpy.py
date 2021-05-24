import numpy as np

a = np.zeros((4, 4))
b = np.ones((5, 5)) * 5

# print(a)
# print(b)

print(a.shape)
print(b.shape)

c = a.reshape((16)) # 개수가 맞아야 함
print(c)

