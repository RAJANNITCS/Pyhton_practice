# def all_total(*args):
#     total=0
#     for i in args:
#         total+=i
#     return total
        

# print(all_total(2,3,4,5,6))

# def multiply(num1,*args):
#     total=1
#     print(num1)
#     for i in args:
#         total*=i
#     return total
# multiply_num=[1,2,3,4,5]
# print(multiply(*multiply_num))

def squrar(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return "you did not pass any args"


num=int(input("enter number"))
num_list=[2,3,4,5]
print(num)
print(num_list)
print(squrar(num,*num_list))