##function that takes two arguments and return the sum

# def sum(a,b):
#     return a+b
# re=sum(5,67)
# print(re)

#function that accepts two arguments and find biggest of two numbers

# def max(a,b):
#     if a>b:
#         return (a,'is biggest')
#     else:
#         return (b,'is bigger')
# re=max(2372,4322)
# print(re)

#function that prints the numbers in the given range

# def rang(a,b):
#     # for i in range(a,b+1):
#     #     print(i)
#     while a<=b:
#         print(a)
#         a+=1
# rang(1,10)

#closures 
def outer():
    def inner():
        return 'hello world'
    return inner
res=outer()

