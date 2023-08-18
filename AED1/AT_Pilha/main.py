from Livro import Livro
from Pilha import Pilha

l1 = Livro("livro 1", "genero1")
l2 = Livro("livro 2", "genero2")
l3 = Livro("livro 3", "genero3")

pilha = Pilha()

pilha.add(l1)
pilha.add(l2)
pilha.add(l3)
pilha.imprimir()
print("--------------")
pilha.remover()
pilha.imprimir()
print("--------------")
pilha.remover()
pilha.imprimir()