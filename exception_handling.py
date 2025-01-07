#exception handling

a=int(input("enter first no: "))
b=int(input("enter second number: "))

try:
	div=a/b
except Exception as e:
    print("exception",e)
    div=None
    
print(div)
    