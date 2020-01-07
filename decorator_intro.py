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
# # print(cube(2))
# from functools import wraps 
# def decorator_function(any_function):
#     @wraps(any_function)
#     def wrappar_function(*args,**kwargs):
#         '''this is wrappar_function'''
#         print("this is awesome function")
#         return any_function(*args,**kwargs)
#     return wrappar_function

# # @decorator_function
# # def func1(a):
# #     print(f"this is function {a}")
# @decorator_function   
# def add(a,b):
#     '''this is add function'''
#     return a+b
    
# print(add(5,6))
# # print(add.__doc__)
# from functools import wraps
# def print_function_data(functon):
#     @wraps(functon)
#     def wrappar_function(*args,**kwargs):
#         print(f"you are calling {functon.__name__}")
#         print(f"{functon.__doc__}")
#         return functon(*args,**kwargs)
#     return wrappar_function

# @print_function_data
# def add(a,b):
#     '''This function takes two number as agrument and return their sum'''
#     return a+b

# print(add(5,7))
# from functools import wraps
# def only_int_allow(function):
#     @wraps(function)
#     def wrappar_function(*args,**kwargs):
#         data_types=[]
#         for arg in args:
#             data_types.append(type(arg)==int)
#         if all(data_types):
#             return function(*args,**kwargs)
#         else:
#             print("invalid argument")
#     return wrappar_function

# @only_int_allow
# def add_all(*args):
#     total=0
#     for i in args:
#         total+=i
#     return total

# print(add_all(1,2,3,4,5,[1,1,2,]))
        
from functools import wraps

def only_int_allow(data_type):
    def decorator(function):
        @wraps(function)
        def wrappar(*args,**kwargs):
            if all([type(arg)==data_type for arg in args]):
                return function(*args,**kwargs)
            print("invalid argument")
        return wrappar
    return decorator

@only_int_allow(str)
def string_join(*args):
    string=''
    for i in args:
        string+=i
    return string
        
print(string_join('rajan','singh'))
        
        
        