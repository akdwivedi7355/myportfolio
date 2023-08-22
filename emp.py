class Employeeone:
    def __init__(self,name,age,pas,bonus):
        self.name=name
        self.age=age
        self.obj_salary=salary(pay,bonus)
    def total_sal(self):
        return self.obj_salary.annual_salary()
emp =Employeeone('Rajat',25,10000,1500)
print(emp.total_sal)