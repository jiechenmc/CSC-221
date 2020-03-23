# This file contains functions used to manipulate files


def write_to_file(people, file):
    """
    Writes the data of people into file
    """
    with open(file, "w") as f:
        headers = ["FirstName".ljust(12), "LastName".ljust(12),
                   "Email".ljust(25), "Position".ljust(12), "Full/PartTime", "Salary".rjust(15), "\n"]
        f.writelines(headers)
        for person in people:
            fn = person.get_firstName().ljust(12)
            ln = person.get_lastName().ljust(12)
            email = person.get_email().ljust(25)
            pos = person.get_position().ljust(12)
            full_part = person.get_full_part_time().ljust(12)
            salary = person.get_salary().rjust(15)
            f.write(
                f"{fn}{ln}{email}{pos}{full_part}{salary}\n")


def read_file(file):
    """
    Read file data
    """
    try:
        with open(file, "r") as f:
            for line in f:
                print(line)
    except:
        print("file don't exist!")


if __name__ == "__main__":
    # Testing to see if the 2 functions work
    from M2PRO_Person_JieChen_Class import Employee
    emp_1 = Employee("Jie", "Chen", "Manager", "Full", "100000000")
    emp_2 = Employee("Jenny", "Guo", "Waiter", "Part", "100")
    write_to_file([emp_1, emp_2], "employee.txt")

    read_file("employee.txt")
