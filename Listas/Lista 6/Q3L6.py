while True:
    cont, cont1 = 0,0
    try:
        para = input()
        para.split(' ')
        e = para.count('(')
        d = para.count(')')
        for i in para:
            if i == ')':
                cont += 1
            elif i == '(':
                cont1 += 1
            if cont > cont1:
                break
        if cont > cont1:
            print("incorrect")
        elif e == d:
            print("correct")
        else:
            print("incorrect")
    except EOFError:
        break