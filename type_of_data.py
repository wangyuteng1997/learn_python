# Python有五个标准的数据类型：
# Numbers（数字）
    # 四种不同的数字类型：
       # int（有符号整型）
       # long（长整型[也可以代表八进制和十六进制]）
       # float（浮点型） 8个字节
       # complex（复数）
# String（字符串）
# List（列表）
# Tuple（元组）
# Dictionary（字典）

# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

'''
list
'''
# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', 'Tracy']

# 变量classmates就是一个list。用len()函数可以获得list元素的个数：
len(classmates)

# 用索引来访问list中每一个位置的元素，记得索引是从0开始的：
classmates[0]  # 'Michael'
classmates[1]  #'Bob'
classmates[2]  #'Tracy'
classmates[-1] # 还可以用-1做索引，直接获取最后一个元素


# 可以往list中追加元素到末尾
classmates.append('Adam')  # ['Michael', 'Bob', 'Tracy', 'Adam']
# 也可以把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1, 'Jack')
# 要删除list末尾的元素，用pop()方法：
classmates.pop()
# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(1) # ['Michael', 'Bob', 'Tracy']
# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[1] = 'Sarah'

# list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]

'''
tuple
'''
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
classmates = ('Michael', 'Bob', 'Tracy')
# 现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。
# 获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。


'''
dic
'''
# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
d['Adam'] = 67 # 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：

#要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('Bob')

'''
set
'''
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
# 要创建一个set，需要提供一个list作为输入集合：
s = set([1, 2, 3]) #  s = {1, 2, 3}
# 注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(4)

#  通过remove(key)方法可以删除元素
s.remove(4)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错

# str是不变对象，而list是可变对象。
#
# 对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如
a = ['c', 'b', 'a']
a.sort()
#  ['a', 'b', 'c']

a = 'abc'
a.replace('a', 'A')
#'Abc'