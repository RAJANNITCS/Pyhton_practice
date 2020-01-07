def fun(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")
    
    

# fun('mohit',name='rajan',age=24)
user1={'name':'rajan','age':24}
fun(**user1)