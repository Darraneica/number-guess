import random 

class Game:
       
    def guessNum(self):
        self.random = random.randint(1, 10)
        count = 0
        attempts = 4

        while attempts > count:
            count += 1

            number = int(input("Guess the number: ")) # the input method where users add their guess.

            if number == self.random: # if the number matches the selected guess
                print(f"Correct! The number is {self.random}. It took you {attempts} attempts.") # print the number + attempts
                break # break is used to stop the loop since the gueess was answered correctly.
            elif number > attempts and number != self.random: # if number exceeds the 4 attempts and the number is not the right guess
                print(f"Game over. The number was {self.random}.") # print the game is over + print the correct number
            elif number > self.random: # if your number is higher than the selected number 
                print("Your guess it too high. Try again.") # print too high
            elif number < self.random: # if your number is lower than the selected number
                print("Your guess is too low. Try again.") # print too low
                        

guess_num = Game() # calls the Game class with an object
print(guess_num.guessNum()) # prints the object + method
