

#Storing a list of numbers the bad way:
print("Input number 1:")
var1 = input()

print("Number 2:")
var2 = input()

print("Number 3:")
var3 = input()

print("Number 4:")
var4 = input()

#A smarter way:
print("Using a list instead")
listOfNumbers = []
currentPos = 1

while (len(listOfNumbers) < 5):
    print("Input number "+str(currentPos)+":")
    currentPos += 1
    listOfNumbers.append(input())

print(listOfNumbers)

print("Numbers in reverse order")

currentPos = len(listOfNumbers)

while (currentPos > 0):
    currentPos -= 1
    print(listOfNumbers[currentPos])

