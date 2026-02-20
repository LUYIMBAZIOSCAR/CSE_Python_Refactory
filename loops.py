# Loops
# A loop is a block of code that tells a computer to 
# continuously do something until a certain condition is false
# Examples
# For loop 
# While loop
# A switch statement

# for loop
numbers=[1,2,3,4,5]

for i in numbers:
    if i % 2==0:
        print(i)
print("****")
for i in numbers:
    if i % 2 !=0:
        print(i)

names=['oscar','luyimbazi']

for name in names:
    if name=='oscar':
        print(name)
    else:
        print("Name was not found")