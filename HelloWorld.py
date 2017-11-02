#!/usr/bin/env python
#coding=utf-8

import sys

print("practice world");
print "你好，世界";
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
if True:
    print days
else:
 print "False"


 '''
 这里是一大堆注视
 '''

print 'zhushi'

counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

print counter
print miles
print name

sentence = "ilovepython"
print sentence[-4:]

list = [  786 , 2.23, 'john', 70.2]
print list[1:]

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print tinydict['name']
print tinydict.keys
print type(tinydict)

for index in range(len(list)):
    print list[index]

print max(list)

import time

localtime = time.localtime(time.time())
print "本地时间为 :", localtime


def sum(arg1, arg2):
    total = arg1 + arg2
    global b
    b = total * 10
    return total

a = sum(1,2)
print a,b

print sys.path
print dir(sys)
print type(globals().keys())


# str = raw_input("请输入：");
# print "你输入的内容是: ", str

numlist = [x*7 for x in range(2,10,2)]
print numlist


class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()


class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary


"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount


import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

json = json.dumps(data)
print json