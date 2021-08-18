
#Define the function:
def printNumbers(n):
    temp = 0
    stringOut = ""
    while (temp<n):
        stringOut = stringOut + str(temp)
        temp += 1
    print(stringOut)

#The code below is how to use the function
print ("Now let's make a triangle, Input size:")
size = int(input())
temp = 0
while (temp<size):
    printNumbers(temp)
    temp += 1
