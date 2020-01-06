# def greater(num1,num2):
#     if num1>num2:
#         return num1
#     return num2

# def greatest(num2,num3):
#     if num2>num3:
#         return num2
#     return num3
    
# num1=int(input("Enter first_number"))
# num2=int(input("Enter second_number"))
# num3=int(input("Enter thired number"))
# print(greatest(greater(num1,num2),num3))

# def greater(num1,num2):
#     if num1 > num2:
#         return num1
#     return num2
# def greatest(num1,num2,num3):
#     if greater(num1,num2)>num3:
#         return greater(num1,num2)
#     return num3

# num1=int(input("Enter first number "))
# num2=int(input("Enter second number "))
# num3=int(input("Enter third number "))

# print(greatest(num1,num2,num3))

#scope

x=5 #global variable
def func():
    global x
    x=7
    return x

print(func())
print(x)




