import tkinter as tk
from time import strftime
import serial
from onibus import Onibus  # Certifique-se de ter o módulo 'onibus' disponível no seu código

# Inicialização da comunicação serial com o Arduino
arduino = serial.Serial('COM8', 9600)

tabela = tk.Tk()
tabela.title("Tabela de Ônibus")
tabela.geometry("800x600")
tabela.configure(background='white')

# Função para mostrar a data
def data():
    data_atual = strftime('%d/%m/%Y')
    datas.config(text=data_atual)
    datas.after(1000, data)

# Função para mostrar a hora
def tempo():
    tempo_atual = strftime('%H:%M:%S %p')
    tempos.config(text=tempo_atual)
    tempos.after(1000, tempo)

# Função para mostrar a tabela de ônibus
def tabela_onibus():
    tabela_atual = "Tabela de Ônibus"
    tabela_o.config(text=tabela_atual)
    tabela_o.after(1000, tabela_onibus)

# Função para verificar e atualizar as informações dos ônibus
def atualizar_informacoes():
    global lista_onibus_passado, lista_onibus_proximo

    onibus_recebido = str(arduino.readline())
    criar_onibus(onibus_recebido)

    # Limpar as informações antigas
    for widget in tabela.winfo_children():
        if isinstance(widget, tk.Label) and widget.grid_info()["row"] > 3:
            widget.destroy()

    # Preencher a tabela com os dados atualizados
    for i, onibus in enumerate(lista_onibus_passado):
        tk.Label(tabela, text=onibus.nome, bg='white', fg='black', font=('Montserrat', 12)).grid(row=i+4, column=0, padx=10, pady=10)
        tk.Label(tabela, text=onibus.prefixo, bg='white', fg='black', font=('Montserrat', 12)).grid(row=i+4, column=1, padx=10, pady=10)

    for i, onibus in enumerate(lista_onibus_proximo):
        tk.Label(tabela, text=onibus.nome, bg='white', fg='black', font=('Montserrat', 12)).grid(row=i+4, column=2, padx=10, pady=10)
        tk.Label(tabela, text=onibus.prefixo, bg='white', fg='black', font=('Montserrat', 12)).grid(row=i+4, column=3, padx=10, pady=10)
        tk.Label(tabela, text=onibus.distancia, bg='white', fg='black', font=('Montserrat', 12)).grid(row=i+4, column=4, padx=10, pady=10)

    tabela.after(1000, atualizar_informacoes)

def verificar_onibus(onibus):
    if onibus.rota_parada == "pa":
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
    elif onibus.rota_parada == "p1":
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

# Função para criar objeto Onibus e verificar a posição
def criar_onibus(dados_onibus):
    rota_parada, numero, prefixo, distancia = dados_onibus[2:15].split("_")
    nome = nome_onibus(numero)
    objOnibus = Onibus(rota_parada, numero, prefixo, nome, distancia)
    verificar_onibus(objOnibus)

# Função para obter o nome do ônibus com base no número
def nome_onibus(numero):
    if numero == "165":
        return "COHAB"
    elif numero == "209":
        return "RESTINGA"
    else:
        return "Desconhecido"

# Dados da tabela de ônibus (exemplo)
lista_onibus_passado = []
lista_onibus_proximo = []

datas = tk.Label(tabela, bg='white', fg='black', font=('Montserrat', 14))
datas.grid(row=0, column=0, columnspan=5, pady=10)

tempos = tk.Label(tabela, bg='white', fg='black', font=('Montserrat', 14))
tempos.grid(row=1, column=0, columnspan=5, pady=10)

tabela_o = tk.Label(tabela, bg='white', fg='black', font=('Montserrat', 14))
tabela_o.grid(row=2, column=0, columnspan=5, pady=10)

# Cabeçalhos da tabela
tk.Label(tabela, text="Ônibus Passados", bg='white', fg='black', font=('Montserrat', 14)).grid(row=3, column=0, padx=10, pady=10, columnspan=2)
tk.Label(tabela, text="Próximos Ônibus", bg='white', fg='black', font=('Montserrat', 14)).grid(row=3, column=2, padx=10, pady=10, columnspan=3)
tk.Label(tabela, text="Nome", bg='white', fg='black', font=('Montserrat', 12)).grid(row=3, column=0, padx=10, pady=10)
tk.Label(tabela, text="Prefixo", bg='white', fg='black', font=('Montserrat', 12)).grid(row=3, column=1, padx=10, pady=10)
tk.Label(tabela, text="Nome", bg='white', fg='black', font=('Montserrat', 12)).grid(row=3, column=2, padx=10, pady=10)
tk.Label(tabela, text="Prefixo", bg='white', fg='black', font=('Montserrat', 12)).grid(row=3, column=3, padx=10, pady=10)
tk.Label(tabela, text="Distância", bg='white', fg='black', font=('Montserrat', 12)).grid(row=3, column=4, padx=10, pady=10)

data()
tempo()
tabela_onibus()
atualizar_informacoes()

tabela.mainloop()