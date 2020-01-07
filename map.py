numbers=[1,2,3,4,5]
def square(a):
    return a**2
# squ1=[]
# for i in numbers:
#      squ1.append(square(i))
# print(squ1)

# squ2=list(map(square,numbers))
squ2=list(map(lambda a:a**2,numbers))
print(squ2)

