#multi-level inheritance
class venkatesh:
    color="white"
    height=5.2
    def work(self):
        print("Lazy")
class bala(venkatesh):
    def job(self):
        print("active")
class naveen(bala):
    def kaam(self):
        print("hyper active")
obj1=venkatesh()
print(obj1.color)
print(obj1.height)
obj2=bala()
print(obj2.color,obj2.height)
obj2.work()
obj2.job()
obj3=naveen()
obj3.work()
obj3.job()
obj3.kaam()


#Multi_level Inheritance
class grandparent:
    def gpdisplay(self):
        print("grand parent method")
class parent(grandparent):
    def pdisplay(self):
        print("parent display method")
class child(parent):
    def cdisplay(self):
        print("child method")
third_gen=child()
third_gen.cdisplay()
third_gen.pdisplay()
third_gen.gpdisplay()

#Hierarchial inheritance
class parent:
    def display(self):
        print("parent class")
class son(parent):
    def show(self):
        print("son class")
class daughter(parent):
    def watch(self):
        print("daughter class")
d=daughter()
d.display()
d.watch()
s=son()
s.display()
s.show()
# s.watch()
# d.show()#it is not possible to access the sibling classes in heirarchial inheritance.

# Multiple inheritance
class father:
    def fdisplay(self):
        print("father class")
class mother:
    def mdisplay(self):
        print("mother class")
class child(father,mother):
    def cdisplay(self):
        print("child class")
c=child()
c.fdisplay(),c.mdisplay(),c.cdisplay()