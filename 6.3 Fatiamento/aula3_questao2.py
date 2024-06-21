t = "None"
URL = []

while t != "Fim":
    t = str(input("Escolha uma URL: "))
    URL.append(t)

dominios = [url[4:-4] for url in URL]

print(URL)
print("\n")
print(dominios)