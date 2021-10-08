i=0
while i<5:
    print(' '*(4-i),end=' ')
    j=0
    while j-i <i*2:
        if (j+1) >(i+1):
            print((i*2)-j+1 ,end=' ')
        else:
            print(j+1,end=' ')
        j+=1
    print( )
    i+=1
