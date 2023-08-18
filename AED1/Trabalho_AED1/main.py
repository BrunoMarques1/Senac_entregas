from Computador import Computador
from Noteboook import Notebook
from Desktop import Desktop

print("---------------------------")
print("DESKTOP:")
d = Desktop("Inspiron", "Preto", 3500, 500)
print(d.getInformacoes())
print("---------------------------")
print("NOTEBOOK:")
n = Notebook("MacBook Pro", "Prata", 5000, "5 horas")
print(n.getInformacoes())
print("---------------------------")