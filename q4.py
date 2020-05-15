l1 = []
ec = 0
oc = 0

num = int(input("enter the length of list: "))
for i in range(1,num+ 1):
    val= int(input("Please enter the Value of Element %d : " %i))
    l1.append(val)

for j in range(num):
    if(l1[j] % 2 == 0):
        ec = ec + 1
    else:
        oc = oc + 1

print("Total Number of Even Numbers in this List =  ", ec)
print("Total Number of Odd Numbers in this List = ", oc)
