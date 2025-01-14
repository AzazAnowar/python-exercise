"""
Implement a function to validate and extract phone numbers from a text
using a regular expression. Assume phone numbers are in the format (123) 456-7890.
"""


import re

def extract_phone_numbers(text):
    phone_pattern = r'\(\d{3}\) \d{3}-\d{4}'
    return re.findall(phone_pattern, text)

text = "Contact us at (123) 456-7890 or (987) 654-3210."
print("Phone Numbers:", extract_phone_numbers(text))
