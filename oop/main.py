import datetime
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
        self.email = first_name.lower() + "." + last_name.lower() + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self) -> str:
        return f"{emp1.first_name.capitalize()} {emp1.last_name.capitalize()}"

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

class Developer(Employee):
    pass


emp1 = Employee("Louis", "Agyapong", 23000)
emp2 = Employee("Zion", "Agyapong", 67000)

dev1 = Developer("Teddy", "Agudogo", 5000)
dev1.raise_amount = 1.50

Employee.raise_amount = 1.05
Employee.set_raise_amount(1.08)
emp1.raise_amount = 1.07

emp_str_1 = "John-Doe-70000"

my_date = datetime.date(2022, 10, 20)
print(Employee.is_workday(my_date))
print(dev1.fullname())
print(dev1.apply_raise())

