# #decision statements
# #if
# name1 = 'Hemanth'
# if name1 == 'Hemanth':
#     print('hemanth')
# else:
#     print('kadhu')
# #elif
# name=input('enter a name:')
# if name=='hemanth':
#     print('yedhava')
# elif name =='yedhava':
#     print('pedda yedhava')
# else:
#     print('gorre')

# #nested if
# peru=input('enter peru :')
# if peru =='lokesh':
#     if clas =='python':
#         print('in python class')
#     else:
#         print('not in class')
# else:
#     print('evarra meerantha')
# #Pass keyword
# #It is used to skip the statement
# if 10>20:
#     pass 
# else:
#     print('Not greater')

# #for loop using collections
# #List in for
# for i in [1,2,3]:
#     print(i)
# #String in for
# for i in 'Hemanth edhava':
#     print(i)
# #Set in for
# for i in {2,3,4,32}:
#     print(i)
# #Dictionary in for
# d = {1 : 2, 'name':'hemanth','quality':'yedhava'}
# for i in d:
#     print(i)

# #Range method
# #Range function is used to print or fetch a range of numbers
# for i in range(11):
#     print(i)
# #Range with start index
# for i in range(1,11):
#     print(i)
# #Range with start index and skip 
# for i in range(1,11,2):
#     print(i)

# x=1
# while x < 6:
#     # print('While is executed')
#     print(x)
    # x+=1
factorial=1
x=5
while x>=1:
    factorial=factorial*x
    x-=1
print(factorial)