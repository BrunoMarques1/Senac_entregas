import serial
from onibus import Onibus
arduino = serial.Serial('COM4', 9600)


lista_onibus_passado = []
lista_onibus_proximo = []

def nome_onibus(numero):
    if numero == "165":
        return "COHAB"
    elif numero == "209":
        return "RESTINGA"

def verificar_onibus(onibus):
    if onibus.rota_parada == "pc":
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
    elif onibus.rota_parada == "p3":
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
    rota_parada, numero, prefixo, distancia = onibus[2:15].split("_")
    nome = nome_onibus(numero)
    objOnibus = Onibus(rota_parada,numero,prefixo,nome,distancia)
    verificar_onibus(objOnibus)


aux = lista_onibus_passado.copy()
aux2 = lista_onibus_proximo.copy()
while True:
    onibus_recebido = str(arduino.readline())
    criar_onibus(onibus_recebido)

    if (aux != lista_onibus_passado) or (aux2 != lista_onibus_proximo):
        print("================")
        print("Lista de ônibus passados:")
        for i in lista_onibus_passado:
            print(i.nome,"-",i.prefixo,)
        aux = lista_onibus_passado.copy()
        print("=================")
        print("Lista de próximos ônibus:")
        for i in lista_onibus_proximo:
            print(i.nome,"-",i.prefixo,"-",i.distancia)
        aux2 = lista_onibus_proximo.copy()
        print("=================\n")