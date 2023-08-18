from abc import ABC, abstractmethod 
from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
        return super().getInformacoes() + f"\nTempoDeBateria: {self.__tempoDeBateria}"

    def cadastrar(self):
        print("Cadastrando notebook....")


        
