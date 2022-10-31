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

emp1 = Employee("Louis", "Agyapong", 23000)
emp2 = Employee("Zion", "Agyapong", 67000)
Employee.raise_amount = 1.05
emp1.raise_amount = 1.07

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp1.__dict__)
print(emp2.raise_amount)
print(Employee.num_of_emps)