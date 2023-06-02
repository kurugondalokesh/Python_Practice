# r=float(input('Enter the area'))
# area=22/7*r*r
# print(area)

# first=input('enter first name: ')
# last=input('enter last name: ')
# name=first+' '+last
# print(name[::-1])


# en=input()
# en=en.split(',')
# print(en)
# print(tuple(en))

# dat='12,12,31'
# de=dat.replace(',','/')
# print(de)

# exam=(11,12,2031)
# print('the exam date is %i / %i / %i'%exam)

# import calendar
# mon=int(input('Enter tha month you want: '))
# year=int(input("Enter the year you want: "))
# print(calendar.month(year,mon))


# from datetime import date
# f_date=date(2014,7,2)
# l_date=date(2014,7,11)
# dela=l_date-f_date
# print(dela.days)

# date1=(2014,7,2)
# date2=(2014,8,22)
# ye=abs(date2[0]-date1[0])
# mo=date2[1]-date1[1]
# da=date2[2]-date1[2]
# days=ye*365+mo*31+da
# print(abs(days))

# rad=6
# volume=4/3*22/7*rad**3
# print(volume)

# n=int(input('enter a number: '))
# dif=n-17
# if n>17:
#     print(dif*2)

# for i in range(1500,2701):
#     if i%7==0 and i%5==0:
#         print(i)

# n=int(input('Enter a number: '))
# for i in range(0,10):
#     if i==n:
#         print('Well guessed')
#         break
#     else:
#         continue
    
# import random
# tn,gn=random.randint(1,10),0
# while tn!=gn:
#     gn=int(input('Enter a number to guess: '))
# print('Well guessed')


# li=[1,2,2.3,5+3j,(1,2),{1,3}]
# for i in li:
#     print('{} type is {}'.format(i,type(i)))

# rn=int(input('enter no of rows: '))
# cn=int(input("Enter no of cols: "))
# nl=[[0 for i in range(rn)] for j in range(cn)]
# print(nl)

# n='python.32.'
# lcount=0
# ncount=0
# ccount=0
# for i in n:
#     if i.isalpha():
#         lcount+=1
#     elif i.isnumeric():
#         ncount+=1
#     else:
#         ccount+=1
# print('letter count is ',lcount)
# print('num count is ',ncount)
# print('char count is ',ccount)


