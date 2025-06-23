import random

class Guess:
 
    def greeting(self):
        self.name = input("What is your name? ")
    
    def guess_game(self):
        num = random.randint(1,50)
        chances = 10
        guesses = 0

        while guesses < chances: 
            guesses += 1
            self.prompt = int(input(f"Can you guess the number, {self.name}? "))
            
            if self.prompt == num:
                print(f"You guessed it correctly! The correct number is {num}. You guessed it in {guesses} attempts!")
                break
            elif guesses >= chances and self.prompt != num:
                print(f"Try again! The number was {num}.")
            elif self.prompt > num:
                print("You've guessed too high. Try a lower number.")
            elif self.prompt < num:
                print("You've guessed too low. Try a higher number.")

guess = Guess()
guess.greeting()
guess.guess_game()
        
