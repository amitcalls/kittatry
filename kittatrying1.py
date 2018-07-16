import numpy as np
l1 = np.array([[[1, 2, 3], [4, 5, 6], [7,8,9]],[[10, 20, 30], [40, 50, 60], [70,80,90]]])
# l2 = np.array([[6],[7],[8],[9],[10]])
# Sum = l1 + l2
x=y=z=0
while z<=1:
    x=0
    while x<=2:
        y=0
        while y<=2:
            print("this is depth: ", z, "row: ", x, "column: ", y, " = ", l1[z,x,y])
            y+=1
        x+=1
    
    z+=1
    

# import pandas as pd
# a = {"a":10, "b":5, "c":1, "d":0}
# b = pd.Series(a)
# b.rename(index = {"a" : "v"}, inplace = True )
# c = b[["v", "c"]]
