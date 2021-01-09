实例 
>>> li = ["a", "b", "mpilgrim", "z", "example"]
>>> li
['a', 'b', 'mpilgrim', 'z', 'example']
>>> li[1]         
'b'
实例 
>>> li 
['a', 'b', 'mpilgrim', 'z', 'example']
>>> li[-1] 
'example'
>>> li[-3] 
'mpilgrim'
>>> li 
['a', 'b', 'mpilgrim', 'z', 'example']
>>> li[1:3]  
['b', 'mpilgrim'] 
>>> li[1:-1] 
['b', 'mpilgrim', 'z'] 
>>> li[0:3]  
['a', 'b', 'mpilgrim'] 
实例 
>>> li 
['a', 'b', 'mpilgrim', 'z', 'example']
>>> li.append("new")
>>> li 
['a', 'b', 'mpilgrim', 'z', 'example', 'new']
>>> li.insert(2, "new")
>>> li 
['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new']
>>> li.extend(["two", "elements"]) 
>>> li 
['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
实例 
>>> li 
['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
>>> li.index("example")
5
>>> li.index("new")
2
>>> li.index("c")
Traceback (innermost last):
 File "<interactive input>", line 1, in ?
ValueError: list.index(x): x not in list
>>> "c" in li
False
实例 
>>> li 
['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
>>> li.remove("z")  
>>> li 
['a', 'b', 'new', 'mpilgrim', 'example', 'new', 'two', 'elements']
>>> li.remove("new")    # 删除首次出现的一个值
>>> li 
['a', 'b', 'mpilgrim', 'example', 'new', 'two', 'elements']    # 第二个 'new' 未删除
>>> li.remove("c")     #list 中没有找到值, Python 会引发一个异常
Traceback (innermost last): 
 File "<interactive input>", line 1, in ? 
ValueError: list.remove(x): x not in list
>>> li.pop()      # pop 会做两件事: 删除 list 的最后一个元素, 然后返回删除元素的值。
'elements'
>>> li 
['a', 'b', 'mpilgrim', 'example', 'new', 'two']
实例 
>>> li = ['a', 'b', 'mpilgrim']
>>> li = li + ['example', 'new']
>>> li 
['a', 'b', 'mpilgrim', 'example', 'new']
>>> li += ['two']         
>>> li 
['a', 'b', 'mpilgrim', 'example', 'new', 'two']
>>> li = [1, 2] * 3
>>> li 
[1, 2, 1, 2, 1, 2] 
实例 
>>> params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
>>> ["%s=%s" % (k, v) for k, v in params.items()]
['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
>>> ";".join(["%s=%s" % (k, v) for k, v in params.items()])
'server=mpilgrim;uid=sa;database=master;pwd=secret'
实例 
>>> li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
>>> s = ";".join(li)
>>> s 
'server=mpilgrim;uid=sa;database=master;pwd=secret'
>>> s.split(";")   
['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
>>> s.split(";", 1) 
['server=mpilgrim', 'uid=sa;database=master;pwd=secret']
实例 
>>> li = [1, 9, 8, 4] 
>>> [elem*2 for elem in li]    
[2, 18, 16, 8] 
>>> li
[1, 9, 8, 4] 
>>> li = [elem*2 for elem in li] 
>>> li 
[2, 18, 16, 8] 
实例 
>>> params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
>>> params.keys()
dict_keys(['server', 'database', 'uid', 'pwd'])
>>> params.values()
dict_values(['mpilgrim', 'master', 'sa', 'secret'])
>>> params.items()
dict_items([('server', 'mpilgrim'), ('database', 'master'), ('uid', 'sa'), ('pwd', 'secret')])
>>> [k for k, v in params.items()]
['server', 'database', 'uid', 'pwd']
>>> [v for k, v in params.items()]
['mpilgrim', 'master', 'sa', 'secret']
>>> ["%s=%s" % (k, v) for k, v in params.items()]
['server=mpilgrim', 'database=master', 'uid=sa', 'pwd=secret']
实例 
>>> li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
>>> [elem for elem in li if len(elem) > 1]
['mpilgrim', 'foo']
>>> [elem for elem in li if elem != "b"]
['a', 'mpilgrim', 'foo', 'c', 'd', 'd']
>>> [elem for elem in li if li.count(elem) == 1]
['a', 'mpilgrim', 'foo', 'c']
