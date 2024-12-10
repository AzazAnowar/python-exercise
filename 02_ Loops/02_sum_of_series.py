n = int(input("Enter the N\'th position : "))
#print(type(n))
sum = 0

for i in range(1, n+1):
    sum = sum + pow(i,3)

print(sum)