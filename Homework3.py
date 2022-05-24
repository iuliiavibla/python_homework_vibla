a = int(input("Enter any number a"))
b = int(input("Enter any number b"))
c = int(input("Enter any number c"))
history = ""
while a < b:
    print("bad news")
    a = a + c
    history = history + " " + str(a)
else:
    print("good news")
    print("Increment history = " + history)


