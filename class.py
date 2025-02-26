#class

class Human:
    # initialises the attributes of class once the object is created.
    #self means the class itself
    #No, the __init__ function is not strictly necessary when writing a class in Python. However, it serves an important purpose: it initializes an object’s attributes when the object is created. If a class does not define an __init__ method, the default constructor (provided by Python) is used, which performs no special initialization.
    def __init__(self,name,occupation):
        #self.name and self.occupation are the attributes of the class
        self.name=name
        self.occupation=occupation
        
    def do_work(self):
        if self.occupation=="tennis player":
            print(self.name,"plays tennis")
        elif self.occupation=="actor":
            print(self.name,"actor")
            
    def speaks(self):
        print(self.name,"says howare you")
        
        
tom=Human("tom","actor")

tom.do_work()
tom.speaks()        

mihir=Human("mihir","tennis player")

mihir.do_work()
mihir.speaks()
        