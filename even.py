"""
n=int(input("Enter a number: "))

for i in range(1,n+1):
    if i%2==0:
        print(i)
    """
"""
no=[15, 20, 25, 30, 35, 40, 45, 50]
for i in range(len(no)):
    
        print(no[i])    
"""

"""
str="Coding Blocks"
for i in range(len(str)):
    print(str[i])
"""

"""
number=[1,2,3,4,5]
for i in range(-1,-len(number)-1,-1):
    print(number[i])
"""

#Printing table 2 to 5

number=[2,3,4,5]
for i in range(2,6):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print("Next Table ")
    