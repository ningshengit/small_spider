 
实例 1：使用内置方法 len() 

str = "runoob"
print(len(str))
 
实例 2：使用循环计算 

def findLen(str): 
    counter = 0
    while str[counter:]: 
        counter += 1
    return counter 
  
str = "runoob"
print(findLen(str))
