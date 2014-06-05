#! /usr/bin/env python
# coding:utf-8
# 对象的属性储存在对象的__dict__属性中.__dict__是一个字典，键为属性名，对应的值为属性本身
class Bird(object):
	feather = True

class Chicken(Bird):
	fly = False
	def __init__(self, age):
		self.age = age
	def getAdult(self):
		if self.age > 1.0: return True
		else: return False
	adult = property(getAdult)

summer = Chicken(2)

print(Bird.__dict__)
print(Chicken.__dict__)
print(summer.__dict__)
# Python中的属性时分层定义的，比如这里分为object/Bird/Chicken/summer四层。
# 当我们需要调用某个属性时，Python会一层层向上遍历，直到找到那个属性。
# 不同层中定义个相同属性，Python向上的过程中，会选取先遇到的那个，即较低层的。
summer.__dict__['age'] = 3
print summer.__dict__['age']
summer.age = 5
print summer.age
print '-------'
print summer.__class__	# 可通过实例的__class__属性找到该实例的类 
print Chicken.__base__	# 可通过类的__base___属性找到该类的父类
print Bird.__base__
print object.__base__
print '-------'
summer.__dict__['age'] = 0
print summer.adult
summer.__dict__['age'] = 3
print summer.adult
