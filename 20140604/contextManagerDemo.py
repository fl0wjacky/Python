#! /usr/bin/env python
# coding:utf-8
# 上下文管理器(context manager)是Python2.5开始支持的一种语法，用于规定某个对象的使用范围。一旦进入或者离开该使用范围，会有特殊操作被调用（比如为对象分配或者释放内存）。它的语法形式是with...as...

# eg.上下文管理器可以在不需要文件的时候，自动关闭文件。
# without context manager
f = open("new.txt", 'w')
print(f.closed)
f.write('Hello World!')
f.close()
print(f.closed)

#with context manager
with open('new.txt', 'w') as f: # 上下文管理器有隶属于它的程序块。当隶属的程序块执行结束的时候（也就是不在缩进）,
	print(f.closed)				# 上下文管理器自动关闭了文件（我们通过f.closed来查询文件是否关闭。我们相当与适用缩进
	f.write("hello world!")		# 规定了文件对象f的适用范围
print(f.closed)
# 上面的上下文管理器基于f对象的__exit__()特殊方法。当我们适用上下文管理器的语法时，我们实际上要求Python在进入程序块
# 之前调用对象的__enter__()方法，在结束程序块的时候调用__exit__()方法。

#任何定义了__enter__()和__exit__()方法的对象都可以用于上下文管理器。文件对象f是内置对象，已定义好此俩特殊方法，无需自定
class VOW(object):
	def __init__(self, text):
		self.text = text
	def __enter__(self):
		self.text = "I say: " + self.text
		return self
	def __exit__(self, exc_type, exc_value, traceback):
		self.text = self.text + "!"
		#print exc_type
		#print exc_value
		#print traceback

with VOW("I'm fine") as myvow: # __enter__()返回一个对象。上下文管理器会适用这一对象作为as所指的变量。此处为myvow
	print myvow.text
	#raise NameError
print myvow.text #注：__exit__()中有四个参数。当程序块中出现异常(exception),__exit__()的参数中exc_type,exc_value,
				 #traceback用于描述异常。我们可以根据这3个参数进行相应的处理。如果正常运行结束，这3参数都是None

# 上下文管理器(with EXPR as VAR)大致相当与如下流程：
##  with EXPR as VAR:
# VAR = EXPR
# VAR = EXPR.__enter__()
# try:
# 	 BLOCK
# finally:
#	 VAR.__exit__()
