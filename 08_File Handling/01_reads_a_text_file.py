"""
Problem 1: Write a program that reads a text file, counts the number of lines, words, and
characters, and writes these counts to a new file.
"""

def count_file_content(file_path, output_file):
    with open(file_path, 'r') as file:
        content = file.read()
        lines = content.splitlines()
        words = content.split()
        characters = len(content)

    with open(output_file, 'w') as out_file:
        out_file.write(f"Lines: {len(lines)}\nWords: {len(words)}\nCharacters: {characters}")

count_file_content('input.txt', 'output.txt')