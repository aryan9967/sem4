class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department
    def cal_salary(self):
        print(self.emp_salary)
    def print_emp_details(self):
        print(self.emp_id)
        print(self.emp_name)
        print(self.emp_department)
        print(self.emp_salary)
        
aryan = Employee(12, "aryan maurya", 17000, "IT")
aryan.cal_salary()
aryan.print_emp_details()