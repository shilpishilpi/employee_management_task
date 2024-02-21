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


def add_department(company, department_name):
    company.add_department(department_name)


def remove_department(company, department_name):
    company.remove_department(department_name)


def display_departments(company):
    company.list_departments()


# Example usage:
if __name__ == "__main__":
    # Creating a company
    company = Company()

    # Adding departments to the company using functions
    add_department(company, "HR")
    add_department(company, "Finance")
    add_department(company, "IT")

    # Displaying departments in the company using function
    display_departments(company)

    # Removing a department from the company using function
    remove_department(company, "Finance")

    # Displaying departments after removal using function
    display_departments(company)