a = input().split()

for i in range (len(a)):
    a[i] = int(a[i])

maior1 = (a[0]+a[1]+abs(a[0]-a[1]))//2
maior2 = (maior1+a[2]+abs(maior1-a[2]))//2

print(maior2,"eh o maior")