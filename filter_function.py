def is_even(a):
    if a%2==0:
        return a

num=list(range(1,11))
num1=list(map(is_even,num))
num2=list(filter(is_even,num))
num3=list(filter(lambda a: a%2==0,num))
print(num1)
print(num2)
print(num3)