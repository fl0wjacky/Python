#! /usr/bin/env python
# coding:utf-8
# 在Python 2.6以后，装饰器被拓展到类。一个装饰器可以接受一个类，从而起到加工类的效果

def decorator(aClass):
	class newClass:
		def __init__(self, age):
			self.total_display = 0
			self.wrapped	   = aClass(age)
		def display(self):
			self.total_display += 1
			print("total display", self.total_display)
			self.wrapped.display()
	return newClass

@decorator
class Bird:
	def __init__(self, age):
		self.age = age
	def display(self):
		print("My age is", self.age)


eagleLord = Bird(5)
for i  in range(3):
	eagleLord.display()
