"""
Develop a grade calculator that takes a student's percentage as input and
assigns a grade based on the following criteria:
o 90% and above: A
o 80-89%: B
o 70-79%: C
o Below 70%: F
"""

# name = input("Enter Your Name: ")
# print("Your name is :",name)

marks = input("Enter your Marks :")
print("your Marks "+marks+"%")
# print(type(marks))
marksInt = int(marks)

if (marksInt >= 90):
    print("Your grade is A")
elif(marksInt >= 80 and marksInt <= 89):
    print("Your grade is B")
elif(marksInt >= 70 and marksInt<= 79):
    print("Your grade is C")
else:
    print("Your grade is F")