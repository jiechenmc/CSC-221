# This file contains functions used to manipulate files
# Work in progress!


def write_to_file(people, file):
    with open(file, "w") as f:
        headers = ["FirstName".ljust(12), "LastName".ljust(12),
                   "Email".ljust(25), "Position".ljust(12), "Full/PartTime", "Salary".rjust(15), "\n"]
        f.writelines(headers)
        for person in people:
            f.write(
                f"{person.get_firstName():<12}{person.get_lastName():<12}{person.get_email():<25}{person.get_position():<12}{person.get_full_part_time():<12}{person.get_salary():>15}\n")


def read_file(file):
    try:
        with open(file, "r") as f:
            for line in f:
                print(line)
    except:
        print("file don't exist!")


if __name__ == "__main__":
    from M2PRO_Person_JieChen_Class import Employee
    emp_1 = Employee("Jie", "Chen", "Manager", "Full", "100000000")
    emp_2 = Employee("Jenny", "Guo", "Waiter", "Part", "100")
    write_to_file([emp_1, emp_2], "employee.txt")

    read_file("employee.txt")
