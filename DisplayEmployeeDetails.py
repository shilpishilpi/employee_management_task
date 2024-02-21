class Employee:
    def __init__(self, name, emp_id, title, department):
        self.name = name
        self.emp_id = emp_id
        self.title = title
        self.department = department

    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Title: {self.title}")
        print(f"Department: {self.department}")

# Example usage:
if __name__ == "__main__":
    emp = Employee("John Doe", "E123", "Software Engineer", "Engineering")
    emp.display_details()