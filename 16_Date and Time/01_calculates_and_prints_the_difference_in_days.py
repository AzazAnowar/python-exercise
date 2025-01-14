"""
Write a program that calculates and prints the difference in days, hours, and
minutes between two given dates and times
"""

from datetime import datetime

def time_difference(date1, date2):
    fmt = "%Y-%m-%d %H:%M:%S"
    d1 = datetime.strptime(date1, fmt)
    d2 = datetime.strptime(date2, fmt)
    diff = d2 - d1
    days, seconds = diff.days, diff.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{days} days, {hours} hours, and {minutes} minutes"

date1 = "2023-01-01 08:00:00"
date2 = "2023-01-03 10:30:00"
print("Difference:", time_difference(date1, date2))
