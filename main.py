import math
class square_function:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def resolve(self):
        if self.a != 0:
            delta = (self.b)**2 - 4 * self.c * self.a
            if delta > 0:
                x1 = (-self.b - math.sqrt(delta)) / (2 * self.a)
                x2 = (-self.b + math.sqrt(delta)) / (2 * self.a)
                return print(f"This is square function, its x1 = {x1:0.2f} and x2 = {x2:0.2f}")
            elif delta == 0:
                x0 = (- self.b) / (2 * self.a)
                return print(f"This is square function, its x0 = {x0:0.2f}")
            else:
                return print("This function has no zero places")
        else:
            if self.b == self.a:
                if self.c == self.b:
                    return print("This function has infinitely many solutions.")
            x0 = -(self.c)/self.b
            return print(f"This is linear function and its zero place is: {x0:0.2f}")
first = square_function(0,2,1)
first.resolve()
second = square_function(1,2,1)
second.resolve()
third = square_function(1,3,1)
third.resolve()
forth = square_function(2,1,1)
forth.resolve()
endless = square_function(0,0,0)
endless.resolve()