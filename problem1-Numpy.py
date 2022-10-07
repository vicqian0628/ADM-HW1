###Arrays###

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr1 = []
    for i in arr:
        arr1.append(float(i))
    return numpy.array(arr1[::-1])
    
    
###Shape and Reshape###

import numpy as np

print(np.array(input().split(), int).reshape(3,3))


###Transpose and Flatten###

import numpy as np

rows, cols = list(map(int, input().split()))
matrix = np.array([list(map(int, input().split())) for _ in range(rows)])
print(matrix.T)
print(matrix.flatten())


###Concatenate###

import numpy as np

M, N, P = map(int, input().split())   
arr1 = np.array([list(map(int, input().split())) for _ in range(M)])
arr2 = np.array([list(map(int, input().split())) for _ in range(N)])
print(np.concatenate((arr1, arr2)))


###Zeros and Ones###

import numpy as np

shapes = list(map(int, input().split()))
print(np.zeros((shapes), dtype = np.int))
print(np.ones((shapes), dtype = np.int))


###Eye and Identity###

import numpy 

numpy.set_printoptions(sign=' ')
print(numpy.eye(*map(int, input().split())))


###Array Mathematics###

import numpy as np

n, m = map(int, input().split())
a = [np.array(input().split(), int) for _ in range(n)]
b = [np.array(input().split(), int) for _ in range(n)]
functions = [np.add, np.subtract, np.multiply, np.floor_divide, np.mod, np.power]
[print(np.array(fn(a,b))) for fn in functions]


###Floor, Ceil and Rint###

import numpy as np

np.set_printoptions(legacy='1.13')
a = np.array(list(map(float, input().split())))
print(f"{np.floor(a)}\n{np.ceil(a)}\n{np.rint(a)}")


###Sum and Prod###

import numpy as np
n, m = map(int, input().split())
npArr = np.array([list(map(int, input().split())) for _ in range (n)], np.int64)
print(np.prod(np.sum(npArr, axis=0), axis=None))


###Min and Max###

import numpy as np
n, m = map(int, input().split())
npArr = np.array([list(map(int, input().split())) for _ in range (n)], np.int64)
print(np.max(np.min(npArr, axis=1)))


###Mean, Var, and Std###

import numpy as np
n,_ = map(int,input().split())
my_array = np.array([list(map(int,input().split())) for _ in range(n)])
print(np.mean(my_array,1), np.var(my_array,0), round(np.std(my_array),11), sep = "\n")


###Dot and Cross###

import numpy as np

n = int(input())
A = np.array([list(map(int, input().split())) for _ in range (n)], np.int64)
B = np.array([list(map(int, input().split())) for _ in range (n)], np.int64)
print(np.dot(A,B))

###Inner and Outer###

import numpy as np

A = np.array(list(map(int, input().split())) , np.int64)
B = np.array(list(map(int, input().split())) , np.int64)
print(np.inner(A,B))
print(np.outer(A,B))


###Polynomials###

import numpy as np

a = list(map(float, (y for y in input().split())))
print(np.polyval(a,int(input())))


###Linear Algebra###

import numpy as np

print(round(np.linalg.det(np.array([list(map(float, input().rsplit())) for _ in range(int(input()))])),2))
