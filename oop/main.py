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
        self.pay = int(self.pay * Employee.raise_amount)
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


emp_str_1 = "Zion-Kwaku-5000"
emp_str_2 = "Afia-Sika-4000"
emp_str_3 = "Maame-Afia-30000"
emp_str_4 = "Paa-Yaw-50000"

new_emp_1 = Employee.fromstring(emp_str_1)

print(new_emp_1.fullname())
print(new_emp_1.pay)
