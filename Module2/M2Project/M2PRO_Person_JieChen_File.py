def write_to_file(people, file):
    with open(file, "w") as f:
        f.write("First Name\tLast Name\tEmail\tPosition\tFull/Part Time\tSalary")
        for person in people:
            f.write(f"{person.get_firstName()}\t{person.get_lastName()}\
                \t{person.get_email()}\t{person.get_position()}\
                \t{person.get_full_part_time()}\t{person.get_salary()}")


def read_file(file):
    with open(file, "r") as f:
        print(f)


if __name__ == "__main__":
    print("!")
