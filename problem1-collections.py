###collections.Counter()###

n = int(input())
l = list(map(int,input().split()))

n2 = int(input())
s = 0
for _ in range(n2):
    a, b = tuple(map(int,input().split()))
    if a in l:
        s += b
        l.remove(a)
print(s)


###DefaultDict Tutorial###

from collections import defaultdict
d1=defaultdict(list)
nums=input().split(" ")
n=int(nums[0])
m=int(nums[1])
for i in range(n):
    d1['A'].append(input())
for j in range(m):
    d1['B'].append(input())

for k in d1['B']:
    d2=[]
    for l in range(len(d1['A'])):
        if k == d1['A'][l]:
            d2.append(l+1)
    if d2==[]:
        d2=[-1]   
    print(' '.join(map(str, d2)))
    
    
###Collections.namedtuple()###

from collections import namedtuple

students = int(input())
cols_name = input().split()
cols = namedtuple('col', cols_name)
total_marks = 0

for student in range(students):
    student_details = input().split()
    rows = cols(ID=student_details[cols_name.index('ID')], MARKS=student_details[cols_name.index('MARKS')],
                NAME=student_details[cols_name.index('NAME')], CLASS=student_details[cols_name.index('CLASS')])
    total_marks += int(rows.MARKS)

print("{:0.2f}".format(total_marks/students))

###Collections.OrderedDict()###

n = int(input())
dic = {}

for i in range(n):
    a = input().split()
    item = " ".join(a[:-1])
    price = int(a[-1])

    dic[item] = price + dic.get(item, 0)

for i, j in dic.items():
    print(i, j)
    
    
###Word Order###

from collections import OrderedDict


dct = OrderedDict()
for i in (input() for _ in range(int(input()))):
    if i in dct.keys():
        dct[i] += 1
    else:
        dct[i] = 1
        
print(len(dct.keys()))
print(*dct.values(), sep=' ')


###Collections.deque()###

from collections import deque
n=int(input())
d=deque()
for _ in range(n):
    com, *args=input().split()
    if com not in ['pop','popleft']:
        eval(f'd.{com}({",".join(args)})')
    else:
        eval(f'd.{com}()')
        
print(*d, sep=' ')


###Piling Up!###

from collections import deque
n = int(input())
for i in range(n):
    m = int(input())
    block = deque(map(int, input().split()))
    for j in range(m-1):
        if block[0] >= block[1] and block[0] >= block[-1]:
            block.popleft()
        elif block[-1] >= block[-2] and block[-1] >= block[0]:
            block.pop()
    if len(block) < 2:
        print('Yes')
    else:
        print('No')
        
        

###Company Logo###

from collections import Counter

print(*[f"{a} {b}" for a, b in Counter(sorted(s)).most_common(3)], sep = "\n")


