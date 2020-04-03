# Exercise 12.6
# 4/2/20
# CSC221 M3Pro – Similarity
# Jie Chen

# No user input
# The program calculates the similiarity between Jonson and Marlowe's work compared to shakespeare.
# The program then display how similiar they are and tells the user who was the most similiar

from pathlib import Path
import spacy

nlp = spacy.load('en')

Jonson = nlp(
    Path(r"Module3\M3PRO\Works\Jonson_EveryManInHisHumor.txt").read_text())
Marlowe = nlp(
    Path(r"Module3\M3PRO\Works\Marlowe_TheJewOfMalta.txt").read_text())
Shakespeare = nlp(
    Path(r"Module3\M3PRO\Works\Shakespeare_Macbeth.txt").read_text())

docs = {"Marlowe": Marlowe, "Johnson": Jonson}
docs_similarity = dict()
for key, doc in docs.items():
    sim = Shakespeare.similarity(doc)
    print(f"{key}: {sim}")
    docs_similarity.update({key: sim})

print(f"{max(docs_similarity)} work is the most similiar to Shakespeare's Macbeth")
