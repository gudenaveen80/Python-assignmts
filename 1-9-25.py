class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
    def mul(self,a,b):
        print(a*b)
    def div(self,a,b):
        print(a/b)
        
obj1=calculator(1,2)
obj2=calculator(3,4)

obj1.add(3,5)
obj1.sub(3,7)
obj1.mul(2,7)
obj1.div(16,8)
obj1.model_num=118
print(obj1.model_num)
obj1.made_in="India"
print(obj1.made_in)
obj2.color="Black"
print(obj2.color)
obj2.discount=60
print(obj2.discount)


# In simple terms, self refers to the current instance of the class. It is a way for a method in a class to refer to the object itself, allowing access to its attributes (variables) and methods (functions).