class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@company.com"

        Employee.num_of_emps += 1

    def get_fullname(self) -> str:
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        return self.pay


emp_1 = Employee("Louis", "Agyapong", 6000)
emp_2 = Employee("Zion", "Agyapong", 10000)

print(emp_1.apply_raise())
emp_1.raise_amount = 1.05
print(emp_1.apply_raise())
print(Employee.num_of_emps)
