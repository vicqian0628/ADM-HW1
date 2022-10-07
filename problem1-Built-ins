###Zipped!###

n, m = map(int, input().split())
marks = []
for i in range(m):
    row = [float(x) for x in input().split()]
    marks.append(row)
print(*list(sum(x)/m for x in zip(*[x for x in marks])), sep='\n')


###Athlete Sort###

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    sorted_list = sorted(arr, key=lambda x:x[k])
    for x in sorted_list:
            print(*x)
            
            
###ginortS###

S=list(input())

number=[]
lower=[]
upper=[]
for i in S:
    if i.isdigit():
        number.append(i)
    else:
        if i.isupper():
            upper.append(i)
        else:
            lower.append(i)

a=sorted(list(map(int,number)))
b=list(map(str,sorted(a,key=lambda x:x%2==0)))

print(''.join(sorted(lower))+''.join(sorted(upper))+''.join(b))


    
    
