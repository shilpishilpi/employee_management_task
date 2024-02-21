class Employee:
    def __init__(self, name, emp_id, title, department):
        self.name = name
        self.emp_id = emp_id
        self.title = title
        self.department = department

    def __str__(self):
        return f"Employee Name: {self.name}\nEmployee ID: {self.emp_id}\nTitle: {self.title}\nDepartment: {self.department}"

# Example usage:
if __name__ == "__main__":
    emp = Employee("John Doe", "E123", "Software Engineer", "Engineering")
    print(emp)