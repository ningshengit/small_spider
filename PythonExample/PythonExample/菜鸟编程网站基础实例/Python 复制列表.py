实例 1 
def clone_runoob(li1): 
    li_copy = li1[:] 
    return li_copy 
  
li1 = [4, 8, 2, 10, 15, 18] 
li2 = clone_runoob(li1) 
print("原始列表:", li1) 
print("复制后列表:", li2) 
实例 2: 使用 extend() 方法 
def clone_runoob(li1): 
    li_copy = [] 
    li_copy.extend(li1) 
    return li_copy 
  
li1 = [4, 8, 2, 10, 15, 18] 
li2 = clone_runoob(li1) 
print("原始列表:", li1) 
print("复制后列表:", li2) 
实例 3: 使用 list() 方法 
def clone_runoob(li1): 
    li_copy = list(li1) 
    return li_copy 
  
li1 = [4, 8, 2, 10, 15, 18] 
li2 = clone_runoob(li1) 
print("原始列表:", li1) 
print("复制后列表:", li2) 
