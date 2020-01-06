# # user1=dict(name='rajan',age=24)
# # print(user1)

# # user={'name':"rajan",'age':24}
# # print(user)
# # print(user["name"])
# # print(user["age"]) 

# user1={"name":'rajan',
#        'age':24,
#        "fav":['colo','kimi no na wa'],
#        'fav_tunes':['awakening','fairy tale']
#        }

# print(user1['fav'])
# print(user1['name'])

# users={
#     user1={"name":'rajan',
#        'age':24,
#        "fav":['colo','kimi no na wa'],
#        'fav_tunes':['awakening','fairy tale']
#        },
#     user1={"name":'rajan',
#        'age':24,
#        "fav":['colo','kimi no na wa'],
#        'fav_tunes':['awakening','fairy tale']
#        }
# }

# user_info={
    
# }

# user_info["name"]='rajan'
# user_info['age']=24
# print(user_info)



# user1={"name":'rajan',
#        'age':24,
#        "fav":['colo','kimi no na wa'],
#        'fav_tunes':['awakening','fairy tale']
#        }

# if 'name' in user1:
#     print('present')
# if 'age' in user1:
#     print('present')
    
# if 'rajan' in user1.values():
#     print('present')
# if 24 in user1.values():
#     print('present')
# if ['colo','kimi no na wa'] in user1.values():
#     print('present')

#loop in dictionaries
# for i in user1:
#     print(i)
# for i in user1.values():
# #     print(i)

# user_info_values=user1.values()
# print(user_info_values)

# for i in user1.keys():
#     print(i)
# for i in user1:
# #     print(i)
# user_info_key=user1.keys()
# print(type(user_info_key))
# print(user_info_key)
# for i in user1:
#     print(user1[i])
# user_items=user1.items()
# print(type(user_items))
# print(user_items)
# dict_items([('name', 'rajan'), ('age', 24), ('fav', ['colo', 'kimi no na wa']), ('fav_tunes', 
# ['awakening', 'fairy tale'])])

# for key,value in user1.items():
# #     print(f"key is {key} and value is {value}")
# for i in user1.items():
#     print(i)


# user1={"name":'rajan',
#        'age':24,
#        "fav":['colo','kimi no na wa'],
#        'fav_tunes':['awakening','fairy tale']
#        }

# user1['fav_song']=['song1','song2']
# print(user1)

# pop_item=user1.pop('fav_tunes')
# print(type(pop_item))
# print(user1)
# popped_item=user1.popitem()
# print(type(popped_item))
# # print(popped_item)
# more_info={'name':"rajan",'state':'uttar pradesh','hobbies':['coding','reading','guitar']}
# user1.update(more_info)
# print(user1)

# user1={"name":'rajan',
#        'age':24,
#        "fav":['colo','kimi no na wa'],
#        'fav_tunes':['awakening','fairy tale']
#        }

# # d={'name':'unknown','age':'unknown'}
# # d=dict.fromkeys(['name','age','height'],'unknown')
# # d=dict.fromkeys(('name','age','height'),'unknown')
# d=dict.fromkeys((range(1,11)),'unknown')

# print(d)
# user1={"name":'rajan',
#        'age':24,
#        "fav":['colo','kimi no na wa'],
#        'fav_tunes':['awakening','fairy tale']
#        }

# # print(user1['name'])
# print(user1.get('name'))

# if user1.get('name'):
#     print('present')
# else:
#     print('not present')

# user1.clear()
# d1=user1.copy()
# print(user1)

# user={'name':'rajan','age':32,'age':24}
# print(user.get('fav','not found'))
# print(user)

# def squer(num1):
#     dic={}
#     for i in range(1,num1+1):
#         dic[i]=i**3
#     return dic

# print(squer(10))

# dic={}
# dic['name']='rajan'
# print(dic)

# def world_count(string):
#     dic={}
#     for i in string:
#         dic[i]=string.count(i)
#     return dic

# print(world_count('rajan singh'))

# user={
#     'name':'rajan',
#     'age':24,
#     'fav_movies':['coco','avengers']
#     'fav_song':['song1','song2']
# }

# user={}
# name=input('Enter your name ')
# age=input("what is your age ")
# fav_movies=input('your fav movies seprated by ,').split(",")
# fav_songs=input("your fav songs separated by ,").split(",")
# user['name']=name
# user['age']=age
# user['fav_movies']=fav_movies
# user['fav_songs']=fav_songs
# print(user)
# for key ,value in user.items():
#     print(f'key is {key} and value is{value}')

my_dic={}
name=input("Enter your name")
age=int(input("Enter your age"))
fav_movies=input("Enter fav movies sepreted by ,").split(',')
fav_song=input("Enter fav song sepreted by , ").split(',')
my_dic['name']=name
my_dic['age']=age
my_dic['fav_movies']=fav_movies
my_dic['fav_song']=fav_song
for key,value in my_dic.items():
    print(f'key is {key} values is {value}')







