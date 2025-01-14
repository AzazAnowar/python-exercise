"""
Problem 1: Write a program to capitalize the first letter of every word in a given string
without using built-in methods like title() or capitalize().
"""

def capitalize_words(sentence):
    words = sentence.split()
    capitalized = [word[0].upper() + word[1:] if word else '' for word in words]
    return ' '.join(capitalized)

sentence = "python programming is fun"
print("Capitalized:", capitalize_words(sentence))