import random

# a = list()   # alternative version
# for x in range(0, 6):
#     rwd = random.randint(1, 48)
#     if rwd in a:
#         a.append(rwd)

a = list()
z = 1
while z <= 6:
    rwd = random.randint(1, 48)
    if rwd not in a:
        a.append(rwd)
        z = z + 1


b = list()
print("Wylosuj 6 szczęśliwych liczb, z zakresu od 1 do 48!!!")
x = 1
while x <= 6:
    try:
        inp = int(input(f"Podaj {x} liczbę: "))
        if inp <= 0 or inp >= 49:
            print("Wartość z poza zakresu")
            continue
        elif inp not in b:
            b.append(inp)
            x = x + 1
        else:
            print("Liczba się powtórzyła")
            continue
    except:
        print("Niepoprawna wartość")

print(f"Wylosowane liczby: {a}\nTwoje liczby: {b}")

y = 0
l = "_"
c = list()
for bb in b:
    if bb in a:
        c.append(bb)
        y = y + 1
    else:
        c.append(l)

print(f"Trafiłeś {y} liczbę/by/b, a o to twoje liczby:{c}")

