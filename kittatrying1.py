def fu(a):
    return lambda inside : inside * a

z = fu("a")
x = fu("x")
print(z(10)+x(10))
