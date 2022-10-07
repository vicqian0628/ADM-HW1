###Detect Floating Point Number###

import re
n = int(input())
for i in range(n):
    if re.match('^[+-]{0,1}[\d]{0,}\.\d+$', input()):
        print(True)
    else:
        print(False)
        

###Re.split()###

regex_pattern = r"[.,]"


###Group(), Groups() & Groupdict()###

import re
n = input()
pattern = re.compile(r"([\dA-Za-z])(?=\1)")
s = pattern.search(n)
if s:
	print(s.group(1))
else:
	print(-1)
  
 
###Re.findall() & Re.finditer()###

import re
string = input()
pattern = re.finditer(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])', string)
match = [i for i in map(lambda x: x.group(), pattern)]
if match != []:
    print(*match, sep='\n')
else: 
    print(-1)
    
    
###Re.start() & Re.end()###

import re

s=input()
k=input()

if (k not in s):
    print("(-1, -1)")
else:
    start_index=0
    while (len(s) > 0):
        m = re.search(f"({k})", s)
        if m:
            not_found=None
            print("(" + str(m.start()+start_index) + ", " + str(m.end()+start_index-1) + ")")
            start_index=start_index+m.start()+1
            s=s[m.start()+1:]
        else:
            break
            
            
###Regex Substitution###

import re

n = int(input().strip())

for i in range(n):
    line = input()
    while re.search(r"(\s&&\s)", line):
        line = re.sub(r"(\s&&\s)", " and ", line)
    while re.search(r"(\s\|\|\s)", line):
        line = re.sub(r"(\s\|\|\s)", " or ", line)
    print(line)
 
 
###Validating Roman Numerals###

regex_pattern = r"(M{0,3})(C[DM]|D?C{0,3})(X[LC]|L?X{0,3})(I[VX]|V?I{0,3})$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))


###Validating phone numbers###

import re

pat = r"^[789][0-9]{9}$"
for _ in range(int(input())):
    if re.search(pat, input()):
        print('YES')
    else:
        print('NO')
        
        
###Validating and Parsing Email Addresses###

import re

pattern = re.compile(r"<[a-z][a-zA-Z0-9\-\.\_]+\@[a-zA-Z]+\.[a-zA-Z]{1,3}>")


for a in range(int(input())):
    b = input().split()
    c = pattern.search(b[1])
    if c:
        print(b[0], c.string)
        
        
###Hex Color Code###

import re

pat = r"#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})"
for _ in range(int(input())):
    string = input()
    if not string or string[0] != "#":
        for s in string.split():
            try:
                result = re.search(pat, s)
                print(result.group())
            except AttributeError:
                pass
                
                
###HTML Parser - Part 1###

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for name,value in attrs:
            print(f"-> {name} > {value}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for name,value in attrs:
            print(f"-> {name} > {value}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")


parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())
parser.close()


###HTML Parser - Part 2###

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if data != '\n':
            if "\n" in data:
                print(">>> Multi-line Comment")
                print(data)
            else:
                print(">>> Single-line Comment")
                print(data)
    def handle_data(self, data):
        if not data == '\n':
            print(f">>> Data")
            print(data)
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()


###Detect HTML Tags, Attributes and Attribute Values###

from html.parser import HTMLParser
class CustomHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for ele in attrs:
            print("->", ele[0], ">", ele[1])


parser = CustomHtmlParser()
for _ in range(int(input())):
    parser.feed(input())
    
    
###Validating UID###

import re

t=int(input())

for _ in range(t):
    uid=input()
    if (uid.isalnum()) and (len(set(uid)) == 10) and \
        (re.match('(.*[A-Z].*){2}', uid) != None) and \
        (re.match('(.*[0-9].*){3}', uid) != None):
        print("Valid")
    else:
        print("Invalid")
        
        
###Validating Credit Card Numbers###

import re

N = int(input())
for _ in range(N):
    CCN = input()
		
    if re.fullmatch('[456]\d{3}(?:-?(\d){4}){3}', CCN):
        CCN = "".join(CCN.split('-'))
				
        if re.search(r'(\d)\1{3}', CCN):
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")
        
        
###Validating Postal Codes###

regex_integer_in_range = r"^[1-9]\d{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?=(\d).\1)"	# Do not delete 'r'.


###Matrix Script###

#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    
a = list(zip(*matrix))
string = ""

for i in range(len(a)):
    string += "".join(a[i])
pattern = re.compile(r"(?<=\w)[!@#$%& ]{1,}(?=\s*\w)")
new_string = re.sub(pattern," ",string)
print(new_string)
