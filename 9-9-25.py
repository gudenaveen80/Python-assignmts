#encapsulation &data hiding 

class demo:
    __a=10
    _b=100
    def display(self):
        print(self.__a)
        print(self._b)
        print("this is display method")
obj1=demo()
obj1.display()


class demo:
    __a=10
    _b=100
    def __display(self):
        print(self.__a)
        print(self._b)
        print("this is display method")
    def show(self):
        self.__display()
obj1=demo()
obj1.show()