import random

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"

words = []
f= open('Words.txt')
words = f.readlines()

grid = ["-----","-----","-----","-----","-----","-----",]

def askReplay():

    valid_anwsers = ["Y", "y", "n", "N"]
    reponse = input("Voulez-vous rejouer ? Y/n : ")

    while reponse not in valid_anwsers:
        input("Voulez-vous rejouer ? Y/n : ")

    if reponse == "Y" or reponse == "y":
        init_game()

    else:
        print("À bientôt")
        quit()

def ask_word(ask, alphabet) -> str:
    var: str = ""
    while len(var) != 5:
        var = input(ask)
        while not var+'\n' in words:
            var = input(ask)
    return var.upper()

def check_letter(word, s_word, i,tempWordLetters:dict) ->str:
    for j in range(len(s_word)):
        if word[i] == s_word[i]:
            tempWordLetters[s_word[i]] -=1 
            return GREEN + s_word[i]
    if s_word[i] in word and tempWordLetters[s_word[i]] > 0:
        return YELLOW + s_word[i]
    else:
        return RED + s_word[i]


def colorLetter(to_guess: str, to_try: str,wordLetters:dict) -> str:
    final_wordle = ""
    tempWordLetters = wordLetters
    
    for i in range(len(to_try)):
        final_wordle += check_letter(to_guess, to_try, i,tempWordLetters)
    tempWordLetters = wordLetters
    return final_wordle+'\x1b[0m'

def printGrid(grid: list,word:str, k:int):
    grid[k]=word
    for i in grid:
        print(i)

def game_loop(word: str, alphabet: list,tries: int, grid:list, wordLetters:dict):
    
    while True:
        for i in grid:
            print(i)
        player_word: str = ask_word("Écrivez un mot de 5 lettres : ", alphabet)
        coloredWord = colorLetter(word, player_word,wordLetters)
        printGrid(grid,coloredWord,0)
        while tries <6 and player_word != word:
            player_word: str = ask_word("Écrivez un mot de 5 lettres : ", alphabet)
            coloredWord = colorLetter(word, player_word,wordLetters)
            printGrid(grid,coloredWord,tries)
            tries+=1
        
        grid = ["-----","-----","-----","-----","-----","-----",]
        if player_word == word:
            print("Tu as trouvé le mot gg et bravo")
            askReplay()
        else:
            print("Le mot était",word,"dommage !")
            askReplay()
        

def init_game():
    a: list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    word:str = random.choice(words).upper()
    word = word[:len(word)-1]
    tries:int=1
    grid: list = ["-----","-----","-----","-----","-----","-----",]
    wordLetters: dict = {}
    
    for i in a:
        wordLetters[i]=0
    for j in word:
        wordLetters[j]+=1

    print(wordLetters)
    print("word :",word)
    
    game_loop(word,a,tries,grid,wordLetters)
    

while True:
    init_game()

    