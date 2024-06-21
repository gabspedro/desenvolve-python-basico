def contar_vogais():
    frase = input("Digite uma frase: ")
    vogais = "aeiouAEIOU"
    indices = [i for i, letra in enumerate(frase) if letra in vogais]
    print(f"{len(indices)} vogais")
    print(f"Índices {indices}")

contar_vogais()