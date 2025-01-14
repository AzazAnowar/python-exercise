"""
Create a program that appends a new line to an existing file and then reads
and displays the entire file content.
"""

def append_and_read_file(file_path, new_line):
    with open(file_path, 'a') as file:
        file.write(f"\n{new_line}")
    with open(file_path, 'r') as file:
        print(file.read())

append_and_read_file('sample.txt', "This is a new line.")