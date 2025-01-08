# inheritance


#benefits 
# 1) reuse
# 2) extensibility
# 3) readable

# single inheritance  

class father:
    
    def skill(self):
        print("programming")
        

class mother:
    
    def skill(self):
        print("cooking")
        
        
class child(father,mother):
    
    def skill(self):
        father.skill(self)
        mother.skill(self)
        print("cricket")
        
        

c=child()
c.skill()