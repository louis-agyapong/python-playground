class Employee:
    def __init__(self, first_name: str, last_name: str, pay: float) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + "." + last_name + "@company.com"

    def fullname(self):
        return f"{emp1.first_name.capitalize()} {emp1.last_name.capitalize()}"

emp1 = Employee("Louis", "Agyapong", 23000)
emp2 = Employee("Zion", "Agyapong", 67000)


print(emp1.fullname())
print(Employee.fullname(emp1))