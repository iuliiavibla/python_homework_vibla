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


a1 = int(input("enter any number"))
b1 = int(input("enter any number"))
c1 = int(input("enter any number"))
text2 = compareabcif(a1, b1, c1)
print(text2)
