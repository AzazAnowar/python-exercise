"""
Write a program that takes a string and identifies all valid IP addresses using
regular expressions.
"""


import re

def find_ips(text):
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    return re.findall(ip_pattern, text)

text = "Valid IPs are 192.168.0.1 and 10.0.0.1."
print("IP Addresses:", find_ips(text))
