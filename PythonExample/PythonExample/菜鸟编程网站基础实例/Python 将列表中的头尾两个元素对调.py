实例 1 
def swapList(newList): 
    size = len(newList) 
      
    temp = newList[0] 
    newList[0] = newList[size - 1] 
    newList[size - 1] = temp 
      
    return newList 

newList = [1, 2, 3] 
  
print(swapList(newList)) 
实例 2 
def swapList(newList): 
      
    newList[0], newList[-1] = newList[-1], newList[0] 
  
    return newList 
      
newList = [1, 2, 3] 
print(swapList(newList)) 
实例 3 
def swapList(list): 
      
    get = list[-1], list[0] 
      
    list[0], list[-1] = get 
      
    return list
      
newList = [1, 2, 3] 
print(swapList(newList)) 
