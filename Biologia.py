print("Para verdadeiro digite 1 , para falso digite 0")

semente = int(input("Sua panta tem sementes? "))
vascu = int(input("Sua planta é vascularizada? "))
flor = int(input("Sua planta possui flores? "))

if semente == 1 and vascu == 1 and flor == 1:
    print("Você tem uma angiosperma")
elif flor == 0 and semente == 1:
    print("Você tem uma gimnosperma")
elif vascu == 1:
    print("Você tem uma pteridófita")
else:
    print("Você tem uma briófita")
