class Employee:
    def __init__(self, name, emp_id, title, department):
        self.name = name
        self.emp_id = emp_id
        self.title = title
        self.department = department

    def __str__(self):
        return f"Name: {self.name}, ID: {self.emp_id}"

    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Title: {self.title}")
        print(f"Department: {self.department}")

# Example usage:
if __name__ == "__main__":
    emp = Employee("John Doe", "E123", "Software Engineer", "Engineering")
    print(emp)  # This will print the employee's name and ID
    emp.display_details()  # This will print all details of the employee