# Display Frequency in a bar chart
# 4/1/20
# CSC221 M3HW – FrqBarChart
# Jie Chen


# No user Input
# The program analyzes the occourence of each word in romeo and juliet
# Creates a bar graph that shows frequency
# Creates a worldcloud with the highest frequency word the largest


# Part 1
from textblob import TextBlob
from nltk.corpus import stopwords
from pathlib import Path
from operator import itemgetter
import pandas as pd

# Part 2
import imageio
from wordcloud import WordCloud

# Creating the blob
blob = TextBlob(
    Path(r"RomeoAndJuliet.txt").read_text(encoding="utf-8"))

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

# Part 2
mask_image = imageio.imread('mask_star.png')
wordcloud = WordCloud(width=1000, height=1000,
                      colormap='prism', mask=mask_image, background_color='white')
wordcloud = wordcloud.generate(str(top20))
wordcloud = wordcloud.to_file('RomeoAndJulietHeart.png')
