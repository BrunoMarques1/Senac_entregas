from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, id, nome, telefone, matricula, presencas):
        super().__init__(id, nome, telefone)
        self.__matricula = matricula
        self.presencas = presencas

    def marcarPresenca(self):
        self.presencas +=1

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self):
        self.__matricula = input("Qual a nova matriula do aluno?")

    def matricular(self):
        print("Matriculando....")

    def getInformacoes(self):
        return f"Id: {self.id}\nNome: {self.nome}\nTelefone: {self._telefone}\nMatricula: {self.__matricula}\nPresenças: {self.presencas}"