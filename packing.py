# a=10,20,30,40
# print(a)


#arbitary arguments packing

# def nums(*r):
#     return r
# s=nums(1,2,3,34,5,53)
# print(s)

#Note: a function can have only one parameter prefixed with star

#arbitary arguments after packing a dictionary
# def nu(**r):
#     return r
# re=nu(name='loki',roll=31)
# print(re)

#Note: a function can have only one parameter prefixed with double stars
#unpacking from a tuple

# a,b,c=(1,2,3)
# print(a)
# print(b)
# print(c)

#unpacking values using arbitary arguments

# *a,b,y=[1,2,4,4,65,67]
# print(a,b,y)

#swapping
# a=10
# b=20
# a,b=b,a
# print(a,b)


#unpacking from dictionary

dic={1:2,3:4,5:6}
a,b,c=dic.values()
print(a,b,c)