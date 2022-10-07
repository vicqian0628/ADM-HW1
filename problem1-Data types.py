###Tuples###

Wrong answer.....I don't know zzz


###List Comprehensions###

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    first_list = [x for x in range(x + 1)]
    second_list = [y for y in range(y + 1)]
    third_list = [z for z in range(z + 1)]
    result_list = [[i, j, k] for i in first_list 
                                for j in second_list
                                    for k in third_list
                                        if sum([i, j, k]) != n]
    print(result_list)


###Find the Runner-Up Score!###

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    print (sorted(set(arr))[-2])


###Nested Lists###

if __name__ == '__main__':
    students=[]
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        students.append((name,score))
    for s in sorted([s for s,g in students if g==sorted(set([x[1] for x in students]))[1]]): 
        print(s)


###Finding the percentage###

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for key, value in student_marks.items():
            if query_name == key:
                sum = 0
                count = 0
                for i in value:
                    sum += i
                    count += 1
                average = sum/count
                print("{:.2f}".format(average))


###Lists###

if __name__ == '__main__':
    nums=[]
    N = int(input())
    
    for _ in range(N):
        split_list=input().split()
        if split_list[0] == 'print':
            print(nums)
            
        elif split_list[0] in ['sort','pop','reverse']:
            eval(f"nums.{split_list[0]}()")
            
        elif split_list[0] == 'insert':
            nums.insert(int(split_list[1]),int(split_list[2]))
            
        elif split_list[0] in ['remove','append']:
            eval(f"nums.{split_list[0]}({split_list[1]})")
