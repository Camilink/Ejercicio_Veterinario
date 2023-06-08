import os
import time
import random
repmenu=True
Lgato = []
Lperro = []

def registrar_mascota():
    print("===INGRESO DE MASCOTA===")
    nombre_dueno=input("Por favor Ingrese su nombre:\n")
    while True:
        id_mascota= input("Ingrese ID mascota (5 dígitos):\n")
        if len(id_mascota)==5 and id_mascota.isalnum():                 
            break
        else:
            print("Ingrese ID válido.")
    
    nombre_mascota=input("Ingrese nombre mascota:\n")
    tipo=int(input("Ingrese tipo:\n 1.Perro 2.Gato"))
    if tipo ==1:
        mascota = "Perro"
        perro = [nombre_dueno,id_mascota,nombre_mascota,mascota]
        Lperro.append(perro)
    if tipo ==2:
        mascota = "Gato"
        gato = [nombre_dueno,id_mascota,nombre_mascota,mascota]
        Lgato.append(gato)

def listar_todo_registro():
    print("=======LISTADO DE MASCOTAS=========")
    for perro in Lperro:
        print(f"Nombre dueño:  {perro[0]} \nID mascota: {perro[1]}\nNombre Mascota: {perro[2]}\nTipo Mascota: {perro[3]}")
        print("==========================================================")
    for gato in Lgato:
        print(f"Nombre dueño:  {gato[0]} \nID mascota: {gato[1]}\nNombre Mascota: {gato[2]}\nTipo Mascota: {gato[3]}")
        print("==========================================================")

def buscar_mascota(busca):
    b=1
    print("====BUSCAR MASCOTA===")
    vacuna= random.randint(1,5)
    while b==1:
        for gato in Lgato:
            for dato in gato:
                if gato[1]==busca:
                    print(f"Nombre dueño:  {gato[0]} \nID mascota: {gato[1]}\nNombre Mascota: {gato[2]}\nTipo Mascota: {gato[3]}\n A su mascota le faltan: {vacuna} vacunas.")
                    b=0
                    print("=================================")
        for perro in Lperro:
            for dato in perro:
                if busca==Lperro[1]:
                    print(f"Nombre dueño:  {perro[0]} \nID mascota: {perro[1]}\nNombre Mascota: {perro[2]}\nTipo Mascota: {perro[3]}\n A su mascota le faltan: {vacuna} vacunas.")
                    print("=================================")
                    b=0
        if b==1:
            print("No se encontró a la mascota.")
            b=0

def imprimir_tipo(tipo):
    vacuna= random.randint(1,5)
    if tipo==1:
        print("LISTADO DE PERROS")
        for perro in Lperro:
            print(f"Nombre dueño:  {perro[0]} \nID mascota: {perro[1]}\nNombre Mascota: {perro[2]}\nTipo Mascota: {perro[3]}\n A su mascota le faltan: {vacuna} vacunas.")
            print("==========================================================")
    if tipo==2:
        print("LISTADO DE GATOS")
        for gato in Lgato:
            print(f"Nombre dueño:  {gato[0]} \nID mascota: {gato[1]}\nNombre Mascota: {gato[2]}\nTipo Mascota: {gato[3]}\n A su mascota le faltan: {vacuna} vacunas.")
            print("==========================================================")


def menu():
    print("\tVETERINARIA")
    print("\t==============")
    print("\t1) Registrar Mascota")
    print("\t2) Listar todos registros")
    print("\t3) Buscar Mascota")
    print("\t4) Imprimir reportes mascota por tipo")
    print("\t5) Salir del menú")
    opcion =''
    while opcion not in ['1','2','3','4','5']:
        opcion = input("Por favor ingrese una opción:\n")
    return(opcion)

while repmenu == True:
    opcion=menu()
    if opcion== '1': registrar_mascota()
    if opcion== '2': listar_todo_registro()
    if opcion== '3': 
        busca=input("Ingrese Id mascota para buscar: ")
        if len(busca)==5 and busca.isalnum(): 
            buscar_mascota(busca)
        else:
            print("Ingrese rut válido.")
    if opcion== '4': 
        tipo=int(input("Ingrese especie: 1.Perro 2.Gato"))
        if tipo==1 or tipo==2:
            imprimir_tipo(tipo)
        else:
            print("Ingrese opción correcta.")
    if opcion== '5': 
        print ("Saliendo del menu") 
        repmenu=False
