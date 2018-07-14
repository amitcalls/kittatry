def iq_test(numbers):

    x = 0
    y=numbers.split(" ")
    o = 0
    e = 0

    while x < len(y):
        if int(y[x])%2 == True:
            o+=1
        else:
            e+=1
        x+=1

    z=0
    if o==1:
        while z < len(y):
            if int(y[z])%2 == True:
                return(z+1)
                break
            z+=1
    elif e==1:
        while z < len(y):
            if int(y[z])%2 == False:
                return(z+1)
                break
            z+=1
    else:
        return(0)

    #o = [int(num) for num in y]
# print(iq_test("1 2 3 4"))