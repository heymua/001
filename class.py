#1.定义类
class Student(object): #类对象
    native_place='四川' #直接写在类里的变量是类属性，方法之外定义的类属性被所有实例对象共享

    #初始化方法
    def __init__(self,name,age):
        self.name=name #self.name是实例属性
        #self.__age=age 若不希望在类的外部使用，所以加了两个_。实例对象在引用时，需用stu1.Student__age，但最好不访问
        self.age=age
    
    def __add__(self,other): #只有通过定义才可使对象相加
        return self.name + other.name

    #类之内定义的为方法，在类之外定义的称为函数
    #实例方法，传的是实例对象即self
    def eat(self): 
        print(self.name+'在吃饭')
    
    #静态方法，什么都不写
    @staticmethod
    def method():
        print('我使用了staticmethod修饰，所以我是静态方法')
    
    #静态方法的使用，类名直接访问
Student.method()

    #类方法，需要写cls
    @classmethod
    def cm(cls):
        print('我使用了classmethod修饰，所以我是类方法')

    #类方法的使用，由类名直接访问，不需要写cls
Student.cm()


#2.创建实例对象后，就可以调用类中的属性和方法
stu1=Student('mia',20)  #Student类对象的实例对象
stu2=Student('may',30)
'''
print(stu1.native_place,stu1.age,stu1.name,stu1+stu2) #实例对象可调用类属性/实例属性，对象名.属性
stu1.eat()        #对象名.方法名
Student.eat(stu1) #类名.方法名(对象)，与上一行一样
'''
Student.native_place='hk'  #更改类属性后，实例对象调用类属性的值也相应变化
print(stu1.native_place)

'''
print('----特殊属性----')
print(stu1.__dict__) #__dict__输出对象的属性字典
print(stu1.__class__) #__class__输出实例对象所属的类
print(Student.__bases__) #__bases__输出其父类的元素
print(Student.__subclasses__) #__subclasses__输出其子

#3.动态绑定属性：创建对象后，可动态的新增属性和方法，其只针对当前实例对象
#如只为stu2绑定性别属性
stu2.gender='F'

#4.动态绑定方法:在定义函数后，由实例对象进行绑定，若不绑定则不起作用
def show():
    print('这是类之外的函数')

stu1.show=show #实例对象绑定show方法
stu1.show()
stu2.show() #因stu2并未绑定show，将报错

#5.面向对象三大特征，与语言无关
封装：提高安全性, 私有属性以__开头
继承：默认继承Object类，可对方法进行重写
多态：Python是动态语言，关注对象的行为

#6.继承，方法重写
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self, name, age,stu_no):
        super().__init__(name, age) #调用父类的Init方法
        self.stu_no=stu_no
    
    def info(self): #方法重写
        super().info() #调用父类方法
        print(self.stu_no)

class Teacher(Person):
    def __init__(self, name, age,teach_year):
        super().__init__(name, age)
        self.teach_year=teach_year

    def info(self):#方法重写
        super().info() #调用父类方法
        print(self.teach_year)

stu1=Student('mia',20,1001)
tea1=Teacher('may',40,10)

print('----继承----')
stu1.info()
tea1.info()

object类是所有类的父类
class Student: 
    
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self): #str方法重写
        return'重写结果'

stu3=Student('mia',22)
print('object类')
print(stu3)

#多态：即便不知道一个变量所引用的对象是什么类型，仍然可以通过这个变量调用方法，动态决定调用哪个方法
class Animal(object):
    def eat(self):
        print('动物会吃')
class Dog(Animal):
    def eat(self):
        print('狗吃')
class Cat(Animal):
    def eat(self):
        print('猫吃')
class Person:
    def eat(self):
        print('人吃饭')

def fun(obj):
    obj.eat()

fun(Cat())
fun(Dog())
fun(Person())

#类的拷贝
class CPU:
    pass
class DISK:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

#(1)变量的赋值
cpu1=CPU()
cpu2=cpu1
print('---变量的赋值---')
print(id(cpu1))
print(id(cpu2)) #实际是一个对象，只是放在了两个变量存储

#(2)类的浅拷贝
disk1=DISK()
computer1=Computer(cpu1,disk1)
import copy
computer2=copy.copy(computer1) #执行浅拷贝，只拷贝源对象，与源对象引用同样的子对象
print('---类的浅拷贝---')
print(computer1,computer1.cpu,computer1.disk) 
print(computer2,computer2.cpu,computer2.disk) #子对象与computer1的一样

#(3)类的深拷贝
print('---类的深拷贝---')
computer3=copy.deepcopy(computer1) #通过deepcopy执行深拷贝，源对象及子对象都会拷一份出来
print(computer1,computer1.cpu,computer1.disk)
print(computer3,computer3.cpu,computer3.disk) #子对象与computer1的不一样
'''