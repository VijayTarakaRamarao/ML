import numpy as np

# Question1
a=np.random.randint(1,20,15)

print("\n")
# 1.a Reshape the array to 3 by 5
a=a.reshape(3,5)
print(a)

print("\n")
# 1.b Print array shape.
print(a.shape)

print("\n")
# 1.c Replace the max in each row by 0
a[np.where(a==np.max(a))]=0
print(a)