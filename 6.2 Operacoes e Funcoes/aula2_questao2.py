import random

num_elementos = [random.randint(5, 20) for a in range(random.randint(1, 15))]
elementos = [random.randint(1, 10) for a in range(len(num_elementos))]

print(f"A Lista dos Elementos é {elementos}")
print(f"A Soma dos Valor é {sum(elementos)}")
print(f"A Média é {sum(elementos) / len(elementos)}")