class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
        else:
            print(f"{employee} is not in {self.name} department.")

    def display_employees(self):
        print(f"Employees in {self.name} department:")
        for employee in self.employees:
            print(employee)


# Example usage:
if __name__ == "__main__":
    # Creating a department
    hr_department = Department("HR")

    # Adding employees to the department
    hr_department.add_employee("Alice")
    hr_department.add_employee("Bob")
    hr_department.add_employee("Charlie")

    # Displaying employees in the department
    hr_department.display_employees()

    # Removing an employee from the department
    hr_department.remove_employee("Bob")

    # Displaying employees after removal
    hr_department.display_employees()