lvl = int(input("Digite o lével do Voltorb: "))

if lvl <= 20:
    print("O choque que você levou foi de ", 20+lvl**2, "W")
elif lvl <= 40:
    print("O choque que você levou foi de ", 8000+(lvl - 10)**2, "W")
elif lvl <= 60:
    print("O choque que você levou foi de ", 9000+5*lvl, "W")
elif lvl <= 80:
    print("O choque que você levou foi de ", 9300+2*lvl, "W")
else:
    print("O choque que você levou foi de ", 9500+lvl, "W")