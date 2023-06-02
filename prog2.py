x=int(input('Enter start: '))
y=int(input('Enter end: '))
for i in range(x,y+1):
    count=0
    a=1
    while a<=i:
        if i%a==0:
            count+=1
        a+=1
    if count==2:
        print(i,' is prime')
    
# while i upper loop

while x<=y:
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count+=1
    # x+=1
    if count==2:
        print(x,'is prime')
    x+=1

#using for loop
for i in range(x,y+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i,'is prime')
