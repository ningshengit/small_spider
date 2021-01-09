实例 1 
def Reverse(lst): 
    return [ele for ele in reversed(lst)] 
      
lst = [10, 11, 12, 13, 14, 15] 
print(Reverse(lst)) 
实例 2 
def Reverse(lst): 
    lst.reverse() 
    return lst 
      
lst = [10, 11, 12, 13, 14, 15] 
print(Reverse(lst)) 
实例 3 
def Reverse(lst): 
    new_lst = lst[::-1] 
    return new_lst 
      
lst = [10, 11, 12, 13, 14, 15] 
print(Reverse(lst)) 
