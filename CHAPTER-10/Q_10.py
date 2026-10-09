class Employee:
    def __init__(self, name, age, salary, department):
        self.name = name
        self.age = age
        self.salary = salary
        self.department = department
    def work(self):
        print(self.name, "is working.")
    def calculate_salary(self):
        print("Salary:", self.salary)
    def take_leave(self):
        print(self.name, "is on leave.")
employee = Employee("Subrat", 22, 1200000, "IT")
employee.work()
employee.calculate_salary()
employee.take_leave()