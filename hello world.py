'''
这个就是个实验，hello python,youy father is coming 是老子第一次写的python代码。
下面老子将写一个汉诺塔递归。写于2018年12月14号
'''
print('hello python,your father is coming')
def hano(n,a,b,c):
    '''
    汉诺塔的实现
    :param n: 代表n个塔
    :param a: 代表第一个塔，开始的塔
    :param b: 代表第二个塔，中间过渡的塔
    :param c: 代表第三个塔，目标塔
    :return: None
    '''
    if n==1:
        print(a,"-->",c )
        return None
    if n==2:
        print(a,"-->",b)
        print(a,"-->",c)
        print(b,"-->",c)
        return None
    hano(n-1,a,c,b) #把n-1个盘子从a塔借助于c塔，挪到b塔上去
    print(a,"-->",c)#把n-1个盘子从b塔借助于a塔，挪到c塔上去
    hano(n-1,b,a,c)
a="A"
b="B"
c="C"


n=3
hano(n,a,b,c)