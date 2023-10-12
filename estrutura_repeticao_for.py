texto = input("Informe um texto: ")
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")
else:
    print() # quebra de linha
    print("Executa no final do laço")

# range(stop) --> raange object
# range(start, stop[, step])

for numero in range(11):
    print(numero, end="")

for numero in range(0, 51, 5):
    print(numero, end="")