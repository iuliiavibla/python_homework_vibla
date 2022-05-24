def compareabcwhile(a, b, c, history):
    while a < b:
        print("bad news")
        a = a + c
        history = history + " " + str(a)
    else:
        print("good news")
        print("Increment history = " + history)


a1 = int(input("enter any number"))
b1 = int(input("enter any number"))
c1 = int(input("enter any number"))
compareabcwhile(a1, b1, c1, "")

