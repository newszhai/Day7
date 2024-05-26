lst=['hellp','world','python','php']
#使用遍历循环for遍历列表元素
for item in lst:
    print(item)


#使用for循环，range()函数，len()函数，根据索引进行遍历
for i in range(0,len(lst)):
    print(i,'-->',lst[i])

for index,item in enumerate(lst):
  print(index,item)
for index,item in enumerate(lst,start=1):
  print(index,item)
for index,item in enumerate(lst,1):
  print(index,item)






