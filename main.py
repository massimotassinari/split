# Nombre: Massimo Tassinari
# Carnet: 20201120010

import requests
from Usuario import Usuario
from Empresa import Empresa
from Persona import Persona
from gestion import gestion
from estadisticas import estadisticas
from split2 import *
from Separa import Separa
import pickle


def api_saman():

    url = "https://a.nacapi.com/saman_pay"

    api = requests.get(url)

    return api.json()
    


def main():
    
    try:
        db = pickle.load(open("db.txt","rb"))
        
    except EOFError:
        db = list()
    

    try:
        dic = pickle.load(open("dic.txt","rb"))
        
    except EOFError:
        dic = dict()


    try:
        solicitudes = pickle.load(open("solicitudes.txt","rb"))
        
    except EOFError:
        solicitudes = list()


    try:
        splits = pickle.load(open("splits.txt","rb"))
        
    except EOFError:
        splits = list()
    




    print("¡Bienvenido a Saman Pay!")

    while True:
        
        print("\n1. Gestionar usuarios\n2. Split\n3. Estadisticas\n4. Salir")

        seleccion = input("Ingrese el número correspondiente a su selección:\n>>> ")

        while (not seleccion.isnumeric()) or (int(seleccion) not in range(1,5)):
            seleccion = input("Por favor ingrese un valor válido:\n>>> ")
            
        print("\n")
        
        if seleccion =="1":
            gestion(api_saman(),db,dic,solicitudes)

        elif seleccion=="2":
            split(splits)

        elif seleccion=="3":
            estadisticas(db,dic,solicitudes,splits)

            print("Imprimiento db")
            print(db)
            print("imprimiendo dic")
            print(dic)
            print("imprimiendo solicitudes")
            print(solicitudes)
            print("imprimiendo splits")
            print(splits)


        else:
            
            pickle.dump(db,open("db.txt","wb"))
            pickle.dump(dic,open("dic.txt","wb"))
            pickle.dump(solicitudes,open("solicitudes.txt","wb"))
            pickle.dump(splits,open("splits.txt","wb"))
            
            break




main()