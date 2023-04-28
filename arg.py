# wap to understand arguments.
'''
# positional argument

def func(a,b):
    print(a+b+c+d)
func(10,15)


# keyword argument

def func(a,b):
    print(a+b+c+d)
func(b=15,a=14)

# default argument

def func(a,b,c=0,d=0):
    print(a+b+c+d)
func(10,b=15,c=14)

# variable leangth argument

# packing

def func(*a):
    print(a)
func(10,15,14,1)
'''
# unpacking

p=(10,20,30,40)
def func(a,b,c,d):
    print(a,b,c,d)
    print(a+b+c+d)
func(*p)

