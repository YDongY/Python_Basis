'''
__doc__ : 取类的描述
__module__ : 取模块
__class__ : 显示实例对象由那个类创建
__init__ : 初始化方法
__del__ : 对象删除对象之前调用
__call__ : 实例对象() 自动调用
__dict__ : 检查类和实例对象的属性
__str__ : 获取对象的描述时调用
__getitem__,__setitem__,__delitem__ : obj = Foo()
                                      obj['k1'] 触发__getitem__
                                      obj['k2'] = "ydy" 触发__setitem__
                                      del obj['k1'] 触发 __delitem__
__getslice__,__setslice__,delslice__: 用于切片
'''
