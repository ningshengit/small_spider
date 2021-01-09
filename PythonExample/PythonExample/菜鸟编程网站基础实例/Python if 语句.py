 
实例(Python 3.0+) 

# Filename : test.py
# author by : www.runoob.com
 
# 用户输入数字
 
num = float(input("输入一个数字: "))
if num > 0:
   print("正数")
elif num == 0:
   print("零")
else:
   print("负数")

 
实例(Python 3.0+) 

# Filename ：test.py
# author by : www.runoob.com
 
# 内嵌 if 语句
 
num = float(input("输入一个数字: "))
if num >= 0:
   if num == 0:
       print("零")
   else:
       print("正数")
else:
   print("负数")

