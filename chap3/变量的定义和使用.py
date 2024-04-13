luck_number=8 #创建一个整型变量并为其赋值为8

my_name='123' #字符串类型的变量

print('luck_number的数据类型为',type(luck_number))
print('my_name的数据类型为',type(my_name))

#python可以动态修改变量的数据类型，通过赋不同类型的值就可以直接修改
luck_number='青岛欢迎你'
print('luck_number的数据类型为',type(luck_number))  #str

#python中允许多个变量指向同一个值
no=number=1024
print(no,number)
print(id(no),id(number)) #查看对象的内存地址