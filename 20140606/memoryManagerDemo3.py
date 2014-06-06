#! /usr/bin/env python
# coding: utf-8
# 容器对象的引用可能构成很复杂的拓扑结构。我们可以用objgraph包来绘制其引用关系

x = [1, 2, 3]
y = [x, dict(key1=x)]
z = [y, (x, y)]

import objgraph
#objgraph.show_refs([x], filename='ref_topo_x.png')
#objgraph.show_refs([y], filename='ref_topo_y.png')
#objgraph.show_refs([z], filename='ref_topo_z.png')

from sys import getrefcount
print getrefcount(x)
print getrefcount(y)
print getrefcount(z)
