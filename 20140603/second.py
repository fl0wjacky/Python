#coding:utf-8

import module.first
for i in range(10):
	module.first.laugh()

#import methods
#	import a as b 引入模块a,并将模块a重命名为b
# 	from a import obj1 从模块a中引入obj1对象，调用a中的对象时，我们不用再说明模块，即直接使用对象，而不是a.obj1
#	from a import * 从模块a中引入所有的对象。调用a中的对象时，我们不用再说明模块，即直接使用对象，而不是a.对象
# 	可以把功能相似的模块放在同一个文件夹中（比如this_dir),构成一个模块包。通过
#		import this_dir.module
#		引入this_dir文件夹中的module模块
#盖文件夹中必须包含一个__init__.py的文件，提醒Python,该文件夹为一个模块包。__init__.py可以是一个空文件。
