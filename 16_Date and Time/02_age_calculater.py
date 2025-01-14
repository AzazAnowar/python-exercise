"""
Develop a function that takes a birthdate as input and calculates the user's
age, displaying it in years, months, and days.
"""

from datetime import datetime

def calculate_age(birthdate):
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.today()
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    if days < 0:
        months -= 1
        days += (birthdate.replace(month=birthdate.month + 1) - birthdate).days
    if months < 0:
        years -= 1
        months += 12

    return f"{years} years, {months} months, and {days} days"

birthdate = "2000-01-01"
print("Age:", calculate_age(birthdate))
