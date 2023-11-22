def checkSize(ask,alphabet)->str:
    while len(var) !=5:
        var= input(ask)
    while True :
        for j in var:
            if j in alphabet:
                return var.upper()
        print("Utilisez seulement des lettres de l'alphabet français")
        var= input(ask)

def checkLetter(guessLetter,tryLetter,guessNum,tryNum):
    if guessLetter == tryLetter and guessNum == tryNum:
        
    
    
a: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word: str = "PATES"
playerWord: str = checkSize("Écrivez un mot de 5 lettres",a)


for i in range (len(word)):
    for j in range (len(playerWord)):
        checkLetter(word[i],word[j],i,j)