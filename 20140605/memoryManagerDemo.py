#! /usr/bin/env python
# coding:utf-8
# Python是动态类型的语言，对象与引用分离。
# 为了探索对象在内存中的存储，我们可以求助于Python内置函数id()
a = 1
print(id(a))		#十进制表示
print(hex(id(a)))	#十六进制表示

b = 1				#在Python中，整数和短小的字符，Python都会缓存这些对象，以便重复使用
print(id(a))		#如此处创建多个等于1的引用时，实际上是让所有这些引用指向同一个对象
print(id(b))
print


# 检验两个引用指向同一个对象，我们适用is关键字。is用于判断两个引用所指的对象是否相同
#True
a = 1
b = 1
print(a is b)
print(id(a))
print(id(b))

#True
a = 'good'
b = "good"
print(a is b)
print(id(a))
print(id(b))

#False
a = 'a very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very long string'
b = 'a very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very long string'
print(a is b)
print(id(a))
print(id(b))

#False
a = []
b = []
print(a is b)
print(id(a))
print(id(b))

#以上示例说明，由于Python缓存了整数和短字符串，因此每个对象只存有一份。比如所有整数1的引用都指向同一对象。
#即使使用赋值语句，也只是创造了新的引用，而不是对象本身。长的字符串和其它对象可以有多个相同的对象，可以使用赋值语句创造出新的对象。
