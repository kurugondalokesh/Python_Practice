#find the sum of all digits in a list
x=[1,2,3,4,4,6,45,5]
sum=0
# for i in x:
#     sum=sum+i
# print(sum)
# y=0
# while y<len(x):
#     sum=sum+x[y]
#     y+=1
# print(sum)

# find the sum of only even numbers in a list
# x=[1,2,4,5,6,7]
# sum=0
# for i in x:
#     if i%2==0:
#         sum=sum+i
# print(sum)

# j=0
# while j<len(x):
#     if x[j]%2==0:
#         sum=sum+x[j]
#     j+=1
# print(sum)

#to find the average value in a list
# x=[1,2,3,4,5]
# sum=0
# for i in x:
#     sum+=i
# avg=sum/len(x)
# print(avg)

# i=0
# while i<len(x):
#     sum=sum+x[i]
#     i+=1
# avg=sum/len(x)
# print(avg)


#find the max number in a list
# x=[0,1,2,43,53,2,67,68]
# max=x[0]
# for i in x:
#     if i>max:
#         max=i
# print(max)

# i=0
# while i<len(x):
#     if x[i]>max:
#         max=x[i]
#     i+=1
# print(max)


#find the 2nd maximum number in a given list
# x=[13,24,53,2]
# x.sort()
# print('2nd highest',x[-2])
# print('2nd lowest',x[1])


#program to reverse a list


# lis=[1,2,3,21,2]
# rev=[]
# for i in lis:
#     rev=[i]+rev
# print(rev)

# to find the prime number in a list

# l=[1,2,3,4,5,6,7]
# for i in l:
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(i,'is prime')

#sum of maximum and minimum


# li=[22,2,1,445,5,3,]
# ma=x[0]
# mi=x[0]
# i=0
# while i<len(li):
#     if li[i]>ma:
#         ma=li[i]
#     if li[i]<mi:
#         mi=li[i]
#     i+=1
# print(ma+mi)

# for i in range(0,11):
#     if i%3==0:
#         continue
#     print(i)

def fun(v,*y):
    print(y,v)
fun(12321,1,4,33,4311433,4)