# Sentiment Analysis
# 4/7/20
# CSC221 M4Pro – Sentiment Analysis
# Jie Chen

import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

# No Userinput
# The program will analyze a news article
# The program will display the sentiment for the news article as a whole and for each sentence
# Analysis will be done with and without the NaiveBayesAnayzer


def PartA():
    """
    This function analyze the sentiment without using NaiveBayesAnalyzer
    """
    url = requests.get(
        "https://www.nytimes.com/2020/04/06/us/coronavirus-schools-attendance-absent.html")
    soup = BeautifulSoup(url.content, "html5lib")

    text = TextBlob(str([p.get_text().strip() for p in soup.find_all("p")]))
    print(f"Sentiment for the whole text: {text.sentiment}")

    for sentence in text.sentences:
        print(f"{sentence}:{sentence.sentiment}")


def PartB():
    """
    This function analyze the sentiment with the NaiveBayesAnalyzer
    """
    url = requests.get(
        "https://www.nytimes.com/2020/04/06/us/coronavirus-schools-attendance-absent.html")
    soup = BeautifulSoup(url.content, "html5lib")

    text = TextBlob(str([p.get_text().strip()
                         for p in soup.find_all("p")]), analyzer=NaiveBayesAnalyzer())
    print(f"Sentiment for the whole text: {text.sentiment}")

    for sentence in text.sentences:
        print(f"{sentence}:{sentence.sentiment}")


def menu():
    """
    Allow the user to choose which analyzer to use!
    """

    print("Please choose which one you want to view first!")
    print("1)Analysis without NaiveBayesAnalyzer")
    print("2)Analysis with NaiveBayesAnalyzer")
    print("3)Exit")
    return int(input("Choice: "))


def main():
    while True:
        choice = menu()
        if choice == 1:
            PartA()
            continue
        elif choice == 2:
            PartB()
            continue
        elif choice == 3:
            print("Bye!")
            break
        else:
            continue


main()
