def ask_int(question, max=1000000000) -> int:
    reponse=""
    while not reponse.isdigit() or ((int(reponse) < 0) or (int(reponse) >= max)):
        reponse = input(question)
    return int(reponse)

def checkAns(player_input, poss, question):
    while True:
        for i in poss:
            if player_input==i:
                return player_input
        player_input = input(question)
