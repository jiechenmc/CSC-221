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
        fn = input(f"Input first name{employee+1}: ")
        ln = input(f"Input last name{employee+1}: ")
        pos = input(f"Input position{employee+1}: ")
        full_part = input(f"Input full/part time{employee+1}: ")
        salary = input(f"Input salary{employee+1}")
        employees.append(Employee(fn, ln, pos, full_part, salary))
    print(employees)


def Read_Info():
    pass


def main():
    choice = menu()
    if choice == 1:
        enter_Info()
    elif choice == 2:
        pass


menu()
