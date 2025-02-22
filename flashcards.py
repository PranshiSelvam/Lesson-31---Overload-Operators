class flashcards: 
    def __init__(self, word, meaning): 
        self.word = word
        self.meaning = meaning
    def __str__(self): 
        return self.word + "( "+self.meaning+" )"
flash = []
print("Welcome to the Flashcard application!")

while (True): 
    word = input("Enter the word: ")
    meaning = input("Enter the meaning of the chosen word: ")

    flash.append(flashcards(word, meaning))
    option = int(input("Enter 0, if you want to add another Flashcard, else enter 1 to end: "))
    if(option): 
        break
print("\nYour flashcards")
for i in flash: 
    print("~~", i)


