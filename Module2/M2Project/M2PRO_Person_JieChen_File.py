def write_to_file(people, file):
    with open(file, "w") as f:
        f.write("First Name\tLast Name\t\tEmail\tPosition\tFull/Part Time\tSalary\n")
        for person in people:
            f.write(f"{person.get_firstName():<10}\t{person.get_lastName():>10}\
                \t{person.get_email():<20}\t{person.get_position()}\
                \t{person.get_full_part_time()}\t{person.get_salary()}\n")


def read_file(file):
    with open(file, "r") as f:
        print(f)


if __name__ == "__main__":
    from M2PRO_Person_JieChen_Class import Employee
    emp_1 = Employee("Jie", "Chen", "Manager", "Full", "100")
    emp_2 = Employee("Jenny", "Guo", "Waiter", "Part", "100")
