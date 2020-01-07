# square={num:num**2 for num in range(1,11)}
# print(square)

# square1={f"Square of {num} is":num**2 for num in range(1,11)}

# for key ,value in square1.items():
#     print(f"key is {key} and value is {value}")
    

num='rajan singh'
countes={i:num.count(i) for i in num}
print(countes)

odd_even={i:('even' if i%2==0 else 'odd')for i in range(1,11)}
print(odd_even)
  