
'''
#1.Search
1.1 linear search, O(n)
def linear search(li, val):
    for ind,v in enumerate(li):
        if v == val:
        return ind
    return None

1.2 binary search二分查找, O(logn),前提是列表已经排序
def binary search(li, val):
    left = 0
    right = len(li)-1
    while left <= right: #候选区有值
        mid=(left+right) // 2
        if val < li[mid]:
            right = mid -1
        elif val > li[mid]:
            left = mid + 1
        else: #val = li[mid]
            return mid
    else: #exit while loop as right>left and the val is not exist
        return None

#二分应用：在一个有序数组中，找>=某个数最左侧的位置
def binary_search_bigger(li, target):
    left = 0
    right = len(li) - 1

    while left <= right:
        mid = (left + right) // 2
        if li[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return left

    if left >= len():
        return None

#二分应用：寻找局部最小值

 
#2.Sorting: 冒泡，选择，插入都是原地排序，时间复杂度都为O(n2) 
# 同样值的个体之间，若不应因为排序改变相对次序，那这个排序是稳定的。
冒泡，插入，归并，一切桶排序思想下的排序具有稳定性；
选择，快速，堆排序不具有稳定性

#       
2.1 bubble sort, O(n2) n square
列表每相邻的两个数，如果前面比后面大，则交换这个数。一趟排序完成后，有序区新增一个数，无序区减少一个数，
共n-1趟,每趟的无序区个数为n-i-1

def bubble_sort(li):
    for i in range(1,len(li)):  #i为趟数，由第1趟到n-1趟，range取值为(1,len(li))
        exchange = False 
        for j in range(len(li)-i): #j为进行比对的元素下标，第i趟时从下标0一直走到下标n-i-1，range取值为(len(li)-i)
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[i]
                exchange = True 
        if not exchange: #若在n-1趟前已完成排序，则退出
            return li

a=[2,1,3,4,6,8,9,12,34]
bubble_sort(a)
print(a)'''

#2.2 selection sort, O(n2) n square
# def select_sort(li):
#     for i in range(len(li)-1): #默认下标0的元素为最小值，并直至下标n-2,range范围为(0,len(li)-1)
#         min_idx = i
#         for j in range(i+1,len(li)): #将i的值与余下列表的值一一比较，若有更小的则进行交换，range(i+1,len(li))
#             if li[j] < li[min_idx]:
#                 min_idx = j
#         li[i],li[min_idx] = li[min_idx],li[i]
        
# a=[2,1,3,6,4,8,12,34]
# select_sort(a)
# print(a)

#2.3 insert sort, O(N2) n square; 若数据本身有序，最优时间复杂度为OMega(N)
# def insert_sort(li):
#     for i in range(1,len(li)): #i is unsorted part
#         j = i-1 #j is sorted part
#         temp = li[i]
#         while j>=0 and li[j] > temp:
#             li[j+1]=li[j]
#             j-=1
#         li[j+1] = temp
#         print(li)

# a=[2,1,3,6,4,8,12,34]
# insert_sort(a)
# print(a)

#2.4快速排序，nlogn
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

#2.5堆排序 nlogn
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

#2.6归并排序，非原地排序，需额外的内存空间。空间复杂度On，时间复杂度nlogn
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

#2.6.1归并排序应用：小和问题


#3 线性数据结构
#3.1 栈Stack
#3.1.1 栈的简单创建
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

#3.1.2 栈的应用-括号匹配问题
# def brace_match(s):
#     stack = Stack()
#     match = {')':'(',']':'[','}':'{'}
#     for ch in s:
#         if ch in {'(','[','{'}:
#             stack.push(ch)
#         else:
#             if stack.is_empty():
#                 return False
#             elif stack.get_top() == match[ch]:
#                 stack.pop()
#             else:
#                 return False
#     if stack.is_empty():
#         return True
#     else:
#         return False

# print(brace_match('{(})'))

#3.1.2 栈的应用-解决迷宫问题，深度优先搜索，回溯法-不走回头路，使用栈来存储当前路径，不保证是最短路径
# from collections import deque

# maze = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
#     [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
#     [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
#     [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
#     [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
#     [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
#     [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]

# dirs = [
#     lambda x,y: (x+1, y),
#     lambda x,y: (x-1, y),
#     lambda x,y: (x, y-1),
#     lambda x,y: (x, y+1)
# ]

# def maze_path(x1, y1, x2, y2): #x1y1为起点, x2y2为终点
#     stack = []
#     stack.append((x1, y1))
#     while len(stack) > 0:
#         curNode = stack[-1] #当前节点
#         # maze[curNode[0]][curNode[1]] = 2
#         if curNode[0] == x2 and curNode[1] == y2:
#             for p in stack:
#                 print(p)
#             return True
#         #四个方向, 上x-1,y 下x+1,y 左x,y-1 右x,y+1
#         no_road = True
#         for dir in dirs:
#             nextNode = dir(curNode[0], curNode[1])
#             if maze[nextNode[0]][nextNode[1]] == 0: #如果下一个节点能走
#                 stack.append(nextNode)
#                 maze[nextNode[0]][nextNode[1]] = 2 #标记为已走过
#                 no_road = False
#                 break
            
#         if no_road:
#             maze[nextNode[0]][nextNode[1]] = 2
#             stack.pop()
         
#     print('没有路')
#     return False

# maze_path(1,1,8,8)
       
# #3.2 队列Queue:队头出队(front),队尾进队(rear)
# #3.2.1简单创建
# class Queue:
#     def __init__(self, size = 100):
#         self.queue = [0 for _ in range(size)]
#         self.size = size
#         self.rear = 0 #队尾，进队的
#         self.front = 0 #队首，出队的

#     def push(self, element):
#         if not self.is_full():
#             self.rear = (self.rear + 1) % self.size
#             self.queue[self.rear] = element
#         else:
#             raise IndexError('Queue is fulll')
    
#     def pop(self):
#         if not self.is_empty():
#             self.front = (self.front + 1) % self.size
#             return self.queue[self.front]
#         else:
#             raise IndexError('Queue is empty')

#     def is_empty(self):
#         return self.front == self.rear 

#     def is_full(self):
#         return (self.rear + 1) % self.size == self.front

# q=Queue(5) 
# for i in range(4):
#     q.push(i)
# q.is_full

# #3.2.2内置Queue
# from collections import deque
# q = deque([1,2,3,4,5],5) #若设定长度，当增加新的元素，队首元素自动出队，可用于读取文件的最后n行
# q.append(6) #队尾进队
# q.popleft() #队首出队

# #用于双向队列
# q.appendleft(2) #队首进队
# q.pop() #队尾出队

#3.3.3 队列的应用 - 迷宫问题，广度优先搜索
# from collections import deque
# maze = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
#     [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
#     [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
#     [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
#     [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
#     [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
#     [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]

# dirs = [
#     lambda x,y: (x+1, y),
#     lambda x,y: (x-1, y),
#     lambda x,y: (x, y-1),
#     lambda x,y: (x, y+1)
# ]

# def print_r(path):
#     curNode = path[-1]
#     realpath = []

#     while curNode[2] == -1:
#         realpath.append(curNode[0:2])
#         curNode = path[curNode[2]]
    
#     realpath.append(curNode[0:2])
#     realpath.reverse()
#     print(realpath)

# def maze_path_queue(x1, y1, x2, y2):
#     queue = deque()
#     queue.append((x1, y1, -1))
#     path = []
#     while len(queue) > 0:
#         curNode = queue.pop
#         path.append(curNode)
#         if curNode[0] == x2 and curNode[1] == y2:
#             print_r(path)
#             return True
#         for dir in dirs:
#             nextNode = dir(curNode[0], curNode[1])
#             if maze[nextNode[0]][nextNode[1]] == 0:
#                 queue.append((nextNode[0],nextNode[1],len(path) - 1)) #储存nextNode的三维信息，包括上一个带进入队的
#                 maze[nextNode[0]][nextNode[1]] = 2
    
#     print('没有路')
#     return False

# maze_path_queue(1, 1, 8, 8)

# 3.3单链表：一系列节点组成的集合。每个节点包括两部分，数据item和指向下一个节点的指针next
#3.3.1手动创建 
from typing import Deque


class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c

#3.3.2创建链表
#头插法
# def create_linklist_head(li):
#     head = Node(li[0])
#     for element in li[1:]:
#         node = Node(element)
#         node.next = head
#         head = node
#     return head
        
# def print_linklist_head(lk):
#     print('头插')
#     while lk:  
#         print(lk.item)
#         lk = lk.next

# li = [1,2,3]
# a=create_linklist_head([1,2,3])
# print_linklist_head(a)

#尾插法
# def create_linklist_tail(li):
#     head = Node(li[0])
#     tail = head
#     for element in li[1:]:
#         node = Node(element)
#         tail.next = node
#         tail = node
#     return head

# def print_linklist_tail(lk):
#     print('尾插')
#     while lk:  
#         print(lk.item)
#         lk = lk.next

# li = [1,2,3]
# a=create_linklist_tail(li)
# print_linklist_tail(a)

#3.3.3链表的插入和删除
'''
p.next = curnode.next
curnode.next = p

curnode.next = curnode.next.next
del p
'''

#3.4双链表：每个节点有两个指针，一个指向后一个元素，一个指向前一个
# 插入和删除
'''
p.next = curnode.next
curnode.next.prior=p
curnode.next=p
p.prior=curnode

curnode.next=p.next
p.next,prior=curnode
del p
'''

#3.5哈希表：哈希函数储存的键值对

#4 非线性数据结构
#4.1 树-模拟目录结构
# class Node():
#     def __init__(self, name, type='dir'):
#         self.name = name
#         self.type = type #dir or file
#         self.children = []
#         self.parent = None

#     def __repr__(self) -> str:
#         return self.name
        
# n = Node('hello')
# n2 = Node('world')
# n.children.append(n2)
# n2.parent = n

# class FileSystemTree():
#     def __init__(self):
#         self.root = Node('/')
#         self.now = self.root

#     def mkdir(self, name): #模拟mkdir命令，即在当前目录下新建文件夹
#         if name[-1] != '/':
#             name +='/'
#         node = Node(name)
#         self.now.children.append(node) #向下连接,树结构使用链式存储
#         node.parent = self.now         #向上连接，树结构使用链式存储

#     def ls(self): #模拟ls命令，即展示当前目录下的文件夹
#         return self.now.children

#     def cd(self, name): #模拟cd命令，即转换文件路径
#         if name[-1] != '/':
#             name +='/'
#         for child in self.now.children:
#             if child.name == name:
#                 self.now = child
#                 break
#         else:
#             print('not exist')
                
# tree = FileSystemTree()
# tree.mkdir('a/')
# tree.mkdir('b/')
# tree.mkdir('c/')
# tree.cd('c')

#4.1 二叉树
class BiTreeNode():
    def __init__(self, data):
        self.data = data
        self.lchild = None #左孩子
        self.rchild = None #右孩子

a = BiTreeNode('A')
b = BiTreeNode('B')
c = BiTreeNode('C')
d = BiTreeNode('D')
e = BiTreeNode('E')
f = BiTreeNode('F')
g = BiTreeNode('G')

e.lchild = a
e.rchild = g
a.rchild = c
g.rchild = f
c.lchild = b
c.rchild = d

root = e

#4.2 二叉树的4种遍历
#前序遍历，打印自己 - 递归左 - 递归右
def pre_order(root):
    if root:
        print(root.data, end=',')
        pre_order(root.lchild)
        pre_order(root.rchild)

print('前序遍历')
pre_order(root)
print('\n')

#中序遍历, 递归左 - 打印自己 - 递归右
def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data,end = ',')
        in_order(root.rchild) 

print('中序遍历')
in_order(root)
print('\n')

#后序遍历, 递归左 - 递归右 - 打印自己
def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data,end = ',')

print('后序遍历')
post_order(root)
print('\n')

#层次遍历, 每一层从左至右
from collections import deque 
def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue)>0:
        node = queue.popleft()
        print(node.data,end = ',')
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)

print('层级遍历')
level_order(root)
print('\n')


#4.3 二叉有序树/搜索树，可实现查询，插入，删除等
#4.3.1插入
class BiTreeNode():
    def __init__(self, data):
        self.data = data
        self.lchild = None #左孩子
        self.rchild = None #右孩子
        self.parent = None #右孩子

class BST():
    def __init__(self):
        self.root = None

    #递归法
    def insert(self, node, val):
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        
        return node
    
    #非递归法
    def insert_no_rec(self, val):
        p = self.root
        if not p: #空数，直接插入root
            self.root = BiTreeNode(val)
            return
        while p:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else: #左孩子不存在
                    p.lchild = BiTreeNode(val)
                    p.lchild = p
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
            else:
                return
#4.3.2查询
#递归版本
def query(self, node, val):
    if not node:
        return
    if node.data < val:
        return self.query(node.rchild, val)
    elif node.data > val:
        return self.query(node.lchid, val)
    else:
        return node

#非递归版本
def query_no_rec(self, val):
    p = self.root
    while p:
        if p.data < val:
            p = p.rchild
        elif p.data > val:
            p = p.lchild
        else:
            return p
    return None

#4.3.3删除
def remove_node_1(self, node): #情况1，删除的是叶子节点
    if not node.parent: #根节点
        self.root = None
    if node == node.parent.lchild: #node是父亲的左孩子
        node.parent.lchild = None
        node.parent = None
    else:
        node.parent.rchild = None

def remove_node_2_1(self, node): #情况2.1，node只有一个左孩子
    if not node.parent: #根节点
        self.root = node.lchild
        node.lchild.parent = None
    elif node == node.parent.lchild: #node是父亲的左孩子
        node.parent.lchild = node.lchild #它的父亲去连它的孩子
        node.lchild.parent = node.parent #它的孩子去连它的父亲
    else:
        node.parent.rchild = node.lchild 
        node.lchild.parent = node.parent 

def remove_node_2_2(self, node): #情况2.2，node只有一个右孩子
    if not node.parent: #根节点
        self.root = node.rchild
        node.rchild.parent = None
    elif node == node.parent.lchild: #node是父亲的左孩子
        node.parent.lchild = node.rchild #它的父亲去连它的孩子
        node.rchild.parent = node.parent #它的孩子去连它的父亲
    else:
        node.parent.rchild = node.rchild 
        node.rchild.parent = node.parent 

def delete(self, val):
    if self.root:
        node = self.query_no_rec(val)  
        if not node: #不存在
            return False
        if not node.lchild and node.rchild:
            self.remove_node_1(node)
    pass

#5.异或运算
# 列表里只有1个元素出现过奇数次，其他元素都是偶数次，找出这1个元素
def single_1(li):
    eor = 0
    for i in li:
        eor = eor ^ i
    return eor

a=[2,2,1,1,1,3,3]
print(single_1(a))

# 列表里有2个元素(元素不同)出现过奇数次，其他元素都是偶数次，找出这2个元素
def single_2(li):
    eor = 0
    for i in li:
        eor = eor ^ i
    
    right1 = eor & (~eor +1)
    
    a = 0
    for i in li:
        if i & right1 == 0:
            a ^= i 
    
    b = eor ^ a
    return a,b

a=[2,2,2,1,1,1,1,3,3,3]
print(single_2(a))
    

a = [1,2]
a.pop()
print(a)
print(s)


import heapq
q = []
heapq.heappush(q, 2)
heapq.heappush(q, 1)
heapq.heappush(q, 12)
heapq.heappush(q, 3)
heapq.heappush(q, 22)
print(q)

