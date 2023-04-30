
n=int(input('Enter a number:'))
sum=0
z=n
l=len(str(n))
while n>0:
    a=n%10
    c=a**l
    sum=sum+c
    n=n//10
print(sum)
if z==sum:
    print('Armstrong')
else:
    print('not an armstrong')
