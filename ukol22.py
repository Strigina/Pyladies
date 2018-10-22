n = int(input("Zadej mi číslo větší než 0: "))
faktorial = 1
base = 2
count = 0
fibonacci1 = 1
fibonacci2 = 1



for i in range (n):
    faktorial = faktorial * (i + 1)
print ("Faktoriál tvého čísla je ", faktorial)

while (n >= base):
    if (n % base == 0) and (n != base):
       count = count + 1
    base = base + 1

if (count != 0) or (n == 1):
    print ("Číslo", n, "není prvočíslo")
else:
    print ("Číslo", n, "je prvočíslo")

count = 0


while count < n:
    print(fibonacci1,end=', ')
    fibonacci_mezihodnota = fibonacci1 + fibonacci2
    fibonacci1 = fibonacci2
    fibonacci2 = fibonacci_mezihodnota
    count = count + 1
