# print()会依次打印每个字符串，遇到逗号“,”会输出一个空格
print('The quick brown fox', 'jumps over', 'the lazy dog')
print('100 + 200 =', 100 + 200)

# print(*objects, sep=' ', end='\n', file=sys.stdout)
# objects --表示输出的对象。输出多个对象时，需要用 , （逗号）分隔。
# sep -- 用来间隔多个对象。
# end -- 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符。
# file -- 要写入的文件对象。
print("www", "snh48", "com", sep=".")  # 设置间隔符


'''
变量的输出
'''
num = 19
print(num)    #19  输出数值型变量


str = 'Duan Yixuan'
print(str)  #Duan Yixuan  输出字符串变量

list = [1,2,'a']
print(list)   #[1, 2, 'a']  输出列表变量

tuple = (1,2,'a')
print(tuple)    #(1, 2, 'a') 输出元组变量

dict = {'a':1, 'b':2}
print(dict)   # {'a': 1, 'b': 2} 输出字典变量

'''
数据的格式化输出
'''
s = 'Duan Yixuan'
x = len(s)
print('The length of %s is %d' % (s, x))
#'The length of %s is %d' 这部分叫做：格式控制符
#(s,x) 这部分叫做：转换说明符
#% 字符，表示标记转换说明符的开始
#输出如下： The length of Duan Yixuan is 11

#  %s 字符串采用str()的显示
#  %c  单个字符
#  %d 十进制整数
#  %f,%F  浮点数
'''
最小字段宽度和精度
'''
#最小字段宽度：转换后的字符串至少应该具有该值指定的宽度。如果是*（星号），则宽度会从值元组中读出。
#点(.)后跟精度值：如果需要输出实数，精度值表示出现在小数点后的位数。如果需要输出字符串，那么该数字就表示最大字段宽度。如果是*，那么精度将从元组中读出。
PI = 3.141592653
print('%10.3f'%PI)
#字段宽10，精度3  3.142


print("PI=%.*f"%(3,PI))
#用*从后面的元组中读取字段宽度或精度,可以读取出来精度是3位


print("PI=%*.3f"%(10,PI))
#精度为3，总长为10.

'''
# 旧式字串格式化（%）
# 新式字串格式化（format()）
'''
text = 'world'
print('hello {}'.format(text))
# hello world

name = 'Jack'
text = 'world'
print('hello {a}, hello {b}'.format(a=name, b=text))
# hello Jack, hello world

# 字串插值（Formatted String Literal）
#虽然已经有了新式字串格式化，然而在Python 3.6又新增了格式字串字面值（Formatted String Literal）此一作法可以把Python运算式嵌入在字串常数中。
#最后一种格式化字符串的方法是使用以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换：
text = 'world'
print(f'Hello, {text}')

x = 10
y = 27
print(f'x + y = {x + y}')
# 37