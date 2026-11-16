import random
from enum import Enum

class GuessResult(Enum):
    Correct = 0
    Low = 1
    High = 2

class GuessingGame:
    def __init__(self):
        self.randNum = self.RandomNum()
        self.Attempts = 0
    
    def RandomNum(self):
        return random.randint(0, 100)
        
    def check_guess(self, guess):
        if guess == self.randNum:
            return GuessResult.Correct
        elif guess < self.randNum:
            return GuessResult.Low
        else:
            return GuessResult.High

    def run(self):
        result = None
        while result != GuessResult.Correct:
            try:
                guess = int(input("Enter a number: "))
            except ValueError:
                print("Enter Valid Number")
                continue
            self.Attempts += 1
            
            result = self.check_guess(guess)
            
            if result == GuessResult.Low:
                print("Low")
            elif result == GuessResult.High:
                print("High")
        
        print(f"Correct ansured in {self.Attempts} attempts.")
        
def game():
    return GuessingGame()