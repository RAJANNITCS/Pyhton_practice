# num1=[]
# for i in range(1,11):
#     num1.append(i**2)
# print(num1)

# num2=[i**2 for i in range(1,11)]
# print(num2)

# number=[-i for i in range(1,11)]
# print(number)

# names=['rajan','seema','mohan']
# new_list=[i[0] for i in names]
# print(new_list)

# words_list=['abc','tuv','xyz']
# new_list=[i[::-1] for i in words_list]
# print(new_list)

# numbers=list(range(1,11))
# new_list=[i for i in numbers if i %2 ==0]
# new_list1=[i for i in numbers if i %2 != 0]
# print(new_list1)

# nums=list(range(1,11))
# new_list=[i*2 if (i%2==0)else -i for i in nums]
# print(new_list)

nested_comp=[[i for i in range(3)] for i in range(1,4)]
print(nested_comp)

