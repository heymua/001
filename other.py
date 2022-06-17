'''格式化表达
a=80
b=90
c=(b/a-1)*100
name='mia'
print('%s的成绩提升了%.2f%%' %(name,c))
print('{0}的成绩提升了{1:.2f}%'.format(name,c))
print(f'{name}的成绩提升了{c:.2f}%')'''

'''
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

a = open('/Users/mia/desktop/a.txt','r')
b = open('/Users/mia/desktop/b.txt','r')

a_dict={}
for idex,value in enumerate(a):
    if idex==0:
        continue
    k,v=value.split()
    a_dict[k]=v

b_dict={}
for idex,value in enumerate(b):
    if idex==0:
        continue
    k,v=value.split()
    b_dict[k]=v

new_name=list(set(list(a_dict.keys())+list(b_dict.keys())))
new_head=['name\t'+'age\t'+'gender\t']
for i in new_name:
    new_age=a_dict[i] if i in a_dict.keys() else''
    new_gender=b_dict[i] if i in b_dict.keys() else''
    new_content=i+'\t'+new_age+'\t'+new_gender
    print(new_content)
    new_head.append(new_content)

open('/Users/mia/desktop/c.txt','w').write(str(new_head))
a.close
b.close


