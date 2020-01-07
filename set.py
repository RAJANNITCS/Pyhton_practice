# s={1,2,3,4,5,2,3}

# print(s)

# l=[1,2,3,4,5,5,5,3,2,1]
# s=set(l)
# print(s)
# l=s
# print(l)

# s={1,2,3,4}
# s.add(5)
# s.add(6)
# s.add(5)
# # s.remove(7)
# s.discard(7)
# # s.clear()
# s1=s.copy()
# print(s1)

# if 2 in s:
# #     print('present')
# for i in s:
#     print(i)
s1={1,2,3,4,5}
s2={3,4,5,6,1}

union_set=s1 | s2
print(union_set)

intersection=s1 & s2
print(intersection)