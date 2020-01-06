import random
num2=0
num=random.choice([1,4,8,10,3,15,9])
while 1:
    num1=int(input("Enter a number in [1,4,8,10,3,15,9]="))
    print("number is "+str(num))
    num2+=1
    if num1==num:
        print("you win")
        print(f"and you guessed this number in {num2} time")
        break
    elif num1>num:
        print("number is to highi")
    else:
        print("number is to low")