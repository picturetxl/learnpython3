
from greet import greet_user

'''
@Author: Austin
@Date: 2020-02-19 21:37:29
@LastEditTime: 2020-02-20 00:05:54
@LastEditors: Please set LastEditors
@Description: hello world 
@FilePath: /python/helloworld.py
'''
# 程序 = 数据结构 +　算法

print('hello world')

message = "hello python world"
print(message)

hello_message = "hello 2+3"
print(hello_message)

print(2+3)

print('hello ')
print("hello")
print(hello_message.title())

print(3**2) 
print(3*2)
# int to string : str(int)
print("hello " + str(2) +" hha" )


bicycles = ['trek','conondale',2]
print(bicycles)

for b in bicycles:
    print(b)


list_numbers = []

numbers = list(range(1,6))
print(numbers)



user={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi'
}
# 遍历字典中每个键值对
for key,value in user.items():
    print("key:"+key + " "+ "value:"+value)
#　遍历字典中的键 
for key in user.keys():
    print("key:"+key )

#　遍历字典中的值
for v in user.values():
    print("value:"+v)


# <==>
greet_user()
greet_user()

# 必选参数在前，默认参数在后
# 默认参数必须跟在非默认参数后面
def describe_pet(animal_type,pet_name="jack"):
    print("I have a "+ animal_type + ".")
    print("My "+animal_type + "'s name is "+pet_name.title()+".")


# describe_pet("cat","mimi")
# describe_pet(animal_type = "cat", pet_name="mimi")
# describe_pet(pet_name="mimi",animal_type = "cat")
















    