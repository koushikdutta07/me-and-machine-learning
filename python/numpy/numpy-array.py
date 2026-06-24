import numpy as np

#one dimensional array

#converting list into array
a = [1,2,3,4,5]
b = np.array(a)
print("List:", a)
print("Array:", b)

#converting tuple into array
c = (1,2,3,4,5) 
d = np.array(c)
print("Tuple:", c)
print("Array:", d)

#converting set into array
e = {1,2,3,4,5}
f = np.array(e)
print("Set:", e)
print("Array:", f)

#converting string into array
g = "Hello"
h = np.array(g)
print("String:", g)
print("Array:", h)

#two dimensional array

#converting list of lists into array
i = [[1,2,3],[4,5,6],[7,8,9]]
j = np.array(i)
print("List of lists:", i)
print("Array:", j)


#zeroes array
k = np.zeros((3,3)) #R,C
print("Zeroes array:", k)

#ones array
l = np.ones((3,3)) #R,C
print("Ones array:", l)

#full array
m = np.full((3,3), 7) #R,C,Value
print("Full array:", m)

#eye array (identity matrix)
n = np.eye(3) #R,C
print("Eye array:", n)
