x=int(input('Enter a number: '))
temp=x
sum=0
while temp!=0:
    rem=temp%10
    sum+=rem
    temp=temp//100
print(sum)
sum1=0

# find the sum of even digits using the str typecasting
x=input('enter a number as string: ')
for i in range(0,len(x)):
    if i%2==1:
        sum1=sum1+int(x[i])
print(sum1)



#prog to find tha sum of the even digits using the count method


x=int(input('Enter a num: '))
tem=x
count=0
while tem!=0:
    count=count+1
    tem=tem//10
# print(count)

temp=x
sum1=0
if count%2==0:
    while temp!=0:
        rem=temp%10
        sum1+=rem
        temp=temp//100
    print(sum1)
else:
    c=1
    while temp!=0:
        rem=temp%10
        if c%2==0:
            sum1=sum1+rem
        temp=temp//10
        c=c+1
    print(sum1)


# prog to find sum of the odd and even digits

x=int(input("Enter a number: "))
temp=x
eve=0
rev=0
while temp!=0:
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10
c=1
while rev!=0:
    re=rev%10
    if c%2==0:
        eve=eve+re
    rev=rev//10
    c+=1
print(eve)
