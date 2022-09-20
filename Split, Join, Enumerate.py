"""Split, Join, Enumerate em Python
*Split - Dividir uma string # str da maneira que você quiser ( , ou espaço ou - ) e gera uma lista com essas divisões.
*Join - Juntar uma lista # str Vai juntar a lista ou a frase com algo ( - , / , ,)
* Enumerate - Enumerar elementos da lista # iteráveis"""

"""#-----------SPLIT---------------------------
string = "O Brasil é o paiís do futbol, o Brasil é penata"
lista_1 = string.split(' ')
lista_2 = string.split(',')
for valor in lista_1:
    print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase.')
palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')
------------JOIN-----------------------------
string = 'O Brasil é penta.'
lista = string.split(' ')
string2 = '-'.join(lista)
print(string)
print(lista)
print(string2)
-----ENUMERATE-------
string = 'O Brasil é penta.'
lista = string.split(' ')
for indice, valor in enumerate(lista):
    print(indice, valor)"""
lista = [
    [1, 2],
    [3, 4],
    [5, 6]
]
for v in lista:
    print(v[0])



