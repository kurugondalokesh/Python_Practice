#print  1 2 3 4 5 
        # 2 4 6 8 10
        # 3 6 9 12 15
        # 4 8 12 16 20
        # 5 10 15 20 25

# for i in range(1,6):
#     for j in range(1,6):
#         print(i*j,end=' ')
#     print()

# i=1
# while i<=5:
#     j=1
#     while j<=5:
#         print(i*j,end=' ')
#         j+=1
#     i+=1
#     print()


#print 1 2 4 8 16
#      2 4 8 16 32
#      4 8 16 32 64
# for i in range(3):
#     if i==0:
#         value=1
#     elif i==1:
#         value=2
#     else:
#         value=4
#     for j in range(5):
#         print(value,end=' ')
#         value*=2
#     print( )

#print    A B C D E 
        # F G H I J
        # K L M N O
        # P Q R S T
        # U V W X Y


# print(ord('A'))
# inc=0
# i=1
# while i<=5:
#     j=1
#     while j<=5:
#         print(chr(65+inc),end=' ')
#         j+=1
#         inc+=1
#     i+=1
#     print()
# print( )
# im=0
# for i in range(5):
#     for j in range(5):
#         print(chr(65+im),end=' ')
#         im+=1
#     print()


# print
# 1 2 3 4 5
# A B C D E
# 6 7 8 9 10
# F G H I J
# 11 12 13 14 15
# k=1
# l=0
# for i in range(5):
#     for j in range(5):
#         if i%2==0:
#             print(k,end=' ')
#             k+=1
#         else:
#             print(chr(65+l),end=' ')
#             l+=1
#     print()

# def par(m,n):
#     val=1
#     alpha='A'
#     for i in range(m):
#         for j in range(n):
#             if i%2==0:
#                 print(val,end=' ')
#                 val+=1
#             else:
#                 if 'A' <= alpha <= 'Z':
#                     print(alpha,end=' ')
#                     alpha=chr(ord(alpha)+1)
#                 else:
#                     alpha='A'
#                     print(alpha,end=' ')
#                     alpha=chr(ord(alpha)+1)                   
#         print()
# par(10,10)

# def fnc(m,n):
#     value=1
#     alpha='A'
#     for i in range(m):
#         for j in range(n):
#             if i%2==0:
#                 print(value,end=' ')
#                 value+=1
#                 if value>=9:
#                     value=1
#             else:
#                 print(alpha,end=' ')
#                 alpha=chr(ord(alpha)+1)
#                 if ord(alpha)>=78:
#                     alpha='A'
#         print()
# fnc(7,7)

# def fn(m,n):
#     value=1
#     alpha='A'
#     for i in range(m):
#         for j in range(n):
#             if i%2==0:
#                 print(value,end=' ')
#                 value+=1
#                 if value>=9:
#                      value=1
#             else:
#                 if ord(alpha)%2==0:
#                     print(alpha,end=' ')
#                 alpha=chr(ord(alpha)+1)
#         print()
# fn(6,6)
# print(ord('#'))
# value=1

# for i in range(3):
#     for j in range(3):
#         if i==0 and j==0:
#             print('@',end=' ')
#         elif i==0 and j==1:
#             print('!',end=' ')
#         elif i==2 and j==2:
#             print('#',end=' ')
#         else:
#             print(value,end=' ')
#             value+=1
#     print()

# value=1
# for i in range(3):
#     for j in range(3):
#         if i==0 and j==2:
#             print('!',end=' ')
#         elif i==0:
#             print('@',end=' ')
#         elif i==2 and j==2:
#             print('@',end=' ')
#         elif i==2 and j==1:
#             print('!',end=' ')
#         else:
#             print(value,end=' ')
#             value+=1
#     print()

# value=1
# for i in range(5):
#     if i==1:
#         alpha='A'
#     else:
#         alpha='a'
#     for j in range(5):
#         if i==0 and j==0:
#             print('!',end=' ')
#         elif i==0 and j==1:
#             print('@',end=' ')
#         elif i==2 and j==2:
#             print('#',end=' ')
#         elif i==2 and j==3:
#             print('$',end=' ')
#         elif i==4 and j==0:
#             print('?',end=' ')
#         elif i==4 and j==1:
#             print('+',end=' ')
#         elif i==4 and j==2:
#             print('-',end=' ')
#         elif i%2==1:
#             print(alpha,end=' ')
#             alpha=chr(ord(alpha)+1)
#         else:
#             print(value,end=' ')
#             value+=1
#     print()
                


# @ @ ! !
# # # @ @
# # # @ @
# ! ! ! @

# for i in range(4):
#     for j in range(4):
#         if (i==0 and j<2) or (i==1 and j>1) or (i==2 and j>1) or (i==3 and j==3):
#             print('@',end=' ')
#         elif j<2 and (i==1 or i==2):
#             print('#',end=' ')
#         else:
#             print('!',end=' ')
#     print()

# + + + =
# + + + +
# + - + -
# + - + -
# for i in range(4):
#     for j in range(4):
#         if i==0 and j==3:
#             print('=',end=' ')
#         elif i>1:
#             if j%2==1:
#                 print('-',end=' ')
#             else:
#                 print('+',end=' ')
#         else:
#             print('+',end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()

# for i in range(5):
#     for j in range(5):
#         if i<=j:
#             print('*',end=' ')
#     print()

# a
# b c
# d e f 
# g h i j 
# k l m n o 

# al='a'
# for i in range(6):
#     for i in range(1,i+1):
#         print(al,end=' ')
#         al=chr(ord(al)+1)
#     print()

# 10 9 8 7 6
#  5 4 3 2 
#  1 10 9
#  8 7
#  6

# value=10
# for i in range(5):
#     for j in range(5):
#         if i<=j:
#             print(value,end=' ')
#             value-=1
#             if value<1:
#                 value=10
#     print()


#         *
#       * *
#     * * *
#   * * * *
# * * * * *
# k=4
# for i in range(1,6):
#         print(k*'  ',end=' ')
#         k-=1
#         for j in range(1,i+1):
#                 print('*',end=' ')
#         print()

# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# for i in range(5):
#     for k in range(i):
#             print('  ',end='')
#     for j in range(5):
#           if i<=j:
#               print('*',end=' ')
#     print()


#     * 
#   * *
# * * *

# k=2
# for i in range(1,4):
#     print(k*'  ',end=' ')
#     k-=1
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()
        
# n=3
# st=1
# for i in range(n,0,-1):
#     h=i-1
#     for sp in range (h):
#         print(' ',end=' ')
#     for j in range(st):
#         print('*',end=' ')
#     st+=1
#     print()

# def pat(n):
#     star=1
#     space=n-1
#     for i in range(n):
#         for k in range(space):
#             print(end=' ')
#         for j in range(star):
#             print(end='*')
#         star+=1
#         space-=1
#         print()
# pat(6)

# * 
# * *
# * * *
# * * * *
# * * *
# * *
# *


# for i in range(1,8):
#     if i<=4:
#         for j in range(1,i+1):
#             print('*',end=' ')
#     else:
#         for j in range(8-i):
#             print('*',end=' ')
#     print()


# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13
# 14 15
# 16

# value=1
# for i in range(1,8):
#     if i<=4:
#         for j in range(1,i+1):
#             print(value,end=' ')
#             value+=1
#     else:
#         for j in range(8-i):
#             print(value,end=' ')
#             value+=1
#     print()

# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3
# 1 2
# 1

for i in range(1,8):
    value=1
    if i<=4:
        for j in range(1,i+1):
            print(value,end=' ')
            value+=1
    else:
        for j in range(8-i):
            print(value,end=' ')
            value+=1
    print()
            