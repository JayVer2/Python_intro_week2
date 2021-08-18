

class cat:
    def __init__(self):
        self.size=40
        self.colour="Blue"
        self.breed="Persian"
    def meow(self):
        print("Meow! I'm a "+self.colour+", "+self.breed+" cat.")

bella = cat()
daisy = cat()

print(bella.size)
print(bella.breed)

#Change this cats breed & colour
daisy.breed = "tabby"
daisy.colour = "black"

bella.meow()
daisy.meow()
