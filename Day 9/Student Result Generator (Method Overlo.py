#Student Result Generator (Method Overloading Concept)#
class Result:
    def calculate(self, a, b, c=None):
        if c is None:
            print("Average:", (a + b) / 2)
        else:
            print("Average:", (a + b + c) / 3)

r = Result()
r.calculate(80, 90)
r.calculate(70, 85, 90)