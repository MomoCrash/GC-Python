import random

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"

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
        while not all(j in alphabet for j in var):
            var = input(ask)
    return var.upper()

def check_letter(word, s_word, i):
    if word[i] == s_word[i]:
        return GREEN + s_word[i]
    elif s_word[i] in word:
        return YELLOW + s_word[i]
    else:
        return RED + s_word[i]


def print_wordle(to_guess: str, to_try: str) -> str:
    final_wordle = ""
    for i in range(len(to_try)):
        final_wordle += check_letter(to_guess, to_try, i)
    print(final_wordle+'\x1b[0m')


def game_loop(word: str, alphabet: list,tries: int):
    
    while True:
        player_word: str = ask_word("Écrivez un mot de 5 lettres : ", alphabet)
        print_wordle(word, player_word)
        while tries <6 and player_word != word:
            player_word: str = ask_word("Écrivez un mot de 5 lettres : ", alphabet)
            print_wordle(word, player_word)
            tries+=1
        if tries == 6:
            print("Le mot était",word,"dommage !")
            askReplay()
        else:
            print("Tu as trouvé le mot gg bravo et suce moi")
            askReplay()
        

def init_game():
    a: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    words: list = ["PATES","BOIRE","AHURI","AUTRE", "BURNE", "CADET", "CASER", ]
    word:str = random.choice(words)
    tries:int=0
    game_loop(word, a,tries)


while True:
    init_game()

    