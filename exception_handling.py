#exception handling

a=int(input("enter first no: "))
b=int(input("enter second number: "))

try:
	div=a/b
except Exception as e:
    print("exception",e)
    div=None
    
print(div)
    
   

# raise exception
    
try:
    raise Exception("exception")
except Exception as e:
    print(e)

try:
    raise MemoryError("memory error")
except MemoryError as e:
    print(e)
finally:
    # used to do cleanup
    print("code will run even if there is an exception")
    
# user defined exception

class Accident(Exception):
    def __init__(self,msg):
        self.msg=msg
        
    def print_exception(self):
        print(self.msg)


try:
    raise Accident("user defined exception")
except Accident as e:
    e.print_exception()