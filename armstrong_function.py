'''
def armstrong(a):
    for i in str(a):
        sum=sum+i**len(str(a))
    return sum
a= int(input("Enter a no:"))
if armstrong(a)==a:
    print('armstrong')
else:
    print('Not armstong')
'''
def armstrong(a):
    sum=0
    for i in str(a):
        sum=sum+int(i)**len(str(a))
    return sum
def series(m,n):
    for i in range(m,n+1):
        if armstrong(i)==i:
            print(i)
series(1,1000)