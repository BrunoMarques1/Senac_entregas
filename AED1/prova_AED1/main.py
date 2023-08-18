from Aluno import Aluno

a = Aluno(1,"Bruno","11223344",632210177,0)
a.marcarPresenca()
print("Informações do aluno:")
print("===================================")
print(a.getInformacoes())
print("===================================")

a.set_matricula()
print("Nova matricula do aluno:",a.get_matricula())