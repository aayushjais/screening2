n=int(input("enter a no: "))


for i in range(1,2*n):
    if i%2!=0:
        if i%5!=0:
            print(i,end=", ")
        else:
            print(i+2,end=', ')
