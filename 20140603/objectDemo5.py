#! /usr/bin/env python
# coding:utf-8
# Program:
# 当定义类的方法时，必须要传递一个self的参数。这个参数指代的就是类的一个对象。我们可以通过操纵self,来修改某个对象的性质。	

class Human(object):
	def __init__(self, input_gender):
		self.gender = input_gender
	def printGender(self):
		print self.gender

if __name__ == "__main__":
	li_lei = Human('male')
	print li_lei.gender
	li_lei.printGender()
