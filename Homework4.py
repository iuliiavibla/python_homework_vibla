def clientinfo(fullname, age, gender):
    result = "Hello my name is" + fullname + " I`m" + age + " years old, and I`m" + gender
    return result


fullname1 = input("name")
age1 = input("age")
gender1 = input("gender")

result1 = clientinfo(fullname1, age1, gender1)
print(result1)


def compareabcif(a, b, c):
    if a > b:
        text1 = "Сумне повідомлення"
        return text1
    elif b > a:
        if b > c:
            text1 = "Безмежно радісне повідомлення"
            return text1
        else:
            text1 = "Не дуже сумне повідомлення"
            return text1
    elif a == b:
        text1 = "a=b"
        return text1


a1 = int(input('enter any number'))
b1 = int(input("enter any number"))
c1 = int(input("enter any number"))
text2 = compareabcif(a1, b1, c1)
print(text2)


def compareabcwhile(d, f, g, history):
    while d < f:
        print("bad news")
        d = d + g
        history = history + " " + str(d)
    else:
        print("good news")
        print("Increment history = " + history)


d1 = int(input("enter any number"))
f1 = int(input("enter any number"))
g1 = int(input("enter any number"))
compareabcwhile(d1, f1, g1, "")
