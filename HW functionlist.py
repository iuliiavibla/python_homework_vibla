from random import randint


def createrandomlist(n, max):
    fulllist = []
    for i in range(n):
        a = randint(0, max)
        fulllist.append(a)
    return fulllist


n1 = int(input("enter any number from 5 till 15"))
max1 = int(input("enter any number"))
fulllist1 = createrandomlist(n1, max1)
print(fulllist1)
