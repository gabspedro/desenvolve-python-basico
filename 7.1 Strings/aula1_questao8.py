def validar_cpf():
    cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ").replace('.', '').replace('-', '')
    
    if len(cpf) != 11 or not cpf.isdigit():
        print("Inválido")
        return
    
    def calcular_digito(cpf, peso):
        soma = sum(int(cpf[i]) * (peso - i) for i in range(peso - 1))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto
    
    primeiro_digito = calcular_digito(cpf, 10)
    segundo_digito = calcular_digito(cpf, 11)
    
    if cpf[-2:] == f"{primeiro_digito}{segundo_digito}":
        print("Válido")
    else:
        print("Inválido")

validar_cpf()