# Handling Files
# 3/12/20
# M1HW1_FilesExceptions
# Jie Chen

# The program displays a menu
# The user picks a choice
# The program should act depending on what choice the user enters
# 1. Display First Seven Rows
# 2. Display Last Seven Rows
# 3. Calculate Descriptive Statistics for “Carat”
# 4. Calculate Descriptive Statistics for “Cut”, “Color” and “Clarity”
# 5. Display Unique Category Values for “Cut”, “Color” and “Clarity”
# 6. Display Histogram of each Numerical Column
# 7. Exit Program


import pandas as pd


def menu():
    """
    This function displays a menu and returns the choice as an integer 
    """

    print("""
    Menu
    1. Display First Seven Rows
    2. Display Last Seven Rows
    3. Calculate Descriptive Statistics for “Carat”
    4. Calculate Descriptive Statistics for “Cut”, “Color” and “Clarity”
    5. Display Unique Category Values for “Cut”, “Color” and “Clarity”
    6. Display Histogram of each Numerical Column
    7. Exit Program
    """)
    while True:
        try:
            return int(input("Enter Your Choice: "))
        except:
            print("please enter a number!")


def task_9_16(choice):
    """
    This function takes in a choice and do whatever the choice instructs to do
    """
    try:
        df = pd.read_csv("diamonds.csv", index_col=0)
    except FileNotFoundError:
        print("file not found!")
    else:
        # First 7 Rows
        if choice == 1:
            print(df.head(7))

        # Last 7 Rows
        elif choice == 2:
            print(df.tail(7))

        # Describe carat
        elif choice == 3:
            print(df.loc[:, "carat"].describe())

        # Describe cut, color, and clarity
        elif choice == 4:
            print(df.loc[:, ["cut", "color", "clarity"]].describe())

        # Display the Unique category of cut, color, clarity
        elif choice == 5:
            uniqueCuts = df.loc[:, "cut"].unique()
            uniqueColors = df.loc[:, "color"].unique()
            uniqueClarities = df.loc[:, "clarity"].unique()
            print(f"Cuts: {uniqueCuts}")
            print(f"Colors: {uniqueColors}")
            print(f"Clarities: {uniqueClarities}")

        # Histogram
        elif choice == 6:
            df.hist(column=["carat", "depth", "table", "price", "x", "y", "z"], figsize=(
                20, 20), xlabelsize=10, ylabelsize=15)
        else:
            print("Bye!", end="")


def main():
    while True:
        choice = menu()
        while choice < 0 or choice > 7:
            print("Please Enter a Valid Choice!")
            choice = menu()
        task_9_16(choice)
        if choice == 7:
            break


main()
