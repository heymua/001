#转义符
'''\n - 换行
   \\ - \
   print('I\'m ok')
'''

#数字类型
'''-整数类型int：包括整数及2、8、16进制数，以0b/0B,0o/0O,0x/0X表示
   -浮点数类型float：包括科学计数法，aeb=a*10b
   -复数类型complex：z=a+bj,a是实数部分，b是虚数部分
   type(x)可返回数据的类型
'''

#字符串类型str，有序有索引，单/双引号，可进行连接和重复运算
'''字符串与列表类似，索引由0到-1，或-L到L-1
如‘hell0’的索引为
   01234
可通过strname[start : end : step]切片
如str[0:2]获取子串，及表示[0,2)的区间
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
split()可以将一个字符串按照指定的分隔符切分成多个子串，子串被保存到列表中（不包含分隔符）  
     .split(sep,maxsplit) 按指定字符进行切割, sep默认为None，包含所有空字符

     .replace() 替换

使用 join() 方法合并字符串时，它会将列表（或元组）中多个字符串采用固定的分隔符连接在一起
newstr = 分隔符.join(iterable)

for x in <str> 遍历每个字符

'''

'''输出格式化字符的3种表达，%, f', format
如，a=80
b=90
c=(b/a-1)*100
name='mia'
1 print('%s的成绩提升了%.1f%%' %(name,c))
2 print('{0}的成绩提升了{1:.1f}%'.format(name,c))
3 print(f'{name}的成绩提升了{c:.1f}%')
'''

#元组类型Tuple
#有序的，一旦初始化则不可更改及删除，通常用于保存无需修改的内容
#没有append.insert等用法，可进行连接和重复运算，外侧圆括号
#索引与LIST用法一样
'''-外侧可用括号，也可不用 t=123, t=(123,)
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

#列表类型List，有序的元素集合，可更改及删除，元素数据类型可不同，可进行连接和重复运算，方括号
#列表的索引总是从 0 开始、连续增大的.因此列表不允许对不存在的索引赋值
'''
create list from range
a=range(1,6)
list1=list(a)
print(list1)

create list from string
a=list('abc')
print(list1)'''

'''-连接：[list]+[list]
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

#字典类型Dictionary，key-value, 无序的集合，可更改及删除，不可进行连接和重复运算，大圆括号
#通过键而不是索引读取元素，键应不可变且唯一
#元组可以作为dict的key，但列表不能作为元组的 key。因为dict要求key必须是不可变类型，但列表是可变类型，因此列表不能作为key。
'''
create dic
1. use bracket
a={'china':'big','us':'small','japan':'tiny'}

by dict
2. a=[('a',1),('b',2),('c',3)]
b=dict(a)
3. b=dict(a=1,b=2) 此时key不允许表达式

为字典增加项,只需为不存在的key赋值；修改现有的类似
a['korea']='cheap'
a.update({'korea':'cheap'})

删除项
del a['korea']
a.pop('korea')

访问元素：
dictname[key] 键不存在时返回异常
dictname.get(key,default) 键不存在时返回NONE or 指定语句
a.setdefault(key,default value) 若key不存在则添加默认value

使用返回的元素
1.转换为list
list(dictname.keys())
list(dictname.values())
list(dictname.items())

2.for in循环遍历
for k in a.keys():

字典遍历
遍历key - for key in dicname:
遍历value - for value in dicname:
遍历item - for item in dicname:
遍历key value - for item, value in dicname:

是否在字典中，基于key来判断
'china' in a
'china' not in a 

操作
tuple(a.keys())
tuple(a.values())
tuple(a.items())
a.get('china') = a['china']
a.pop('china') 删除及返回键对应的值
a.clear
print(a)'''

'''集合，set类型，类似dict, 无序的集合，不储存value. 不重复
创建set需提供list作为输入集合，s=set([1,2,3])
a={1,2,3}
a=set('abc')

访问元素：无索引，最常用是使用循环结构遍历
a=set('abc')
for x in a:

向 set 集合中添加元素
setname.add(element)
setname.remove(element) if element not exist, return error
setname.discard(element) if element not exist, nothing returned

交集、并集、差集运算
交集&: set1 & set2
并集|：set1 | set2
差集-：set1 - set2
对称差集^：取集合AB中不属于A&B的元素
'''   

#统计词频问题
from codecs import replace_errors
from os import replace

def processline(line,wordcounts):
    line=replacesign(line)
    words=line.split()
    for word in words:
        if word in wordcounts:
            wordcounts[word]+=1
        else:
            wordcounts[word]+=1

def replacesign(line):
    for ch in line:
        if ch in '~@#%&()+_=-':
            line=line.replace(ch,'')
    return line

filename=input('input a filename:')
infile=open(filename,'r')

wordcounts={}
for line in infile:
    processline(line.lower(),wordcounts)

#函数-默认参数
a={1:1,2:2,3:3,4:4}
# for i in sorted(a.values()):
#     print(i)
print(sorted(a.values()))

#文件操作
'''打开文件 
# <variable>=open(<name>,<mode>)
# mode包括:
# r-只读：文件不存在时则输出错误
# w-只写：文件不存在时则自动创建文件
# r+：读写
# a：附加到文件末尾
# rb/wb/ab: 对二进制文件的操作
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

'''CASE 1 - option 1
combine 2 txt and create a new txt'''
# read source file
ftele1=open('/Users/mml/desktop/file 1.txt','r')
ftele2=open('/Users/mml/desktop/file 2.txt','r')
ftele1.readline() #skip column header
ftele2.readline() #skip column header
line1=ftele1.readlines() #read the content
line2=ftele2.readlines() #read the content

# establish a blank list to store info
list1_name=[]
list1_tele=[]
list2_name=[]
list2_email=[]

#red name and tel info from file 1,then store in new list
for line in line1:
    elements=line.split( ) 
    list1_name.append(str(elements[0]))
    list1_tele.append(str(elements[1]))

#red name and tel info from file 2,then store in new list
for line in line2:
    elements=line.split( )  
    list2_name.append(str(elements[0]))
    list2_email.append(str(elements[1]))

#create a new list with header
lines=[]
lines.append('name\ttel\temail\n') 

#search if file 1 name in file 2 name, if yes, copy email info from file 2 and store in new list
for i in range(len(list1_name)):
    s=''
    if list1_name[i] in list2_name:
        j=list2_name.index(list1_name[i]) #find the index in file 2
        s='\t'.join([list1_name[i],list1_tele[i],list2_email[j]])
        s+='\n' #即s=s+'\n',换到下一行
    else:
        s='\t'.join([list1_name[i],list1_tele[i],str('----')])
        s+='\n'
    lines.append(s)


for i in range(len(list2_name)):
    s=''
    if list2_name[i] not in list1_name:
        s='\t'.join([list2_name[i],str('----'),list2_email[i]])
        s+='\n'
    lines.append(s)

ftele3=open('result','w')
ftele3.writelines(lines)

#close the opening, not the files
ftele3.close
ftele2.close
ftele1.close

'''CASE 1 - option 2
a = open('/Users/mml/desktop/file 1.txt')
b = open('/Users/mml/desktop/file 2.txt')

a_dict = {}
for idx,i in enumerate(a):
    if idx == 0:
        continue
    k,v = i.split()
    # print(k,v)
    a_dict[k] = v


b_dict = {}
for idx,i in enumerate(b):
    if idx == 0:
        continue
    k,v = i.split()
    b_dict[k] = v


keys = list(set(list(a_dict.keys()) + list(b_dict.keys())))

list_str = ['name' + ' '+'tel' + ' '+'email']
for k in keys:
    a_v = a_dict[k] if k in a_dict.keys() else ''
    b_v = b_dict[k] if k in b_dict.keys() else ''
    s = k + ' ' + b_v +' '+ a_v
    list_str.append(s)

open('c','w').write('\n'.join(list_str))

'''

'''CASE2
multiple data in one row, separated by comma, extract and sort'''

with open('/Users/mml/desktop/file_case2.txt') as x:
    d=[]
    for line in x:
        b=line.strip()
        c=b.split(',')
        d.extend(c)

#convert a str list to int list
    d=list(map(int,d)) # use map

    e=[] 
    for item in d:
        e.append(int(item)) #use loop

#only print out unique no. in ascending/descending order
print(sorted(list(set(d)))) #create set to eliminate duplicate, then convert to list to sort

f=[]
for item in d:
    if item not in f: #check duplicates
        f.append(item)
print(sorted(f,reverse=True))

x.close


