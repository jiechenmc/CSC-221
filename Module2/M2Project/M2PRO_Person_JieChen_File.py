# This file contains functions used to manipulate files
# Work in progress!


def write_to_file(people, file):
    with open(file, "w") as f:
        f.write(
            "FirstName\tLastName\t\t\t\tEmail\t\t\t\tPosition\t\tFull/PartTime\t\t\tSalary\n")
        for person in people:
            f.write(f"{person.get_firstName():<12}{person.get_lastName()}\
                {person.get_email():<5}\t{person.get_position()}\
                {person.get_full_part_time():<15}{person.get_salary()}\n")


def read_file(file):
    try:
        with open(file, "r") as f:
            for line in f:
                print(line)
    except:
        print("file don't exist!")


if __name__ == "__main__":
    from M2PRO_Person_JieChen_Class import Employee
    emp_1 = Employee("Jie", "Chen", "Manager", "Full", "100")
    emp_2 = Employee("Jenny", "Guo", "Waiter", "Part", "100")
    write_to_file([emp_1, emp_2], "employee.txt")

    read_file("employee.txt")
