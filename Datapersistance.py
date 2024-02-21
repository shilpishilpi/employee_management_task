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

    def to_dict(self):
        return {
            "name": self.name,
            "employees": self.employees
        }

    @classmethod
    def from_dict(cls, data):
        department = cls(data["name"])
        department.employees = data["employees"]
        return department


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

    def to_dict(self):
        return {
            "departments": {name: department.to_dict() for name, department in self.departments.items()}
        }

    @classmethod
    def from_dict(cls, data):
        company = cls()
        for name, department_data in data["departments"].items():
            company.departments[name] = Department.from_dict(department_data)
        return company


def save_company_data(company, filename):
    with open(filename, "w") as file:
        json.dump(company.to_dict(), file, indent=4)


def load_company_data(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return Company.from_dict(data)


def main():
    filename = "company_data.json"
    try:
        company = load_company_data(filename)
        print("Company data loaded successfully.")
    except FileNotFoundError:
        print("No existing company data found.")
        company = Company()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee_to_department(company)
        elif choice == "2":
            remove_employee_from_department(company)
        elif choice == "3":
            display_department_employees(company)
        elif choice == "4":
            add_department(company)
        elif choice == "5":
            remove_department(company)
        elif choice == "6":
            display_departments(company)
        elif choice == "0":
            save_company_data(company, filename)
            print("Company data saved. Exiting the Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()