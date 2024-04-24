class A:
    def __init__(self, a):
        self.a = a
    def __add__(self, other):
        return self.a +other.a
    # def __subtract__(self, other):
    #     return self.a - other.a

x = A(5)
y = A(6)
print(x+y)
# print(x-y)