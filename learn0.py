#1.转义字符
'''
\n - 换行
\r - 回车
\t - 水平制表符
\b - 退格
'''

'''
print('hello\nworld')
print('hello\tworld')
print('helloooo\tworld')
print('hello\rworld') #输出world
print('hello\bworld') #\b退一格，输出hellworld
print('http:\\\\www.baidu.com') #每一个\都需要转义
print('老师说：\'大家好\'')
print(r'hello\nworld') #原字符r,转义字符则不起作用，最后一个字符不能是反斜杠
'''

#2.变量命名：英文字母或下划线开始，其由3部分组成，内存地址id()，类型type()，值print()
'''
a='mia'
print('标识',id(a))
print('类型',type(a))
print('值',a)
'''

#3.整数类型，int：包括整数及2、8、16进制数，以0b/0B,0o/0O,0x/0X表示，默认十进制输出
'''
print(0b11001)
print(0o176)
print(0x1EA)
'''

#4.浮点类型，float：包括科学计数法，aeb=a*10b
'''
n1=1.1
n2=2.2
n3=n1+n2
print('成绩提升了%.2f'% n3) #精确浮点位数
'''
'''a='128'
print(float(a))'''

#5.Bool类型，True-1, False-0
'''f1=True
f2=False
print(f1+1)
print(f2+1)
a='abc'
print('a' in a)
print('a' not in a)'''

'''
0，false, NONE,空的LIST,TUPLE,SET,DICT都为FALSE
print(bool(0))
print(bool(''))
print(bool([]))
print(bool(list()))'''

#6.字符串类型，为不可变的字符序列，单/双引号，可进行连接和重复运算
'''name='mia'
age=30
print('我是'+name+'今年'+str(age)+'岁')

字符串与列表类似，索引由0到-1，或-L到L-1
如‘hell0’的索引为
   01234
可通过strname[start : end : step]切片
如str[0:2]获取子串，及表示[0,2)的区间;str[-6:-1] 则为从索引的-6开始到最后一位
字符串可进行连接和重复运算
即‘a'+'a'='aa',a=‘ab''cd'， 2 *'a'='aa'
字符串的操作包括：
<str>.upper() 大写
     .lower() 小写
     .capitalize() 首字母大写
     .strip() 去除两端空格及指定字符
     .count() 检索指定字符串在另一字符串中出现的次数
     .find()  检索目标字符串第一次出现的索引,不存在则返回-1
     .rfind() 从右边开始检索，不存在则返回-1
     .index() 检索目标字符串第一次出现的索引，不存在会返回异常
     .rindex() 从右边开始检索，不存在会返回异常
     .split()可以将一个字符串按照指定的分隔符切分成多个子串，子串被保存到列表中（不包含分隔符）  
     .split(sep,maxsplit) 按指定字符进行切割, sep默认为None，包含所有空字符
     .replace() 替换
使用 join() 方法合并字符串时，它会将列表（或元组）中多个字符串采用固定的分隔符连接在一起
newstr = 分隔符.join(iterable)

驻留机制：建立一个变量后，若再对另一个变量赋予相同的值，使用同一块内存，提升性能
建议使用Join方法进行字符串拼接，此方法是先计算所有字符中的长度再拷贝，只新建一次对象

格式化字符串：
1. %作为占位符，%s,%i,%f等
2. format方法，{}；大圆括号内由0,1..n表示，format内变量
3. f string
a=80
b=90
c=(b/a-1)*100
name='mia'
1 print('%s的成绩提升了%.1f%%' %(name,c))
2 print('{0}的成绩提升了{1:.1f}%'.format(name,c))
3 print(f'{name}的成绩提升了{c:.1f}%')

查找操作
<str>.find()  检索目标字符串第一次出现的索引,不存在则返回-1
     .rfind() 从右边开始检索，不存在则返回-1
     .index() 检索目标字符串第一次出现的索引，不存在会返回异常
     .rindex() 从右边开始检索，不存在会返回异常

大小写转换，转换后原字符串不变，将产生一个新的字符串
<str>.upper() 大写
     .lower() 小写
     .capitalize() 第一个字母大写
     .title() 首字母大写
     .swapcase() 原本的大小写互换

对齐方法
<str>.center(20,'#') 居中，总长度，填充符-默认为空格
     .ljust() 左对齐
     .rjust() 右对齐
     .zfill() 右对齐,使用0填充

拆分
<str>.split(sep=,maxsplit=) 分割的结果为列表List
     .rplit(sep=,maxsplit=) 从右边分割

其他
<str>.replace(原字符,新字符) 替换
'&'.join(字符串/list/tuple) 

编码 <str>.encode(encoding='GBK') 或UTF-8  字符串转换为字节
解码 字节类型数据.decode(encoding='GBK') 或UTF-8
’‘’

#7.运算符
a,b=10,10
print(a==b) #比较值
print(a is b) #比较标识id
print(a is not b) #比较标识id
a,b=b,a #交换变量的值

print(4&8) #二进制对位，按位与，同为1时结果为1
print(4|8) #二进制对位，按位或，同为0时结果为0
print(4<<2) #位运算，向左移动1位，相当于乘以2
print(4>>1) #位运算，向右移动1位，相当于除以2
算术运算>位运算>比较运算
'''

#input输入多个数字
'''
n1=input('输入两个数字，以逗号分开')
n2=n1.split(',')
n3=int(n2[0])+int(n2[1])
print(n3)
'''
#8.分支结构
'''money=float(input('请输入你的购物金额'))
a=input('您是会员吗')
if a=='y':
    print('付款金额为',money*0.8) if money>=200 else print('付款金额为',money*0.9)
else:
    print('付款金额为',money*0.95) if money>=200 else print('付款金额为',money)'''

'''a=int(input('请输入你的成绩'))
if 90<=a<=100:
    print('成绩为A')
elif 80<=a<=89:
    print('成绩为B')
elif a>=70 and a<=79:
    print('成绩为C')  
elif a>=60 and a<=69:
    print('成绩为D')
elif a<60:
    print('不及格')
else:
    print('你输入的数据不在有效范围内，请重新输入')'''

#9.循环结构
#9.1 range()的用法
'''r=range(2,10,2)
print(list(r))
print(9 not in r)'''

#9.2 while循环
'''a=0
sum=0
while a<101:
    if a%2==0:
        sum+=a
    a+=1
    if sum>1000:
        break
print(sum)'''

#9.3 for...in循环
'''for a in 'python': #遍历字符串
    print(a)

for _ in range(5): #不使用变量，只进行循环时,使用_
    print('mia你好')

for item in range(100,1000):
    ge=item%10
    shi=item//10%10
    bai=item//100

    if ge**3+shi**3+bai**3==item:
        print(item)'''

'''for item in range(3): #break语句，退出程序
    put=input('请输入密码')
    if put=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
else:
    print('三次输入错误，账户已锁')'''

'''for item in range(1,51): #continue语句，结束当前循环，进入下一次循环 
    if item%5!=0:
        continue
    print(item)'''

#9.4 嵌套循环
'''for i in range(1,10): #99乘法表
    for j in range(1,i+1): 
        print(i,'*',j,'=',i*j,end='\t')
    print('')'''

#10.列表list,方括号。有序的元素集合，可更改及删除，元素数据类型可不同，可重复，可进行连接和重复运算。列表的索引总是从0开始、连续增大的,因此列表不允许对不存在的索引赋值
'''
create list from range
a=range(1,6)
list1=list(a)
print(list1)

a=list('abcdefg') #建立list

l=[i for i in range(1,11)] #列表生成式
print(l)

a.sort(reverse=True) #sort在原列表上排序
b=sorted(a,reverse=True) #sorted()方法会产生一个新的列表对象
print(a,b)

-连接：[list]+[list]
   -重复：n * [list]
   -索引单个元素：[list][n]
   -取子序列：[list][start:end] 
   -元素个数：len([list])
   -遍历列表里的元素：for <var> in [list]
   -检查是否在列表中：<x> in / not in [list]
   -添加x到列表最末：[list].append(x)
   -排序：[list].sort()
   -反转：[list].reverse()
   -在i位置插入x：[list].insert(i,x)

查找元素
   -返回x第一次出现的索引值：[list].index(x)
   -x在列表中出现的次数：[list].count(x) return o if x not exist

根据目标元素所在位置的索引进行删除，可以使用 del 关键字或者 pop() 方法；
根据元素本身的值进行删除，可使用列表（list类型）提供的 remove() 方法；
将列表中所有元素全部删除，可使用列表（list类型）提供的 clear() 方法。
   -移除第一次出现的x: [list].remove(x) if x did not exist then error
   -移除末尾的元素：[list].pop(x) if no x, then delete the last element
   -取出索引i的位置并移除：[list].pop(i)
'''

#11.字典dict,花括号。key-value, 无序的集合，可更改及删除，不可进行连接和重复运算。通过键而不是索引读取元素，键应不可变且唯一
#元组可以作为dict的key，但列表不能作为元组的 key。因为dict要求key必须是不可变类型，但列表是可变类型，因此列表不能作为key。
'''
create dic
1. use bracket
a={'china':'big','us':'small','japan':'tiny'}

by dict
2. a=[('a',1),('b',2),('c',3)]
b=dict(a)
3. b=dict(a=1,b=2) 此时key不允许表达式

a={'mia':20,'mason':100}
print(a['mia'])
print(a.get('j','不存在')) #get方法可定义键不存在时的返回值

为字典增加项,只需为不存在的key赋值；修改现有的类似
a['korea']='cheap'
a.update({'korea':'cheap'})

删除项
del a['korea']
a.pop('korea')
print('字典元素转为列表')

字典遍历
遍历key - for key in dicname:
遍历value - for value in dicname:
遍历item - for items in dicname:
遍历key value - for item, value in dicname:

print(list(a.keys()))
print(list(a.values()))
print(list(a.items()))

操作
tuple(a.keys())
tuple(a.values())
tuple(a.items())
a.get('china') == a['china']
a.pop('china') 删除及返回键对应的值
a.clear
print(a)

'''

#12.元组tuple,圆括号。不可变序列，没有增删改操作。若元组的元素是列表，列表内的元素可以更改
'''没有append.insert等用法，可进行连接和重复运算，外侧圆括号,索引与LIST用法一样
   -外侧可用括号，也可不用 t=123, t=(123,)
   -可以为空 t=()
   -可只包含一个元素 t=(123,)
   -元素可以是不同类型 t=(1,2,('mia','mason'))
   -定义后不可更改及删除
   -可通过索引访问单个元素
   -可进行连接和重复运算


两种创建元组的方法
tuplename = (element1, element2, ..., elementn)
a = tuple("hello")
a = tuple(range(1,6))
'''

#13.集合set, 花括号。无序，为没有value的字典，没有重复
'''
a1={1,2,3}
a2={1,2,3,4,5}
print(1 not in a1) #一次添加一个元素
a1.add(80) #至少添加一个元素
a1.update([4,5,6])
print(a1.issubset(a2))
'''

#14.函数
'''
函数调用过程进行参数的传递。
如果是不可变对象，函数体内修改不会影响实参的值；而可变对象相反

返回值：
1.若没有返回值，可以不写return
2.若返回1个，直接返回类型
3.若返回多个，返回的结果为元组

个数可变的位置参数
def fun(*x),返回的是元组，只能有1个
调用函数时，如果对象是列表，需将列表每个元素传递，亦使用fun(*list)

个数可变的关键字形参
def fun(**)，返回的是字典，只能有1个
调用函数时，如果对象是字典，需将列表每个元素传递，亦使用fun(**list)

既有位参和关键字形参，要求位参放在前面
'''

#15.异常处理 try...except...else...finally'''
'''try:
    a=int(input('请输入第一个数'))
    b=int(input('请输入第二个数'))
    result=float(a/b)
except BaseException as e:
    print('出错了',e)
else:
    print('计算结果为',result)
finally:
    print('谢谢使用')'''

#16 os模块,与操作系统之间的交互
'''
打开文件 
<variable>=open(<name>,<mode>)
mode包括:
r-只读：文件不存在时则输出错误
w-只写：文件不存在时则自动创建文件
r+：读写
a：附加到文件末尾
rb/wb/ab: 对二进制文件的操作
file.tell() 判断文件指针当前所处的位置
file.seek(offset[, whence]) 移动文件指针到文件的指定位置
whence：可选参数用于指定文件指针要放置的位置，有3个选择：0 代表文件头（默认值）、1 代表当前位置、2 代表文件尾。
offset：表示相对于 whence 位置文件指针的偏移量，正数表示向后偏移，负数表示向前偏移

打开及读取文件-单个文件
使用 with as 操作已经打开的文件对象（本身就是上下文管理器），无论期间是否抛出异常，都能保证 with as 语句执行完毕后自动关闭已经打开的文件。
def main1():
    with open(input('enter file name to open ')) as r:
        print(r.read()) #按文件格式输出全部信息
        print(r.readline()) #输出当下行信息
        print(r.readlines()) #输出全部信息，每行以\n结尾
main1()

多个文件
fileinput.input（files="filename1, filename2, ...", inplace=False, backup='', bufsize=0, mode='r', openhook=None）

读取文件内容及排序
a=[]
with open('/Users/mia/Desktop/file1.txt') as x:
    for line in x:
        a.append(int(line.strip()))
        a.sort()
print(sorted(a))

遍历文件
with open('file name') as x:
    for line in x:
x.close'

写文件时，务必要调用f.close()来关闭文件
def main2():
    with open(input('enter file name to open '),'w') as r:
        r.write('555')
        r.close()
        print(r.read())
main2()'''

'''交叉合并两个文件及输出到新文件
a = open('/Users/mia/desktop/a.txt','r')
b = open('/Users/mia/desktop/b.txt','r')

a_dict = {}
for idx,i in enumerate(a):
    if idx == 0:
        continue
    k,v = i.split()
    print(k,v)
    a_dict[k] = v

b_dict = {}
for idx,i in enumerate(b):
    if idx == 0:
        continue
    k,v = i.split()
    b_dict[k] = v

keys = list(set(list(a_dict.keys()) + list(b_dict.keys())))

list_str = ['name' + ' '+'gender' + ' '+'age']
for k in keys:
    a_v = a_dict[k] if k in a_dict.keys() else ''
    b_v = b_dict[k] if k in b_dict.keys() else ''
    s = k + ' ' + b_v +' '+ a_v
    list_str.append(s)

open('c','w').write('\n'.join(list_str))
a.close
b.close
'''

#17 类的写法

import math
import os
'''
class Circle():
    def __init__(self,r):
        self.r=r

    def get_area(self):
        return math.pi*math.pow(2,2)

    def get_premier(self):
        return math.pi*2*self.r

if __name__=='__main__':
    r=int(input('请输入半径'))
    c=Circle(3)
    print('圆的周长为',c.get_area(),c.get_premier())
'''
'''
class Instrument():
    def make_sound(self):
        pass
    
    def play_sound(self):
        self.make_sound()

class erhu(Instrument): #erhu类继承Instrument类，可重写父类的方法
    def make_sound(self): 
        print('二胡在演奏')

class Piano(Instrument):
    def make_sound(self):
        print('钢琴在演奏')
    
class Violin(Instrument):
    def make_sound(self):
        print('小提琴在演奏')

# def play(instrument):
#     instrument.make_sound()

if __name__=='__main__':
    violin = Violin()
    violin.play_sound()
'''

#18 算法
'''
Search
18.1 linear search, O(n)
def linear search(li,val):
    for ind,v in enumerate(li):
        f v==val:
        return ind
    return None

18.2 binary search, O(logn),前提是列表已经排序
def binary search(li,val):
    left=0
    right=len(li)-1
    while left <= right: #候选区有值
        mid=(left+right)//2
        if li[mid]==val:
            return mid
        elif li[mid]>val: #待查找的值在mid左侧
            right=mid-1
        else:
            left=mid+1
else:
    return None

#Sorting: 冒泡，选择，插入都是原地排序，时间复杂度都为O(n2)       
18.3 bubble sort, O(n2) n square
列表每相邻的两个数，如果前面比后面大，则交换这个数。一趟排序完成后，有序区新增一个数，无序区减少一个数，
共n-1趟,每趟的无序区个数为n-i-1

def bubble_sort(li):
    exchange=False
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[i]
                exchange=True
        if not exchange:
            return

a=[2,1,3,4,6,8,9,12,34]
bubble_sort(a)
print(a)'''

#18.4 selection sort, O(n2) n square
# def select_sort(li):
#     for i in range(len(li)-1):
#         min_idx = i
#         for j in range(i+1,len(li)):
#             if li[j] < li[min_idx]:
#                 min_idx = j
#         li[i],li[min_idx] = li[min_idx],li[i]
        
# a=[2,1,3,6,4,8,12,34]
# select_sort(a)
# print(a)

#18.5 insert sort, O(n2) n square
# def insert_sort(li):
#     for i in range(1,len(li)): #i is unsorted part
#         j = i-1 #j is sorted part
#         temp = li[i]
#         while j>=0 and li[j] > temp:
#             li[j+1]=li[j]
#             j=j-1
#         li[j+1] = temp
#         print(li)

# a=[2,1,3,6,4,8,12,34]
# insert_sort(a)
# print(a)

#18.6快速排序，nlogn
# def partition(li, left, right):
#     tmp = li[left]
#     while left < right:
#         while left < right and li[right] >= tmp: #从右边开始找，若比tmp大，则向左移一位
#             right -= 1 
#         li[left] = li[right] #当找到了比tmp小的，填入左边空位
    #     print(li,'left')
    #     while left < right and li[left] < tmp: #从左边开始找，若比tmp小，则向右移一位
    #         left += 1
    #     li[right] = li[left] #当找到了比tmp大的，填入右边空位。最终左右碰头，退出此循环
    #     #print(li,'right')
    # li[left] = tmp #将碰头的位置放入tmp,完成partition
    # return left

# def quicksort(li, left, right):
#     if left < right:
#         mid = partition(li, left, right)
#         quicksort(li, left, mid-1)
#         quicksort(li, mid+1, right)

# a=[8,4,3,6,2]
# print('original list:',a)
# quicksort(a, 0, len(a)-1)
# print('quicksort:',a)

#18.7堆排序 nlogn
# def sift(li, low, high): #low是堆的堆顶位置，high是堆的最后一个元素位置
#     i = low # i最初指向根节点
#     j = 2 * i + 1 #j开始是左孩子
#     tmp = li[low] #存堆顶
#     while j <= high: #只要j位置有数，就继续循环
#         if j +1 <= high and li[j+1] > li[j]: #右孩子存在且大于左孩子
#             j = j + 1 #则j指向右孩子
#         if li[j] > tmp:
#             li[i] = li[j]
#             i = j #往下看一层
#             j = 2 * i + 1
#         else:
#             li[i] = tmp #把tmp放回某一层上
#             break
#     else:
#         li[i] = tmp #当j>high,则到了最后一层，把tmp放回叶子上

# def heap_sort(li):
#     n = len(li)
#     for i in range(((n - 1) - 1) // 2, -1, -1): #找最后一个非叶子节点=最后一个节点n-1找其父亲(i-1)//2
#         #i指的是本层建堆的根节点下标
#         sift(li, i, n-1)
#     #建堆完成了,开始从顶端进行交换排序
#     for i in range(n-1, -1, -1):
#         # i指向当前堆的最后一个元素
#         li[0],li[i] = li[i],li[0]
#         sift(li, 0 ,i-1) #i-1是新的high

# 内置heap模块，默认生成小根堆，即根小于孩子
# import heapq
# import random

# li=list(range(100))
# random.shuffle(li)

# heapq.heapify(li)
# heapq.heappop(li)

#18.8归并排序，非原地排序，需额外的内存空间。空间复杂度On，时间复杂度nlogn
# def merge(li, low, mid, high): 
#     i = low         #low到mid是第一段
#     j = mid + 1     #mid+1到High是第二段
#     newli=[]
#     while i <= mid and j <= high: #只要左右两边都有数
#         if li[i] < li[j]:
#             newli.append(li[i])
#             i += 1
#         else:
#             newli.append(li[j])
#             j += 1
#     #while执行完则肯定有一部分没数字，但并不知道是哪部分
#     while i <= mid:
#         newli.append(li[i])
#         i += 1
#     while j <= high:
#         newli.append(li[j])
#         j += 1
#     li[low: high+1] = newli #把排序后的写回原本的li
    
# def merge_sort(li, low, high):
#     if low < high: #至少有两个元素
#         mid = (low + high) // 2
#         merge_sort(li, low, mid)
#         merge_sort(li, mid+1, high)
#         merge(li, low, mid, high)
        
# a=[2,1,4,3,5,7,6,8,10,9,20]
# merge_sort(a, 0, len(a)- 1) 

#19 数据结构
#19.1 栈
#19.1.1 栈的简单创建
# class Stack:
#     def __init__(self):
#         self.stack = []
    
#     def push(self,element):
#         self.stack.append(element)

#     def pop(self):
#         return self.stack.pop()

#     def get_top(self):
#         if len(self.stack) > 0:
#             return self.stack[-1]
#         else:
#             return None

#     def is_empty(self):
#         return len(self.stack) == 0


# s1=Stack()
# s1.push(1)
# s1.push(2)
# s1.push(3)

#19.1.2 栈的应用-括号匹配问题

