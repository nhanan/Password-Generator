from random import randint

abc = 'abcdefghijklmnopqrstuvxyz'
abcCap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '1234567890'
sym = "~`!@#$%^&*()_-+={[}]|\:;\"'<,>.?/"

pLength = 400
symbols = True

dict = {0: abc, 1: abcCap, 2: num, 3: sym}

def passwordGenerator():
    pwd = []
    wtf=""
    for i in range(0, pLength):
        randDict = randint(0, len(dict) - 1)
        randKey = randint(0, len(dict[randDict]) - 1)
        pwd.append(dict[randDict][randKey])
    return(wtf.join(pwd))

print(passwordGenerator())