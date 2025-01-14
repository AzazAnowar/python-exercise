"""
Implement a program that calculates and displays the sum of the series
1^3+2^3+3^3+⋯+n^3 for a given n using a for loop.
"""

n = int(input("Enter the N\'th position : "))
#print(type(n))
sum = 0

for i in range(1, n+1):
    #sum = sum + pow(i,3)
    sum += i**3
    # [**] double star represent power

print(sum)