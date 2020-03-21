from M2PRO_Person_JieChen_Class import Employee
from M2PRO_Person_JieChen_File import write_to_file, read_file


def menu():
    print("""
    1) Enter Employee info
    2) Read Employee Info
    3) Exit
""", end="")

    return int(input("Choice: "))


def enter_Info():
    numOfEmployee = int(input("How many employees do you want to enter? "))
    employees = []
    for employee in range(numOfEmployee):
        fn = input(f"Input first name for employee {employee+1}: ").title()
        ln = input(f"Input last name for employee {employee+1}: ").title()
        pos = input(f"Input position for employee {employee+1}: ").title()
        full_part = input(
            f"Input full/part time for employee {employee+1}: ").title()
        salary = input(f"Input salary for employee {employee+1}: ")
        employees.append(Employee(fn, ln, pos, full_part, salary))
        print("")
    write_to_file(employees, "employee.txt")


def Read_Info():
    pass


def main():
    choice = menu()
    while choice != 1 and choice != 2:
        choice = menu()
    if choice == 1:
        enter_Info()
    elif choice == 2:
        pass


main()
