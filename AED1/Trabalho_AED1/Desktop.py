from abc import ABC, abstractmethod 
from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        return super().getInformacoes() + f"\nPotencia da fonte: {self._potenciaDaFonte}"

    def cadastrar(self):
        print("Cadastrando desktop....")