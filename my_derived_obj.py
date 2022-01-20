import my_object

class MyDerivedObj(MyObject):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return self.greeting
