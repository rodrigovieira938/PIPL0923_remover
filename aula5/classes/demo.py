
def f1():
    f3()
    print("f1")

def f2():
    f1()
    print("f2")

def f3():
    print("f3")

f2()