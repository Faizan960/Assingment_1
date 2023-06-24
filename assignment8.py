class PrivateAccessError(Exception):
    
    def _init_(self,msg):
        super()._init_(msg);

class A:
    
    __a=None 
    _b=None  
    c=None   
    
    def _init_(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    
    def display(self):
        print("a =",self.a)
        print("b =",self.b)
        print("c =",self.c);

class B(A):

    def _init_(self,a,b,c):
        super()._init_(a,b,c)
    
    def display(self):
        print("[Printing by display() of 'B' class :-]");

        try:
           if(self.a==self.a):
               raise PrivateAccessError("Private member cannot be access.")
           else:
               print("a =",self.a);
        except PrivateAccessError as pae:
           print(f"{type(pae)._name_} : {pae.args[0]}");
        
        print("b =",self.b)
        print("c =",self.c)
        print()
        print("[Printing by display() of 'A' class :-]");
        super().display();
        

b=B(10,20,15)
b.display()