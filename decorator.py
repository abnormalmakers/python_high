"""
    装饰器：不改变原有函数的基础上为函数添加新的功能
    通过闭包实现，原有函数添加上装饰器以后，实际调用时是调用装饰器函数的内部函数
"""
# 闭包实现装饰器
def mydec(fn):
    def fx():
        print('this is mydec add start')
        fn()
        print("this is mydec add stop")
    return fx

def fn():
    print('this is fn')

myfn=mydec(fn)
myfn()


# pythn装饰器
def mydec(fn):
    def fx():
        print('this is mydec add start')
        fn()
        print("this is mydec add stop")
    return fx

@mydec
def fn():
    print('this is fn')

fn()

