words:list = []
f = open('ods4.txt')
f2 = open('Words.txt', 'w')
words = f.readlines()
for i,j in enumerate(words):
    if len(j)== 6:
        print(j)
        f2.write(j)