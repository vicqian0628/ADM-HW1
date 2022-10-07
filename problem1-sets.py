###Introduction to Sets###

def average(array):
    # your code goes here
    return float(sum(set(array))/len(set(array)))
    
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
	
	
###Symmetric Difference###

M=int(input())
set1=set([int(x) for x in input().split()])
N=int(input())
set2=set([int(x) for x in input().split()])
result = sorted(set(set1.difference(set2).union(set2.difference(set1))))
for i in result:
    print(i)
	
	
###No Idea!###

temp = 0
_, array = input(), input().split()
A, B = set(input().split()), set(input().split())
for arr in array:
    if arr in A: temp+=1
    if arr in B: temp-=1
print(temp)


###Set .add()###

l=[]
a=int(input())
for i in range (a):
     b=input()
     l.append(b)
b=set(l)
print(len(b))


###Set .discard(), .remove() & .pop()###

n = int(input())
data = set(map(int, input().split()))

operations = int(input())

for x in range(operations):
  oper = input().split()
  if oper[0] == "remove":
    data.remove(int(oper[1]))
  elif oper[0] == "discard":
    data.discard(int(oper[1]))
  else:
    data.pop()
    
print(sum(data))


###Set .union() Operation###

input()
s1 = {s for s in input().split()}
input()
s2 = {s for s in input().split()}
print(len(s1.union(s2)))


###Set .intersection() Operation###

_, A = input(), set(input().split())
_, B = input(), set(input().split())
print(len(A & B))


###Set .difference() Operation###

_, A = input(), set(input().split())
_, B = input(), set(input().split())
print(len(A - B))


###Set .symmetric_difference() Operation###

_, A = input(), set(input().split())
_, B = input(), set(input().split())
print(len(A ^ B))


###Set Mutations###

_, A = input(), set(input().split())
for _ in range(int(input())):
    (op, _), B = input().split(), set(input().split())
    eval(f'A.{op}({B})')
print(sum(map(int, A)))


###The Captain's Room###

from collections import Counter
group_size=int(input())
room_list=list(map(int,input().split()))

C = Counter(room_list)

for i,j in C.items():
    if j<group_size:
        print(i)
	

###Check Subset###

numberOfTest = int(input())
for i in range(numberOfTest):
    temp = input()
    setA = set(map(int, input().split()))
    temp = input()
    setB = set(map(int, input().split()))
    if len(setB.intersection(setA)) == len(setA):
        print("True")
    else:
        print("False")
	
	
###Check Strict Superset###

setA = set(map(int, input().split()))
n = int(input())
ctr = 0
for i in range (n):
    tempSet = set(map(int, input().split()))
    if(setA.issuperset(tempSet)):
        ctr += 1
if(ctr == n):
    print("True")
else:
    print("False")
    
    

