#function 

# # name ='rajan singh'
# # print(len(name))

# def add(a,b):#formal argument
#     return a+b

# print(add(2,3))#actual argument

# first_name=input("Enter first name")
# second_name=input("Second name")
# print(add(first_name,second_name))

# #function practice
# def last(name):
#     return name[-1]

# print(last("rohan"))

# def odd_even(number):
#     if number%2==0:
#         print("Even")
#     else:
#         print("odd")

# def odd_even1(number):
#     return "even" if number%2==0 else "odd" 
# print(odd_even1(44))

# def is_even(num):
#     return num%2==0

# print(is_even(5))

# def maxed(num1,num2):
#     if num1>num2:
#         return num1
#     return num2

# num1=int(input("Enter first_number"))
# num2=int(input("second number"))
# print(maxed(num1,num2))

# def maxxed(num1,num2,num3):
#     if num1>num2 and num1>num3:
#         return num1
#     elif num2>num1 and num2>num3:
#         return num2
#     return num3
# num1=int(input("Enter number 1="))
# num2=int(input("Enter number 2="))
# num3=int(input("Enter number 3="))

# print(maxxed(num1,num2,num3))

def greater(num1,num2):
    if num1>num2:
        return num1
    return num2

def greatest(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num3 and num2>num1:
        return num2
    return num3

num1=int(input("Enter first_number"))
num2=int(input("Enter second_number"))
num3=int(input("Enter thired number"))
print(greatest(greater(num1,num2),num3)