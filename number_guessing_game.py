import random
num=random.choice([1,4,8,10,3,15,9])
num1=int(input("Enter a number in [1,4,8,10,3,15,9]="))
print("number is "+str(num))
if num1==num:
    print("you win")
elif num1>num:
    print("number is to highi")
else:
    print("number is to low")