class Employee:
    def __init__(self, name, emp_id, title, department):
        self.name = name
        self.emp_id = emp_id
        self.title = title
        self.department = department

    def display_details(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Title:", self.title)
        print("Department:", self.department)

    def __str__(self):
        return f"{self.name} (ID: {self.emp_id})"


# Example usage:
if __name__ == "__main__":
    emp1 = Employee("John Doe", 1001, "Software Engineer", "Engineering")
    emp2 = Employee("Jane Smith", 1002, "HR Manager", "Human Resources")

    print("Employee Details:")
    emp1.display_details()
    print()

    print("Employee Representation:")
    print(emp1)