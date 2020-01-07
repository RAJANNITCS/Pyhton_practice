# def square(a):
#     return a**2

# s=square
# print(s(5))
# print(s.__name__)
# print(square.__name__)
# print(s)
# print(square)

# def outer_fun():
#     def inner_fun():
#         print('inside inner func')
#     return inner_fun

# var =outer_fun()
# var()

# def outer_fun2(masg):
#     def inner_fun2():
#         print(f'mass is {masg}')
#     return inner_fun2

# var =outer_fun2("hi there !")
# var()

# def to_power(x):
#     def calc_power(n):
#         return n**x
#     return calc_power

# cube=to_power(3)
# print(cube(2))
from functools import wraps 
def decorator_function(any_function):
    @wraps(any_function)
    def wrappar_function(*args,**kwargs):
        '''this is wrappar_function'''
        print("this is awesome function")
        return any_function(*args,**kwargs)
    return wrappar_function

# @decorator_function
# def func1(a):
#     print(f"this is function {a}")
@decorator_function   
def add(a,b):
    '''this is add function'''
    return a+b
    
print(add(5,6))
# print(add.__doc__)

        
        
        
        
        
        
        
        
        