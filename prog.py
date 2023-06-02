for i in range(1,11):
    print(i)
# print(/n)
n=1
while n<11:
    print(n)
    n+=1

for i in range(10,0,-1):
    print(i)

n = 10
while n>=1:
    print(n)
    n-=1


n = int(input('Enter a number: '))
if n>0:
    print('positive')
elif n==0:
    print('zero')
else:
    print('negative')


n=int(input('Enter a number: '))
l=[]
for i in range(0,n):
    l.append(int(input()))
print(l)

# number swapping

x=10
y=11
x,y=y,x
print(y)
print(x)

a=10
b=12
a=a+b
b=a-b
a=a-b
print(a)
print(b)

 #factorial of a number

n=int(input('enter a number:'))
x=1
fact=1
while n>=1:
    fact=fact*n
    n-=1
print(fact)

for i in range (1,n+1):
    fact=fact*i
print(fact)

# factors of a number

for i in range(1,n+1):
    if n%i==0:
        print(i)
while x<=n:
    if n%x==0:
        print(x)
    x+=1

#even or odd

n=int(input())
if n%2 == 0:
    print('even')
else:
    print('odd')