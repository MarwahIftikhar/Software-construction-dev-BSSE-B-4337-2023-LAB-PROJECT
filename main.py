from employee import Employee
from storage import load_data, save_data

# --- Utility Functions ---

def add_employee():
    data = load_data()

    emp_id = input("Enter Employee ID: ").strip()
    if any(emp['emp_id'] == emp_id for emp in data):
        print("Employee ID already exists!")
        return

    name = input("Enter Name: ").strip()
    age = input("Enter Age: ").strip()
    department = input("Enter Department: ").strip()
    salary = input("Enter Salary: ").strip()

    if not emp_id or not name or not age.isdigit() or not salary.replace(".", "", 1).isdigit():
        print("Invalid input! Try again.")
        return

    age = int(age)
    salary = float(salary)

    emp = Employee(emp_id, name, age, department, salary)
    data.append(emp.to_dict())
    save_data(data)
    print("Employee added successfully!")

def view_employees():
    data = load_data()
    if not data:
        print("No employees found.")
        return

    print("\n--- Employee List ---")
    print("{:<10} {:<20} {:<5} {:<15} {:<10}".format("ID", "Name", "Age", "Department", "Salary"))
    print("-" * 60)
    for emp in data:
        print("{:<10} {:<20} {:<5} {:<15} {:<10}".format(
            emp['emp_id'], emp['name'], emp['age'], emp['department'], emp['salary']
        ))
    print("-" * 60)

def search_employee():
    data = load_data()
    if not data:
        print("No employees found.")
        return

    query = input("Enter Employee ID or Name to search: ").strip().lower()
    found = [emp for emp in data if emp['emp_id'].lower() == query or emp['name'].lower() == query]

    if not found:
        print("Employee not found.")
        return

    print("\n--- Search Results ---")
    for emp in found:
        print(emp)

def update_employee():
    data = load_data()
    emp_id = input("Enter Employee ID to update: ").strip()

    for emp in data:
        if emp['emp_id'] == emp_id:
            print("Leave field empty to keep current value.")
            name = input(f"Name [{emp['name']}]: ").strip()
            age = input(f"Age [{emp['age']}]: ").strip()
            department = input(f"Department [{emp['department']}]: ").strip()
            salary = input(f"Salary [{emp['salary']}]: ").strip()

            if name: emp['name'] = name
            if age.isdigit(): emp['age'] = int(age)
            if department: emp['department'] = department
            if salary.replace(".", "", 1).isdigit(): emp['salary'] = float(salary)

            save_data(data)
            print("Employee updated successfully!")
            return

    print("Employee ID not found.")

def delete_employee():
    data = load_data()
    emp_id = input("Enter Employee ID to delete: ").strip()

    for i, emp in enumerate(data):
        if emp['emp_id'] == emp_id:
            confirm = input(f"Are you sure you want to delete {emp['name']}? (y/n): ").strip().lower()
            if confirm == "y":
                data.pop(i)
                save_data(data)
                print("Employee deleted successfully!")
            return

    print("Employee ID not found.")

# --- Main Menu ---

def main():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

        choice = input("Choose an option: ").strip().lower()

        if choice in ["1", "add", "add employee"]:
            add_employee()
        elif choice in ["2", "view", "view employees"]:
            view_employees()
        elif choice in ["3", "search", "search employee"]:
            search_employee()
        elif choice in ["4", "update", "update employee"]:
            update_employee()
        elif choice in ["5", "delete", "delete employee"]:
            delete_employee()
        elif choice in ["6", "exit"]:
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
