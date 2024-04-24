def dictionary(dict1):
    act_dict = vars(dict1)
    return act_dict
class book:
    def __init__(self, name, price):
        self.name = name
        self.price = price

a = book("The Wise Man's Fear", 300)
print(dictionary(a))