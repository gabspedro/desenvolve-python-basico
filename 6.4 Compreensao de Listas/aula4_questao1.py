import random

lista = [random.randint(-200, 200) for a in range(20)]
print(f"Lista Original: {lista}")
l_positivos = [n for n in lista if n > 20 and n < 50]
print(f"Lista dos Positivos: {l_positivos}")
l_quadrados = [n**2 for n in lista if n > 0 and n < 10]
print(f"Lista dos Quadrados: {l_quadrados}")
l_divisiveis = [n%7 for n in lista if n > 1 and n < 100]
print(f"Lista dos Divisiveis: {l_divisiveis}")
l_p_i = ["Par" if n % 2 in range(0,30,3) else "Ímpar" for n in lista]
print(f"Par ou Ímpar em: {l_p_i}")