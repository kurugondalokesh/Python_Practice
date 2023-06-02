#program to print vowels and then consonants

# x=input('Enter a string: ')
# vow='aeiouAEIOU'
# l=''
# for i in x:
#     if vow.find(i)!=-1:
#         print(i)
#         l+=i
# for i in x:
#     if vow.find(i)==-1:
#         print(i)
#         l+=i
# print(l)
# v=''
# c=''

# for i in x:
#     if i in vow:
#         v+=i
#     else:
#         c+=i
# print(v+c)

# #program to reverse a given string
# y=input('Enter a string: ')
# rev=''
# i=len(y)-1
# while i>=0:
#     rev+=y[i]
#     i-=1
# print(rev)

# # using for loop to check palindrome or not

# rev1=''
# for i in range(len(y),0,-1):
#     rev1+=y[i-1]
# print(rev1)

# if rev1 == y:
#     print('Palindrome ')
# else:
#     print('not a palindrome')

# r = input("enter a nrm:")
# rum = ''
# for i in range(len(r),0,-1):
#     rum =rum + r[i-1]
# print(rum)

# count the number of repeating characters

# s=input('Enter a string: ')
# for i in s:
#     count=0
#     for j in s:
#         if i==j:
#             count+=1
#     print('{} count is {}'.format(i,count))



# x=int(input('Enter start: '))
y=int(input('Enter end: '))
s=0
for i in range(0,y+1,2):
    s=s+i
print(s)

#using while loop

j=0
sum1=0
while j<=y:
    sum1=sum1+j
    j=j+2
print(sum1)