class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            print(f"{employee} has been removed from the {self.name} department.")
        else:
            print(f"{employee} is not in the {self.name} department.")

    def list_employees(self):
        print(f"Employees in the {self.name} department:")
        for employee in self.employees:
            print(employee)


class Company:
    def __init__(self):
        self.departments = {}

    def add_department(self, department_name):
        if department_name not in self.departments:
            self.departments[department_name] = Department(department_name)
            print(f"{department_name} department has been added to the company.")
        else:
            print(f"{department_name} department already exists in the company.")

    def remove_department(self, department_name):
        if department_name in self.departments:
            del self.departments[department_name]
            print(f"{department_name} department has been removed from the company.")
        else:
            print(f"{department_name} department does not exist in the company.")

    def list_departments(self):
        print("Departments in the company:")
        for department_name in self.departments:
            print(department_name)


# Example usage:
if __name__ == "__main__":
    # Creating a company
    company = Company()

    # Adding departments to the company
    company.add_department("HR")
    company.add_department("Finance")
    company.add_department("IT")

    # Listing departments in the company
    company.list_departments()

    # Removing a department from the company
    company.remove_department("Finance")

    # Listing departments after removal
    company.list_departments()