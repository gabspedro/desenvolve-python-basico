import random

lista = [random.randint(-10, 10) for a in range(20)]
print(lista)

i_m, t_m = 0, 0
i_m_a, t_m_a = 0, 0

for i in range(len(lista)):
    if lista[i] < 0:
        t_m_a += 1
        if t_m_a == 1:
            i_m_a = i
    else:
        if t_m_a > t_m:
            t_m = t_m_a
            i_m = i_m_a
        t_m_a = 0

print(i_m, t_m)
del lista[i_m:i_m+t_m]
print(lista)