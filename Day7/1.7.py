lst=['hello','world','python']
print('原列表',lst,id((lst)))
lst.append('sql')
print('增加元素之后：',lst,id((lst)))

lst.insert(1,100)
print(lst)

lst.remove('world')
print('删除元素之后的列表：',lst,id((lst)))

#使用pop(idnex)根据索引将元素取出，然后删除
print(lst.pop(1))
print(lst)

#清除列表中所有的元素clear()
# lst.clear()
# print(lst,id(lst))

lst.reverse()
print(lst)

new_list=lst.copy()
print(lst,id((lst)))
print(new_list,id(new_list))

lst[1]='mysql'
print(lst)