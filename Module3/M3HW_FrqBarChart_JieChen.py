# Display Frequency in a bar chart
# 4/1/20
# CSC221 M3HW – FrqBarChart
# Jie Chen

from textblob import TextBlob
from nltk.corpus import stopwords
from pathlib import Path
from operator import itemgetter
import pandas as pd

# Creating the blob
blob = TextBlob(
    Path(r"C:\Users\jiech\Documents\GitHub\CSC-221\Module3\RomeoAndJuliet.txt").read_text(encoding="utf-8"))

# Removing Stop words
stop_words = stopwords.words("english")
items = [item for item in blob.word_counts.items() if item[0]
         not in stop_words]

# Sort the words                  sorts by item[1] the frequency
sorted_items = sorted(items, key=itemgetter(1), reverse=True)
top20 = sorted_items[1:21]

# Plotting the data
df = pd.DataFrame(top20, columns=['word', 'count'])
axes = df.plot.bar(x='word', y='count', legend=False)
