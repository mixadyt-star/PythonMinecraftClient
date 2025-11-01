class DataType:
    def __init__(self, inp):
        self.inp = inp

    def __repr__(self):
        return self.__class__.__name__ + f"({self.inp})"