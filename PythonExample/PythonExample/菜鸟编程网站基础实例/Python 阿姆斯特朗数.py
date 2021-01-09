 
实例(Python 3.0+) 

# Filename : test.py
# author by : www.runoob.com
 
# Python 检测用户输入的数字是否为阿姆斯特朗数
 
# 获取用户输入的数字
num = int(input("请输入一个数字: "))
 
# 初始化变量 sum
sum = 0
# 指数
n = len(str(num))
 
# 检测
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** n
   temp //= 10
 
# 输出结果
if num == sum:
   print(num,"是阿姆斯特朗数")
else:
   print(num,"不是阿姆斯特朗数")

 
实例(Python 3.0+) 

# Filename ：test.py
# author by : www.runoob.com
 
# 获取用户输入数字
lower = int(input("最小值: "))
upper = int(input("最大值: "))
 
for num in range(lower,upper + 1):
   # 初始化 sum
   sum = 0
   # 指数
   n = len(str(num))
 
   # 检测
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** n
       temp //= 10
 
   if num == sum:
       print(num)

