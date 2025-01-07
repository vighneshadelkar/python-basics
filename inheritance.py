# inheritance


#benefits 
# 1) reuse
# 2) extensibility
# 3) readable

# single inheritance  

class vehicle:
    
    def general_usage(self):
        print("driving")
        

class car(vehicle):
    
    def __init__(self,colour):
        self.wheels=4
        self.colour=colour
        
    def specific_usage(self):
        self.general_usage()
        print("road trip")
        
        
class truck(vehicle):
    
    def __init__(self,colour):
        self.wheels=6
        self.colour=colour
        
    def specific_usage(self):
        # self.general_usage()
        print("logistics")
        
        

c=car("red")
t=truck("blue")

c.general_usage() #driving
c.specific_usage() #road trip when we add self.general_usage() we also print driving when we call specific_usage()

t.specific_usage() #logistics

print(isinstance(c,car)) #true

print(issubclass(car,vehicle)) #true
