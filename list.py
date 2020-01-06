# numbers=[1,2,3,4,5,6,7]
# # print(numbers)
# # for i in numbers:
# #     print(i)
    
# words=['rajan',1,3.4,'r','allahabad']
# print(words)
# print(words[0])
# print(words[1:4])
# print(words[1:4:2])
# print(words[::-1])
# words[4]="mohan"
# # for i in words:
# #     print(i)
# # for i in range(len(words)):
# #     print(words[i])
# print(words)
# # print(words+numbers)

# frouits=['graps','apple']
# name=['rajan','seema','rohit']
# frouits.append('mango')
# frouits.append('gwava')
# frouits.insert(1,"potato")
# frouits.insert(2,'rajan')
# # print(frouits+name)
# frouits.extend(name)
# print(frouits)
# print(name)

# frouits.append(name)
# print(frouits)
# name=['rajan','seema','rohit','mohit','manish','seema']
# name.pop()
# name.pop(1)
# first_name=name.pop(1)
# print(first_name)
# del name[1]
# name.remove('seema')
# print(name)

# if 'seema' in name:
# #     print("seema is present")

# name=['rajan','seema','rohit','ravi','rajan']

# print(name.count("rajan"))
# name.sort()
# print(name)

# numbers=[34,65,1,3,9,4,7,2,6,8,9,3]
# # # numbers.sort()
# # print(sorted(numbers))
# # print(numbers)
# # numbers.clear()
# # print(numbers)
# # numbers_copy=numbers.copy()
# print(numbers_copy)

# number=[1,2,3,5,6,8,9]
# number1=[1,2,3,5,6,8,9]
# # if number1 is number1:
# #     print('same')
# # if number1 == number:
# #     print('same')
# print(number1==number) #check value
# print(number is number1) #check memory place

# user_info='rajan 24'
# name=user_info.split()
# # print(user_info.split(" "))
# print(name)
# user_info='rajan 24'.split()
# print(user_info)
# name,age=input("Enter name and age").split(",")
# print(name)
# print(age)
# user_info=['rajan , 24']
# # print(','.join(user_info))
# info=','.join(user_info)
# print(type(info))
# print(info)

# s='string'

# t=s.title()
# print(t)


# l=['word1','word2','word3','words4']
# l.pop()
# l.append('rajan')
# print(l)

# name=['rajan','seema','mohan','sohan','ravi']
# for i in name:
#     print(i)
# for i in range(len(name)):
#     print(name[i])
    
# i=0
# while i<len(name):
#     print(name[i])
#     i+=1

# list1=[1,2,3,4]
# list2=[5,6,7,8]
# list3=[9,10,11,12]
# # list1.append(list2)
# # list1.append(list3)
# list4=list1+list2+list3
# print(list4)
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# print(matrix[0][1])
# for i in matrix:
#     for j in i:
#         print(j)

# numbers=list(range(1,11))

# print(numbers)

# # num1=numbers.pop()
# # print(num1)

# print(numbers.index(5))
# print(numbers.index(5,6))
# print(numbers.index(5,6,8))


# def negative_list(lists):
#     neg=[]
#     for i in lists:
#         neg.append(-i)
#     return neg

# print(negative_list(numbers))


# def squer(lists):
#     sqr=[]
#     for i in lists:
#         sqr.append(i*i)
#     return sqr

# print(squer(numbers))

# def revers_1(lists):
#      lists.reverse()
#      return lists
# def revers_1(lists):
#     return lists[::-1]

# def revers_1(lists):
#     li=[]
#     for i in range(len(lists)):
#         li.append(lists.pop())
#     return li
# numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]       
# print(revers_1(numbers))

# words=['abc','tuv','xyz']
# def reverse1(words):
#     lists=[]
#     for i in words:
#         lists.append(i[::-1])
#     return lists
# print(reverse1(words))

# numbers=list(range(1,21))
# def filter_odd_even(numbers):
#     even_list=[]
#     odd_list=[]
#     sum_list=[]
#     for i in numbers:
#         if i %2==0:
#             even_list.append(i)
#         else:
#             odd_list.append(i)
#     sum_list.append(even_list)
#     sum_list.append(odd_list)
#     return sum_list

# print(filter_odd_even(numbers))

# def filter_list(num_list1,num_list2):
#     output=[]
#     for i in num_list1:
#         if i in num_list2:
#             output.append(i)
#     return output
    
# num_list1=[1,2,5,8]
# num_list2=[1,2,7,6]
# print(filter_list(num_list1,num_list2))

# def defference(num_list):
#     output=max(num_list)-min(num_list)
#     return output

# num_list=[3,8,9,12,2,5,7]
# print(min(num_list))
# print(max(num_list))
# # print(defference(num_list))

# def count_list(num_list):
#     list_count=0
#     for i in num_list:
#         if type(i)==list:
#             list_count+=1
#     return list_count
        
        
# num_list=[1,2,3,[1,2],[3,4],[]]
# print(count_list(num_list))

