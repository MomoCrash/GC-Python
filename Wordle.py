import random

def checkSize(ask,alphabet)->str:
    var:str=""
    while len(var) !=5:
        var= input(ask)
    while True :
        if all (j in alphabet for j in var):
                return var.upper()
        print("Utilisez seulement des lettres de l'alphabet")
        var= input(ask)

def checkLetter(guessLetter,tryLetter,guessNum,tryNum)->str:
    if guessLetter == tryLetter and guessNum == tryNum:
        return '\033[0;32m'
    elif guessLetter==tryLetter and guessNum != tryNum:
        return "\033[38;2;255;165;0m"
    else :
        return "\033[1;38m"
    
    
a: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word: str = "PATES"


playerWord: str = checkSize("Écrivez un mot de 5 lettres : ",a)
checkList:list = []

for i in range (len(word)):
    for j in range (len(playerWord)):
        checkList.append(checkLetter(word[i],word[j],i,j))

print(checkList)
for i in range(len(playerWord)):
    print(checkList[i],playerWord[i],'\x1b[0m')
    