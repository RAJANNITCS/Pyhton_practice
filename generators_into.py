# def nums(n):
#     for i in range(1,n+1):
#         yield(i)

# for number in nums(10):
#     print(number)
import time
t1=time.time()
l=[i**2 for i in range(10000000)]
print(time.time()-t1)


# t1=time.time()
# g=(i**2 for i in range(100000000))
# print(time.time()-t1)