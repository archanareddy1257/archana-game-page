import random   
import re       

class HangMan:
    def __init__(self, Web = False) -> None:
        self.movies = None
        self.WEB = Web
        with open("./../../src/assets/HangMan/words.txt") as f:
            self.movies = f.read().splitlines()
        random_num = random.randint(0, len(self.movies)-1)
        self.word_chosen = self.movies[random_num]
        self.encoded_word = re.sub('[0-9a-zA-Z]', '-', self.word_chosen)
        self.number_of_lives = self.SetDifficulty()
        # print(self.encoded_word,self.word_chosen)

    def SetDifficulty(self,value = 7):
        if not self.WEB:
            try:
                inp = int(input('select difficulty : \n1: Easy\n2 : Medium\n3 : Hard'))
                if(inp == 1):
                    return 9
                elif inp == 2:
                    return 7
                else:
                    return 5
            except:
                print('interger only')
                return self.SetDifficulty()
        return value
        
    def guess(self,letter, word, encoded):
        # Does the letter exist within the word?
        found = False
        if letter in word:
            found = True
            # Replace the dashes with the letter
            for i in range(0, len(word)):
                if word[i] == letter:
                    encoded = encoded[0:i] + letter + encoded[i+1:len(encoded)]
        return (found, encoded)
    
    def playForward(self):
        pass
    
    def generateWord():
        s = ''
        
        #implement 
                
        return s
    
    def play(self):
        print("\nTime to guess a letter! You have %d lives remaining." % self.number_of_lives)
        while(self.number_of_lives > 0):
            guessed_letter = input("Your guess: ")[:1]
            letter_found, self.encoded_word = self.guess(guessed_letter, self.word_chosen, self.encoded_word)
            if not letter_found:
                self.number_of_lives -= 1
                if self.number_of_lives == 0:
                    print("\nGame over, you lost! :( The word or phrase was '%s'" % self.word_chosen)
                    break
                else:
                    print("\nWhoops! That letter was not found. You now have %d lives remaining." % self.number_of_lives)
                    print(self.encoded_word)
            else:
                if "-" not in self.encoded_word:
                    print("\nHooray! You won with %d lives remaining. The word or phrase was '%s'" % (self.number_of_lives,self.word_chosen))
                    break
                else:
                    print("\nGood job! That letter was found. You still have %d lives remaining." % self.number_of_lives)
                    print(self.encoded_word)

class webGameHangMan:
    def __init__(self) -> None:
        self.Game = HangMan(True)
        
    def gameForwardStep(self, inp=None):
        result = {
            "winner": None,  #Yes/ No 
            "status": "NotStarted",  # GameOver , Playing
            "toGuessWord": self.Game.generateWord(),
            "message": "",
        }
        
        # implement
        
        return result

    def reset(self):
        self.Game = HangMan()
    
    def setDifficulty(self,inp):
        # extact level selected 
        self.Game.SetDifficulty(inp)
        
        
        
def main_cli():
    print('You have 7 chances')
    H = HangMan()
    H.play()
    

def main_web():
    h = HangMan()
    

if __name__ == '__main__':
    main_cli() # Working K
    # main_web() 