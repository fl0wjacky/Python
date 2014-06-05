#! /usr/bin/env python
# codign:utf-8
# 
class Bird(object):
	feather = True

class Chicken(Bird):
	fly = False
	def __init__(self, age):
		self.age = age

summer = Chicken(2)
print Bird.__dict__
print Chicken.__dict__
print summer.__dict__
