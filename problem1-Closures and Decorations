###Standardize Mobile Number Using Decorators###

def wrapper(f):
    def fun(l):
        # complete the function
        f([f"+91 {i[-10:-5]} {i[-5:]}" for i in l])
    return fun
    
    
###Decorators 2 - Name Directory###

import operator

def person_lister(f):
    def inner(people):
        # complete the function
        people.sort(key=lambda x: int(x[2]))
        return [f(person) for person in people]
    return inner
