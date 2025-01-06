indian=["samosa","jalebi","poha"]
italian=["pasta","pizza","meatball"]
chinese=["fried rice","pot rice"]

dish=input("enter a dish name: ")

if dish in indian:
    print("indian")
elif dish in italian:
    print("italian")
elif dish in chinese:
    print("chinese")
else:
    print("not in menu")
    
# for loop

exp=[1,2,3,6,8]

total=0
for item in exp:
    total+=item

for i in range(5):
    print(i)
 
for i in range(1,5):
    print(i)
    
for i in range(len(exp)):
    print('month',i+1,'expense',exp[i])
    total+=exp[i]
print(total)

i=1
while i<=5:
    print(i)
    i+=1
