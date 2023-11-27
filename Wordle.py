import random

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"


def ask_word(ask, alphabet) -> str:
    var: str = ""
    while len(var) != 5:
        var = input(ask)
    while True:
        if all(j in alphabet for j in var):
            return var.upper()
        print("Utilisez seulement des lettres de l'alphabet")
        var = input(ask)


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


def game_loop(word: str, alphabet: list):
    while True:
        player_word: str = ask_word("Écrivez un mot de 5 lettres : ", alphabet)

        print_wordle(word, player_word)


def init_game():
    a: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    words: str = ["PATES"]
    word = random.choice(words)

    game_loop(word, a)


while True:
    init_game()

    