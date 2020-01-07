# def track_position(names):
#     dec={}
#     for i in range(len(name)):
#         dec[i]=name[i]
#     return dec

# name=['abc','abcdef','harshit']
# print(track_position(name))


name=['abc','abcde','abcdef']
for pos,name in enumerate(name):
    print(f"{pos}--------{name}")
    
