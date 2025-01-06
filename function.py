l1=[1,2,3,4,5]
l2=[2,3,4,7,8]

def sum(l1):
    total=0
    for i in l1:
        total+=i
    print(total)
    
sum(l1)
sum(l2)

# b=0 would be the default value if no b is passed as paramenter
def twosum(a,b=0):
    return a+b
n1=twosum(1,2)
n2=twosum(b=2,a=1)
n3=twosum(1)
print(n1,n2, n3)
#15
# 24
# 3 3 1
