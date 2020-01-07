# numbers=[1,2,3,4,5]
# print(min(numbers))
# print(max(numbers))

# def counte(names):
#     demo=[]
#     for i in name:
#         demo.append(len(i))
#     return demo

# name=['rajan','seema singh','anil']
# print(min(counte(name)))
# print(max(counte(name)))

# def func(item):
#     return len(item)

# name=['rajan','seema singh','anil','z']
# print(min(name,key=func))
# print(max(name,key=func))
# print(min(name,key=lambda item:len(item)))

student2=[
    {'name':'harshit','score':90,'age':24},
    {'name':'mohit','score':70,'age':19},
    {'name':'rohit','score':60,'age':25}
]
print(max(student2,key=lambda item:item.get('age'))['name'])