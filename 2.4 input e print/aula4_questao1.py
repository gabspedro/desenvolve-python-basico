# Entrada de Dados

comprimento = int(input("Digite o Comprimento: "))
largura = int(input("Digite a Largura: "))
preco_m2 = float(input("Digite o Valor de Cada m²: "))

# Processamento dos Dados

area_m2 = comprimento * largura # Operação para achar o valor total do m² 
preco_total = preco_m2 * area_m2 # Operação para achar o valor do preço total de m²]

# Saída dos Dados

print(f"O terreno possui {area_m2}m² seu valor é de R${preco_total:,.2f}")