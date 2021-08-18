
#Initialize the two dictionaries
meaningDictionary = {}
sizeDictionary = {}

meaningDictionary["orange"] = "A Fruit"
sizeDictionary["orange"] = 5

meaningDictionary["cabbage"] = "A vegetable"
sizeDictionary["cabbage"] = 10

meaningDictionary["tomato"] = "Widely contested"
sizeDictionary["tomato"] = 5

print("What definition do you seek?")
query = input()
print("The size of " + query + " is " +str(sizeDictionary[query]) + ", it means: " + meaningDictionary[query])
