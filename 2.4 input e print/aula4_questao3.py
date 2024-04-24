# Valores das Roupas

camisa = 49.95
calca = 199.90 
cinto = 25

# Entrada de Dados

camisa = (int(input("Quantas Camisas ?")) * camisa)
calca = (int(input("Quantas Calças? ")) * calca)
cinto = (int(input("Quantos Cintos? ")) * cinto)

# Processamento dos Dados

preco_total = camisa + calca + cinto

# Saída dos Dados

print(f"O valor da compra será R${preco_total:,.2f}")