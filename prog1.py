#Prime number


n=int(input('Enter a number: '))
count=0
for i in range(1,n+1):
    if n%i == 0:
        count+=1
if n==1:
    print('prime')
elif count==2:
    print('prime')
else:
    print('not a prime')

count1=0
k=1
while k<=n:
    if n%k == 0:
        count1+=1
    k+=1

if count1<=2:
    print('prime')
else:
    print('not a prime')


#Even number in given range





for i in range(k,n+1):
    if i%2==0:
        print(i)


while k<=n:
    if k%2==0:
        print(k)
    k+=1

#printing even and odd in given range

while k<=n:
    if k%2==1:
        print(k, 'is odd')
    elif k%2==0:
        print(k, 'is even')
    k+=1

#no of digits in a number
l=int(input('Enter a number: '))
# s=len(l)
# print(s)
tem=l
count=0
while tem!=0:
    tem=tem//10
    count+=1
print('count of digits in a number',count)

#sum of digits of a number

temp=l
sum1=0
while temp!=0:
    re=temp%10
    temp=temp//10
    sum1+=re
print('sum of the digits',sum1)

#reverse a number

temp1=l
rev=0
while temp1!=0:
    mo=temp1%10
    rev=rev*10+mo
    temp1=temp1//10
print('reverse of the digits',rev)
if rev==l:
    print('palindrome')
else:
    print('not palindrome')