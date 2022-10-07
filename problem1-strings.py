###sWAP cASE###

def swap_case(s):
    return s.swapcase()


###String Split and Join###

def split_and_join(line):
    # write your code here
    words = line.split(' ')
    return ('-'.join(words))
    
    
###What's Your Name?###

def print_full_name(first, last):
    # Write your code here
    print("Hello " + first + " " + last + "! You just delved into python.")
    

###Mutations###

def mutate_string(string, position, character):
    
    return(string[:position] + character + string[(position+1):])


###Find a string###

def count_substring(string, sub_string):
    
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    
    return count


###Sring Validators###

if __name__ == '__main__':
    s = input()
    
    print(any(x.isalnum() for x in s))
    print(any(x.isalpha() for x in s))
    print(any(x.isdigit() for x in s))
    print(any(x.islower() for x in s))
    print(any(x.isupper() for x in s))    


###Text Alignment###

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


###Text Wrap###

def wrap(string, max_width):
    
    return(textwrap.fill(string,max_width))


###Designer Door Mat###

# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int,input().split())
for i in range(1,N,2): 
    print((i * ".|.").center(M, "-"))
print("WELCOME".center(M,"-"))
for i in range(N-2,-1,-2): 
    print((i * ".|.").center(M, "-"))


###String Formatting###

def print_formatted(number):
    # your code goes here
    count = 1
    x = len(bin(number)[2:])
    while (count <= number):
        oc = oct(count)[2:]
        he = hex(count).upper()[2:]
        bi = bin(count)[2:]
        print(str(count).rjust(x), oc.rjust(x), he.rjust(x), bi.rjust(x))
        count+=1
  

###Alphabet Rangoli###

def print_rangoli(size):
    # your code goes here
    N = size
    num_dashes = (N - 1)*2
    high_char = chr(N + 96)
    alpha_str = high_char
    cached_lines = []
    for i in range(0, num_dashes + 1, 2):
        new_str = '-'*(num_dashes - i) + alpha_str + '-'*(num_dashes-i)
        cached_lines.append(new_str)
        print(new_str)
        alpha_str = alpha_str[:len(alpha_str)//2 + 1] + '-' + chr(ord(alpha_str             [len(alpha_str)//2]) - 1) + '-' + alpha_str[len(alpha_str)//2:]
    for i in range(len(cached_lines)-2, -1, -1):
        print(cached_lines[i])
    

###Capitalize!###

# Complete the solve function below.
def solve(s):
    s = s.split(" ")
    return(" ".join(i.capitalize() for i in s))
    
    
###The Minion Game###

def minion_game(string):
    # your code goes here
    vowel =['A','E','I','O','U']
    S=0
    K=0
    for i in range(len(string)):
        if string[i] in vowel:
            K+= len(string)-i
        else:
            S+=len(string)-i
    if S>K:
        print("Stuart"+" "+ "%d" % S)
    elif K>S:
        print("Kevin"+" "+'%d' % K)
    else:
        print("Draw")
    

###Merge the Tools!###

def merge_the_tools(string, k):
    # your code goes here
    for part in zip(*[iter(string)] * k):
        d = dict()
        print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))

