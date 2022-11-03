import datetime
import http
from types import NoneType


class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first_name: str, last_name: str, pay: float) -> None:
        """
        The init method runs when a new emplyee is created.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

        Employee.num_of_emps += 1

    @property
    def fullname(self) -> str:
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

    @fullname.setter
    def fullname(self, name: str):
        first_name, last_name = name.split()
        self.first_name = first_name
        self.last_name = last_name

    @fullname.deleter
    def fullname(self):
        print("Delete name")
        self.first_name = None
        self.last_name = None

    @property
    def email(self) -> str:
        return f"{self.first_name.lower()}.{self.last_name.lower()}@company.com"

    def apply_raise(self) -> int:
        self.pay = int(self.pay * self.raise_amount)
        return self.pay

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        """
        Class method is used as alternative constructors.
        """
        first_name, last_name, pay = emp_str.split("-")
        return cls(first_name, last_name, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __add__(self, other):
        return self.pay + other.pay

    def __str__(self) -> str:
        return f"{self.fullname()}, {self.email}"

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.pay}"


class Developer(Employee):
    raise_amount = 1.70

    def __init__(self, first_name: str, last_name: str, pay: float, prog_lang: str) -> None:
        super().__init__(first_name, last_name, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first_name: str, last_name: str, pay: float, employees: list[str] = None) -> None:
        super().__init__(first_name, last_name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for employee in self.employees:
            print(f"'-->' {employee.fullname()}")

    def total_employees_supv(self) -> int:
        total_emp_supv: int = 0
        for employee in self.employees:
            total_emp_supv += 1
        return total_emp_supv


emp1 = Employee("Louis", "Agyapong", 23000)
emp2 = Employee("Zion", "Agyapong", 67000)

emp1.fullname = "Nana Sarpong"
print(emp1.email)
print(emp1.fullname)

# del emp1.fullname
# print(emp1.fullname)


dev1 = Developer("Teddy", "Agudogo", 5000, "Python")
dev1.apply_raise()
dev2 = Developer("Louis", "Agyapong", 10000, "Java")
dev3 = Developer("Nana", "Sarpong", 5000, "R")

# dev2.apply_raise()
# print(f"Name: {dev1.fullname()}, Email: {dev1.email}, Salary: {dev1.pay}, Programming Language: {dev1.prog_lang}")
# print(f"Name: {dev2.fullname()}, Email: {dev2.email}, Salary: {dev2.pay}, Programming Language: {dev2.prog_lang}")
# print(dev1.__dict__)

mgr1 = Manager("Kezia", "Agyapong", 45000, [dev1, dev2, dev3])
mgr2 = Manager("Rita", "Watson", 15000)

# print(mgr1.fullname())
# print(mgr1.email)
# print(mgr1.is_workday(datetime.date(2022, 10, 20)))
# mgr1.print_employees()
# mgr1.remove_employee(dev1)
# mgr1.print_employees()
# print(mgr1.total_employees_supv())
# print(isinstance(mgr1, Developer))
# print(issubclass(Developer, Employee))

# print(mgr1.__str__())
# print(mgr1.__repr__())


# print(help(Developer))

# Employee.raise_amount = 1.05
# Employee.set_raise_amount(1.08)
# emp1.raise_amount = 1.07

# emp_str_1 = "John-Doe-70000"
# my_date = datetime.date(2022, 10, 20)
# print(emp1 + emp2)
# print("test".__len__())
