class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@company.com"

        Employee.num_of_emps += 1

    def fullname(self) -> str:
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def fromstring(cls, emp_str):
        """Alternative constructors"""
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def isworkday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self) -> str:
        return f"{self.fullname()} {self.pay}"

    def __str__(self) -> str:
        return f"{self.fullname()} {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first: str, last: str, pay: int, prog_lang) -> None:
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first: str, last: str, pay: int, employees: list = None) -> None:
        super().__init__(first, last, pay)
        self.employees = employees
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
            print(employee.fullname())


dev_1 = Developer("Louis", "Agyapong", 8000, "Python")
dev_2 = Developer("Nana", "Osei", 6000, "Java")

mger_1 = Manager("Kesse", "Norma", 12000, [dev_1])
print(mger_1)
print(mger_1.__init__)
print(dev_1 + dev_2)
print(len(mger_1))

# print(mger_1.email)

# mger_1.add_employee(dev_2)
# mger_1.print_employees()
# print(isinstance(mger_1, Manager))
# print(dev_1.fullname())
# print(dev_1.prog_lang)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(help(Developer))
