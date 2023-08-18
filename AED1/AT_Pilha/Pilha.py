from Livro import Livro

class Pilha:
    def __init__(self):
       self.ultimoADD = None
       self.primeiroADD = None

    def add(self,livro):
        if self.primeiroADD == None:
            self.ultimoADD = livro
            self.primeiroADD = livro
        else:
            livro.proximo = self.ultimoADD
            self.ultimoADD = livro

    def remover(self):
        if self.primeiroADD == None:
           print("Fila está Vazia!")
        else:
           aux = self.ultimoADD
           self.ultimoADD = aux.proximo

    def imprimir(self):
       if self.primeiroADD == None:
           print("Fila está Vazia!")
       else:
           aux = self.ultimoADD
           while aux:
                print(aux.titulo,"-",aux.genero)
                aux = aux.proximo
        
       