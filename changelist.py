words:list = []
f = open('ods4.txt')
f2 = open('Words.txt', 'w')
a: list= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '\n']

words = f.readlines()
for i,j in enumerate(words):
    if len(j)== 6 and all(h in a for h in j):
        print(j)
        f2.write(j)