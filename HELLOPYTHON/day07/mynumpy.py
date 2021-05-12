import numpy as np  # Alias

arr = [1, 2, 3, 4, 5]

arr_n = np.array(arr)  # arr를 np의 array 형태로

print(arr)
print(arr_n)

arr = arr * 5
print(arr)
# [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

arr_n = arr_n * 5
print(arr_n)
# [5 10 15 20 25]