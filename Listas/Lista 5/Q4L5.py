val = {'1':2, '2':5, '3':5, '4':4, '5':5, '6':6, '7':3, '8':7, '9':6, '0':6}
n = int(input())
led = []
for i in range (n):
    led.append(str(input()))
for c in led:
    soma = 0
    for j in c:
        soma += val[j]
    print(f"{soma} leds")