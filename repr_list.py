class ReprList(list):
    def __init__(self, repr: bool = True, *args, **kwargs):
        self.repr = repr

    def __repr__(self, depth: int = 0):
        if (not self.repr):
            return "..."
        
        if (len(self) == 0):
            return "[]"
        
        repr = "[\n"
        for e in self:
            repr += "\t" * depth
            try:
                repr += e.__repr__(depth=depth)
            except TypeError:
                repr += e.__repr__() + "\n"

        return repr + "\t" * depth + "]"