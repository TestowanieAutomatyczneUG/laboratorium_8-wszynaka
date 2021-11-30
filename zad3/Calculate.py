class Calculate:
    def dividingints(self, x, y):
        if type(x) == int and type(y) == int:
            return x/y
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))
