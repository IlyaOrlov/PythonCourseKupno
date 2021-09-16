def mul(a, b):
    return a * b


class Mul:
    def __init__(self, multiplier):
        self.multiplier = multiplier
        self.state = None

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        if len(args) < 1:
            return None
        return args[0] * self.multiplier


x = mul(10, 20)
#print(x)

m = Mul(10)
y = m(20, 100, 500, 234, s=150)
print(y)
