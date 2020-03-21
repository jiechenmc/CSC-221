from M2PRO_Person_JieChen_Class import Employee
from M2PRO_Person_JieChen_File import write_to_file, read_file

# Entering and Reading records
# 3/20/20
# CSC121 M2HW – Students Class
# Jie Chen

# The program will display a menu with choices
# if 1:
#   prompt the user for how many employees to enter
#   then gather data on that employee
#   make an employee object
#   write the data into employee.txt
# if 2:
#   read the contents of employee.txt
#   if file dont exist:
#       let the user know
# if 3:
# The program terminates


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


def read_Info():
    try:
        read_file("employee.txt")
    except:
        print("File does not exist!")


def main():
    while True:
        choice = menu()
        while choice != 1 and choice != 2 and choice != 3:
            choice = menu()
        if choice == 1:
            enter_Info()
            continue
        elif choice == 2:
            read_Info()
            continue
        elif choice == 3:
            print("Bye!")
            break


main()
