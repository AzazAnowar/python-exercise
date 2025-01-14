"""
Write a dictionary comprehension that maps each word in a sentence to its
length.
"""

sentence = "This is a sample sentence"
word_lengths = {word: len(word) for word in sentence.split()}
print("Word lengths:", word_lengths)
