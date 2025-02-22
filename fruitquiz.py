import random
class FruitQuiz: 
    def __init__(self): 
        self.fruits = {'Apple': 'red', 
                       'Orange': 'orange', 
                       'Banana': 'yellow', 
                       'Guava': 'green', 
                       'Blueberry': 'blue', 
                       'Jamun': 'purple', 
                       'Dragon Fruit': 'pink'}
    def quiz(self): 
        while (True): 
            fruit, color = random.choice(list(self.fruits.items()))
            print("What is the color of", fruit)
            answer = input()
            print(answer.lower())
            print(color)
            if(answer.lower()==color): 
                print("Correct!")
            else: 
                print("Wrong!")

            option = int(input("Enter 0 if you want to continue, else enter 1 to end: "))
            if (option): 
                break
print("Welcome to Fruit Quiz")
fq = FruitQuiz()
fq.quiz()

            