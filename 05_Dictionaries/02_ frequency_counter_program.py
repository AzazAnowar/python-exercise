"""
Implement a frequency counter program that counts the occurrence of each
word in a long string, case-insensitively, and displays the top 5 most frequent words
"""

from collections import Counter

def top_words(text, top_n=5):
    words = text.lower().split()
    word_count = Counter(words)
    return word_count.most_common(top_n)

text = "Python is great and Python is fun. Python programming is amazing."
print("Top words:", top_words(text))