# n=int(input('Enter a number: '))


# p=int(input('Enter power of a number: '))
# print('square of a number : ',n*n)
# print('square root of a number is : ',n**0.5)
# power=n**p
# print('{} power of {} is {}'.format(p,n,power))
# dic={'name':'loki','no':21,'place':'naidupet'}
# st=input('enter a key to find: ')
# if st in dic.keys():
#     print('present')
# else:
#     print('not present')
# dic1={i:i**2 for i in range(1,n+1)}
# print(dic1)
# l1=[1,2,3,4]
# l2=[5,6,7,8]
# dic={}
# for ke,val in map(l1,l2):
#     dic[ke]=val
# print(dic)
# dic2={'name1':'pandu','place1':'tpt'}
# dic.update(dic2)
# print(dic)
# rm=dic.pop('no')
# print(dic)
# dic2={1:10,2:30}
# sumk=0
# sumv=0
# for i in dic2.keys():
#     sumk=sumk+i
# for j in dic2.values():
#     sumv=sumv+j

# for i,j in dic2.items():
#     sumk=sumk+i
#     sumv=sumv+j
# print('sum of keys ',sumk)
# print('sum of values ',sumv)

#mapping in dictionary

# l1=[1,2,3,4,5]
# l2=[6,7,8,9,0]
# dic=dict(zip(l1,l2))
# print(dic)
# res={l1[i]:l2[i] for i in range(len(l1))}
# print(res)

#closures
# def npower(exponent):
#     x=10
#     def poe(num):
#         print(x)
#         return (pow(num,exponent))
#     return poe
# square=npower(2)
# print(square(2))

#python example to access the indexand the values in a list

li=[1,2,3,4,5,6,7]
for i in range(len(li)):
    print(f'{i} value is {li[i]}')
