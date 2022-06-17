# def linear_search(li, val):
#     for idx, v in enumerate(li):
#         print(idx, v)
#         if val == v:
#            return idx
#     return None

# # a=[1,2,3,4]
# # print(linear_search(a,2))

# def binary_search(li, val):
#     left = 0
#     right = len(li) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if val < li[mid]:
#             right = mid - 1
#         elif val > li[mid]:
#             left = mid + 1
#         else: #val = li[mid]
#             return mid 
#     else: #exit while loop as right>left and the val is not exist
#         return None

# # a=[1,2,3,4,5,6,7,8,9,10]
# # print(binary_search(a,11))

# def bubble_sort(li):
#     for i in range(1,len(li)):
#         for j in range(len(li)-i):
#             if li[j] > li[j+1]:
#                 li[j],li[j+1] = li[j+1], li[j]
#     return li

# # a=[2,2,4,5]
# # print(bubble_sort(a))

# import math
# def select_sort(li):
#     for i in range(len(li)-1):
#         min_idx = i
#         for j in range(i+1, len(li)):
#             if li[j] < li[min_idx]:
#                 li[j],li[min_idx] = li[min_idx],li[j]
#     return li

# a=[2,1,6,5,3,7,4]
# print(select_sort(a))

def single_2(li):
    eor = 0
    for i in li:
        eor ^= i
        
    right1 = eor & (~eor +1)
    print(right1)

    a = 0
    for i in li:
        if i & right1 == 0:
            print(i)
            a ^= i 
    
    b = eor ^ a
    return a,b

# a=[2,2,4,1,1,3]
# print(single_2(a))

def binary_search_bigger(li, target):
    left = 0
    right = len(li) - 1

    while left <= right:
        mid = (left + right) // 2
        if li[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
        print(left,mid,right)
   
# a = [1,2,3,3,4]
# print(binary_search_bigger(a,3))
    
 
def merge(li, low, mid, high): 
    i = low         #low到mid是第一段
    j = mid + 1     #mid+1到High是第二段
    newli=[]
    low_sum = 0
    while i <= mid and j <= high: #只要左右两边都有数
        if li[i] < li[j]:
            newli.append(li[i])
            i += 1
        else:
            newli.append(li[j])
            j += 1
    #while执行完则肯定有一部分没数字，但并不知道是哪部分
    while i <= mid:
        newli.append(li[i])
        i += 1
    while j <= high:
        newli.append(li[j])
        j += 1
    li[low: high+1] = newli #把排序后的写回原本的li
    
def merge_sort(li, low, high):
    if low < high: #至少有两个元素
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid+1, high)
        merge(li, low, mid, high)
        
a=[2,1,4,3,5,7,6,8,10,9,20]
merge_sort(a, 0, len(a)- 1)