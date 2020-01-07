number1=[2,4,6,8,10]
number2=[1,2,3,4,5,6]

# def is_even(number):
#     num_list=[]
#     for i in number:
#         if i%2==0:
#             num_list.append(True)
#     return num_list

# num1=all(is_even(number1))
# print(num1)

num1=any([i%2==0 for i in number2])
print(num1)