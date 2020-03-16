# Reading and analyzing a text file
# 3/12/20
# CSC221 M1Pro â€“ FileExceptions
# Jie Chen

# The program displays a menu
# The user then picks what he wants to do
# The program then executes their wishes
#    1. Display Entire Speech
#    2. Display Total Word Count
#    3. Display Total Character Count
#    4. Display Average Word Length
#    5. Display Top Ten Longest Words
#    6. Exit Program


def menu():
    """
    This function displays a menu and returns the user's choice
    """

    print("""MENU
    1. Display Entire Speech
    2. Display Total Word Count
    3. Display Total Character Count
    4. Display Average Word Length
    5. Display Top Ten Longest Words
    6. Exit Program
    """)
    while True:
        try:
            return int(input("Enter your choice: "))
        except ValueError:
            print("Enter a integer please!")


def executor(choice):
    """
    Executes functions based on choice given!
    """

    with open("speech.txt", "r", encoding="utf8") as file:
        if choice == 1:
            displaySpeech(file)
        elif choice == 2:
            displayWordCount(file)
        elif choice == 3:
            displayCharacterCount(file)
        elif choice == 4:
            displayAverageWordLength(file)
        elif choice == 5:
            displayTopTenLongestWords(file)
        else:
            print("Bye!", end="")
        return choice


def displaySpeech(file):
    """
    Prints the whole speech to the console!
    """
    print(file.read())


def displayWordCount(file):
    """
    Prints out the total number of words!
    """
    total = 0
    for line in file:
        words = line.split()
        total += len(words)
    print(f"Total word count is {total}\n")


def displayCharacterCount(file):
    """
    Prints out the total number of characters!
    """
    total = 0
    for line in file:
        words = line.split()
        for word in words:
            total += len(word)
    print(f"The total character count is {total}\n")


def displayAverageWordLength(file):
    """
    Prints out the average word length!
    """
    wordCount = 0
    characterCount = 0
    for line in file:
        words = line.split()
        wordCount += len(words)
        for word in words:
            characterCount += len(word)
    averageWordLength = characterCount / wordCount
    print(
        f"The average word count is {averageWordLength:.0f} ({averageWordLength:.2f})\n")


def displayTopTenLongestWords(file):
    """
    Prints out the top 10 longest words!
    """

    allWords = []
    for line in file:
        words = (word for word in line.split())
        for word in words:
            if word.endswith("."):
                word = word.replace(".", "")
            elif word.endswith(","):
                word = word.replace(",", "")
            if word not in allWords:
                allWords.append(word)
    while len(allWords) > 10:
        allWords.remove(min(allWords, key=len))
    print(f"The 10 longests words are {allWords}\n")


def main():
    while True:
        choice = menu()
        while choice < 0 or choice > 7:
            print("Please enter a valid choice!")
            choice = menu()
        executor(choice)
        if choice == 6:
            break


main()
