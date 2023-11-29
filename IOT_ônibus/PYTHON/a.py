import serial
import tkinter as tk
from tkinter import ttk
from onibus import Onibus

arduino = serial.Serial('COM8', 9600)

lista_onibus_passado = []
lista_onibus_proximo = []

def nome_onibus(numero):
    if numero == "165":
        return "COHAB"
    elif numero == "209":
        return "RESTINGA"

def verificar_onibus(onibus):
    if onibus.rota_parada in ["a","b","c"]:
        for i in lista_onibus_proximo:
            if i.prefixo == onibus.prefixo:
                lista_onibus_proximo.remove(i)
        var = False
        for i in lista_onibus_passado:
            if i.prefixo == onibus.prefixo:
                var = True
        if var == False and len(lista_onibus_passado) > 3:
            lista_onibus_passado.append(onibus)
            lista_onibus_passado.pop(0)
        elif var == False and len(lista_onibus_passado) < 4:
            lista_onibus_passado.append(onibus)
    else:
        var = False
        for i in lista_onibus_proximo:
            if i.prefixo == onibus.prefixo:
                var = True
        if var == False and len(lista_onibus_proximo) < 4:
            lista_onibus_proximo.append(onibus)
        elif var == False and len(lista_onibus_proximo) > 3:
            lista_onibus_proximo.append(onibus)
            lista_onibus_proximo.pop(0)
        else:
            for i in lista_onibus_proximo:
                if i.prefixo == onibus.prefixo and i.distancia > onibus.distancia:
                    lista_onibus_proximo.remove(i)
                    lista_onibus_proximo.append(onibus)


def criar_onibus(onibus):
    rota_parada, numero, prefixo, distancia = onibus[2:-9].split("_")
    nome = nome_onibus(numero)
    objOnibus = Onibus(rota_parada,numero,prefixo,nome,distancia)
    verificar_onibus(objOnibus)

def atualizar_tela():
    tree_passados.delete(*tree_passados.get_children())
    tree_proximos.delete(*tree_proximos.get_children())

    for i in lista_onibus_passado:
        tree_passados.insert("", "end", values=(i.nome, i.prefixo, i.distancia))
    for i in lista_onibus_proximo:
        tree_proximos.insert("", "end", values=(i.nome, i.prefixo, i.distancia))
        
    root.after(1000, atualizar_tela)

def receber_dados():
    onibus_recebido = str(arduino.readline())
    criar_onibus(onibus_recebido)
    root.after(100, receber_dados)

# Criar a interface gráfica
root = tk.Tk()
root.title("Monitor de Ônibus")
root.configure(bg='Black')  # Configurar o fundo preto

# Configurar a tabela para ônibus passados
tree_passados = ttk.Treeview(root, columns=("Ônibus", "Prefixo", "Distância"), show="headings", height=4)
tree_passados.heading("Ônibus", text="Ônibus", anchor="w")
tree_passados.heading("Prefixo", text="Prefixo", anchor="w")
tree_passados.heading("Distância", text="Distância", anchor="w")
tree_passados.tag_configure('passados', background='black', foreground='white')
tree_passados.pack()

# Configurar a tabela para ônibus próximos
tree_proximos = ttk.Treeview(root, columns=("Ônibus", "Prefixo", "Distância"), show="headings", height=4)
tree_proximos.heading("Ônibus", text="Ônibus", anchor="w")
tree_proximos.heading("Prefixo", text="Prefixo", anchor="w")
tree_proximos.heading("Distância", text="Distância", anchor="w")
tree_proximos.tag_configure('proximos', background='black', foreground='white')
tree_proximos.pack()

# Iniciar a atualização da tela e recebimento de dados
atualizar_tela()
receber_dados()

# Iniciar o loop principal do tkinter
root.mainloop()