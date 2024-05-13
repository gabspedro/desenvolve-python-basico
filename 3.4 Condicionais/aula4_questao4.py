distancia = int(input("Qual a Ditância a ser Pecorrida? "))
kg = int(input("Quantos KG? "))

if distancia <=100 and kg >10:
    d1 = kg * 1 + 10
elif distancia <=100:
    d1 = kg * 1

if distancia >100 <301 and kg >10:
    d1 = kg * 1.50 + 10
elif distancia >100 <301:
    d1 = kg * 1.50

if distancia >300 and kg >10:
    d1 = kg * 2 + 10
elif distancia >300:
    d1 = kg * 2

print(distancia)
print(kg)
print(f"O valor será: R${d1}")