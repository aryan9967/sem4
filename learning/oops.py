# class Employee:
#     salary = 89
#     def getsalary(self):
#         return self.salary
    
# rohan = Employee()
# print(rohan.salary)
# print(rohan.getsalary())

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
rohan = Employee("rohan", "12000")
print(rohan.name)
print(rohan.salary)

aryan = Employee("aryan", "120000")
print("aryan name: ", aryan.name)
print("aryan salary: ", aryan.salary)