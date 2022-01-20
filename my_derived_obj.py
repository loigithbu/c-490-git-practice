import my_object

class MyDerivedObj(my_object.MyObject):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return self.greeting
