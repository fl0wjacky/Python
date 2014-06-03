#! /usr/bin/env python
# coding:utf-8
#lambda函数
func = lambda x,y:x+y
print func(3,4)
#函数作为参数传递
def test(f, a , b):
	print 'test'
	print f(a, b)
test(func, 3, 5)
test((lambda x,y:x**2 + y**2), 6, 9)
#map()的功能是将函数对象依次作用于表的每一个元素
re = map((lambda x: x+3),[1,3,5,6])
print re
re = map((lambda x,y:x+y),[1,2,3],[6,7,9])
print re
#filter()函数的第一个参数也是一个函数对象,它也是将作为参数的函数对象作用于多个元素。如果函数对象返回的是True,则该次的元素被储存于返回的列表中。
def func2(a):
	if a > 100:
		return True
	else:
		return False
print filter(func2, [10,56,101,500])
#reduce()函数将表中的前两个元素（1和2）传递给lambda函数，得到3.该返回值（3）将作为lambda函数的第一个参数，而表中的下一个元素（5）作为lambda函数的第二个参数，进行下一次的对lambda函数的调用...本例相当于:(((1+2)+5)+7)+9
print reduce((lambda x,y:x+y), [1,2,5,7,9])
