# -*- coding: utf-8 -*-
"""PDS Assignment 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d9XOlU1oDdh656K9MPA4TC11iXXUt_n9
"""

import pandas as pd

df = pd.read_csv('/content/sample_data/Corona_NLP_test.csv')

df.head()

"""PART A"""

!pip install nltk

import nltk
nltk.download('punkt')

df['tokens'] = df['OriginalTweet'].apply(lambda x: nltk.tokenize.word_tokenize(x))

df['tokens'][0]

"""PART B"""

nltk.download('stopwords')

from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

df['tokens_without_stopwords'] = df['tokens'].apply(lambda x: [word for word in x if word.lower() not in stop_words])

df['tokens_without_stopwords'][0]

"""PART C"""

import collections
import itertools

all_tokens = list(itertools.chain(*df['tokens_without_stopwords']))

word_counts = collections.Counter(all_tokens)

word_counts['stock']

word_counts['supermarket']

"""PART D"""

!pip install wordcloud

from wordcloud import WordCloud
import matplotlib.pyplot as plt

wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stop_words, 
                min_font_size = 10)

wordcloud.generate_from_frequencies(word_counts)

plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show()

