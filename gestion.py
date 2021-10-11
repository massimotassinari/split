
from ast import Str
from Usuario import Usuario
from Empresa import Empresa
from Persona import Persona
from fecha_y_hora import *

def gestion(api,db,dic,solicitudes):
        
    primer_while=True
    
    while primer_while:

        print("\n1. Crear una cuenta\n2. Iniciar seccion \n3. Salir\n")

        seleccion = input("Ingrese el número correspondiente a su selección:\n>>> ")

        while (not seleccion.isnumeric()) or (int(seleccion) not in range(1,5)):
            seleccion = input("Por favor ingrese un valor válido:\n>>> ")
            
        print("\n")
#CREAR UNA NUEVA CUENTA       
        if seleccion =="1":
            bancos =[]
            for y in api:
                
                banks = y.keys()
                n=1
                for x in banks:
                    print(f"{n}. {x}")
                    n+=1
                    bancos.append(x)

        
            banco = input("Seleccione el banco\n>>> ")

            while not banco.isnumeric() or int(banco) not in range(1,4):
                banco = input("Error, Seleccione el banco\n>>> ")

            codigo_personal = input("Ingrese su codigo personal del banco\n>>> ")
            codigos = []

            for key in api[0][bancos[int(banco)-1]]:
                codigos.append(key["code"])

            while not codigo_personal.isnumeric() or int(codigo_personal) not in codigos:

                codigo_personal = input("Error, Ingrese su codigo personal del banco\n>>> ")
# ###       
            banco = int(banco)
            codigo_personal = int(codigo_personal)


            for key in api[0][bancos[banco-1]]:
                
#Tipo Persona
                if codigo_personal == key["code"] and key["company"] == False:
                    print(f'''
        Nombre: {key["full_name"]}
        Sexo: {key["gender"]}
        Balance: {key["balance"]}
        Fecha nacimiento: {key["birthdate"]}
        Tipo: {key["company"]}   
        ''')            
                    mail = input("Introduzca el correo electronico con el que usara Saman Pay:\n>>> ")
                    psw = input("Introduzca la contraseña que usara para ingresar en Saman Pay:\n>>> ")
                    
                    banco = bancos[banco-1]
                    codigo = key["code"]
                    balance = key["balance"]
                    nombre = key["full_name"]
                    correo = mail
                    contrasena = psw
                    tipo = key["company"]
                    fecha = key["birthdate"]
                    sexo = key["gender"]

                    nuevo_usuario = Persona(banco,codigo,balance,nombre,correo,contrasena,tipo,fecha,sexo)
                    
                    db.append([nuevo_usuario.banco,nuevo_usuario.codigo,nuevo_usuario.balance,nuevo_usuario.nombre,nuevo_usuario.correo,nuevo_usuario.contrasena,nuevo_usuario.tipo,nuevo_usuario.fecha,nuevo_usuario.sexo])
#TIPO EMPRESA
                elif codigo_personal == key["code"] and key["company"] == True:
                    print(f'''
        Nombre: {key["full_name"]}
        
        Balance: {key["balance"]}
        
        Tipo: {key["company"]}  

        ''')   


                    mail = input("Introduzca el correo electronico con el que usara Saman Pay: ")
                    psw = input("Introduzca la contraseña que usara para ingresar en Saman Pay: ")
                    banco = bancos[banco-1]
                    codigo = key["code"]
                    balance = key["balance"]
                    nombre = key["full_name"]
                    correo = mail
                    contrasena = psw
                    tipo = key["company"]
                      
                    nuevo_usuario = Empresa(banco,codigo,balance,nombre,correo,contrasena,tipo) 
                    db.append([nuevo_usuario.banco,nuevo_usuario.codigo,nuevo_usuario.balance,nuevo_usuario.nombre,nuevo_usuario.correo,nuevo_usuario.contrasena,nuevo_usuario.tipo])
#HACER LOGIN
        elif seleccion=="2":
            i=0
            
            while i==0:
        
                mail= input("Ingrese su correo electronico\n>>> ")
                psw = input("Ingrese su psw\n>>> ")

                for z in db:
                
                    if mail == z[4] and psw == z[5]:
                        i=1
                    else:
                        pass
                        

            for cliente in db:
                  
                #TIPO PERSONA
                if cliente[6] == False and cliente[4] == mail and cliente[5] == psw:

                    
                    print(f'''
                        
    Banco: {cliente[0]}
    Codigo: {cliente[1]}
    Balance: {cliente[2]}
    Nombre: {cliente[3]}
    Correo: {cliente[4]}
    Contraseña: {cliente[5]}
    Empresa: {cliente[6]}
    Fecha nacimiento: {cliente[7]}
    Sexo: {cliente[8]}
                        

                        ''')
                    while True:
        
                        print("\n1. Transferir\n2. Cambiar correo electronico \n3. Ver solicitudes de pago\n4. Ver directorio de contactos\n5. Salir\n")

                        seleccion = input("Ingrese el número correspondiente a su selección:\n>>> ")

                        while (not seleccion.isnumeric()) or (int(seleccion) not in range(1,6)):
                            seleccion = input("Por favor ingrese un valor válido:\n>>> ")

                        #TRANSFERIR 
                        if seleccion == "1":

                            correo = input("Ingrese el correo al que desea transferir")

                            n=0
                            for x in db:


                                if str(correo) == str(x[4]):
                                    monto = float(input("Ingrese el monto a transferir"))
                                    comision = 0
                                    capicua = "no"
                                    if str(monto) == str(monto)[::-1]:
                                        capicua = "si"
                                        print("No te cargaremos el iva, ya que tu monto es un numero capicua!")
                                    else:
                                                
                                        comision = monto * 0.05
                                        monto_con_iva = monto + comision
                                        

                                    my_balance = cliente[2].split("$")
                                    my_balance = float(my_balance[1])

                                    destinatario = db[n][2].split("$")
                                    destinatario = float(destinatario[1])
                                    monto_dolar_receptor = "$" + str(destinatario + monto)
                                    monto_dolar_emisor = "$" + str(my_balance - monto_con_iva)

                                    if monto <= my_balance:

                                        cliente[2] = monto_dolar_emisor
                                        
                                        db[n][2] = monto_dolar_receptor

                                        descripcion = input("Ingrese el motivo de pago")
                                        while len(descripcion) >20:
                                            descripcion = input("Tienen que ser menos de 20 caracteres, Ingrese el motivo de pago:  ")
                                
                                        fecha = fecha_trans()
                                        codigo_trans = code_trans()
                                        cuerpo = [[x[3],x[4],fecha,codigo_trans,monto,descripcion,comision,x[6],capicua]]
                                        dic[cliente[3]]= cuerpo
                                        print(cuerpo)
                                        print(cliente[3])
                                        print(f'''
        --------TRANSACCION--------
        Receptor: {x[3]}
        Correo: {x[4]}
        Fecha y hora: {fecha}
        Codigo de transaccion: {codigo_trans}
        Monto emitido: {monto}
        Descripcion: {descripcion}       

                                            ''')
                                n+=1

                        #cambiar correo
                        elif seleccion =="2":
                            print(f"Su correo es {cliente[4]}\n")
                            while True:
                                seleccion = input("1. Cambiar correo\n2. Volver:\n>>> ")
                                while (not seleccion.isnumeric()) or (int(seleccion) not in range(1,3)):

                                    seleccion = input("Por favor ingrese un valor válido:\n>>> ")
                                if seleccion=="1":
                                    nuevo_correo = input("Ingrese su nuevo correo:\n>>> ")
                                   
                                    
                                    cliente[4] = nuevo_correo
                                    
                                else:
                                    break

                        #ver solicitudes de pago
                        elif seleccion =="3":
                            print("---Solicitudes de pago---\n")

                            w=0
                            for x in solicitudes:
                                                          
                                if x[0] == cliente[4]:
                                    while True:                               

                                        print(f"-Tiene una solicitud de: {x[4]}\n-Monto: {x[2]}\n-Descripcion: {x[1]}\n-Estado: {x[3]}\n")
                                        seleccion = input("1. Para pagar\n2.Para rechazar\n3. Volver\n")
                                        while (not seleccion.isnumeric()) or (int(seleccion) not in range(1,4)):
                                            seleccion = input("Por favor ingrese un valor válido:\n>>> ")
                                        
                                        if seleccion =="1":
                                            
                                            
                                            monto = x[2]

                                            if str(monto) == str(monto)[::-1]:
                                                pass
                                            else:
                                                comision = monto * 0.05
                                                monto_con_iva = monto + comision
                                            

                                            my_balance = cliente[2].split("$")
                                            my_balance = float(my_balance[1])
                                            j=0
                                            for y in db:
                                                if y[4] == x[4]:

                                                    destinatario = db[j][2].split("$")
                                                    destinatario = float(destinatario[1])


                                                    monto_dolar_receptor = "$" + str(destinatario+monto)
                                                    monto_dolar_emisor = "$" + str(my_balance-monto_con_iva)

                                                    if monto <= my_balance:
                                                        cliente[2] = monto_dolar_emisor

                                                        db[j][2] = monto_dolar_receptor
                                                        solicitudes[w][3] = "Aceptada"

                                                        break
                                                    else:
                                                        break
                                                j+=1



                                        elif seleccion=="2":
                                            solicitudes[w][3] = "Rechazada"
                                            break
                                            
                                        else:
                                            break
                                w+=1


                            

                        #ver directorio de contactos
                        elif seleccion=="4":

                            for key,value in dic.items():

                                ['bank of Saman', 1234, '$1522019.24', 'Carolina Broadberrie', 'massi', '2112', False, '13/9/2011', 'M']
                                if key == cliente[3]:

                                    print("Lista de contactos:\n")

                                    for x in value:
                                        print(f"-{x[0]}")
                                    

                        else: 
                            break  

                            
                #TIPO EMPRESAAAA
                elif cliente[6] == True and cliente[4] == mail and cliente[5] == psw:

                    print(f'''
                        
    banco: {cliente[0]}
    codigo: {cliente[1]}
    balance: {cliente[2]}
    nombre: {cliente[3]}
    correo: {cliente[4]}
    contraseña: {cliente[5]}
    Empresa: {cliente[6]}
                        
                        ''')

                    while True:
        
                        print("\n1. Transferir\n2. Cambiar correo electronico \n3. Ver solicitudes de pago\n4. Ver directorio de contactos\n5. Solicitar pago\n6. Salir")

                        seleccion = input("Ingrese el número correspondiente a su selección:\n>>> ")

                        while (not seleccion.isnumeric()) or (int(seleccion) not in range(1,7)):
                            seleccion = input("Por favor ingrese un valor válido:\n>>> ")
                        #HACER TRANSFERENCIA
                        if seleccion == "1":

                            correo = input("Ingrese el correo al que desea transferir\n>>>")
                                    
                            n=0
                            for x in db:

                        
                                if str(correo) == str(x[4]):
                                    monto = float(input("Ingrese el monto a transferir\n>>>"))
                                    comision = 0
                                    capicua = "no"
                                    if str(monto) == str(monto)[::-1]:
                                        capicua = "si"
                                        print("¡No te cargaremos el iva, ya que tu monto es un numero capicua!\n")
                                    else:
                                                
                                        comision = monto * 0.1
                                        
                                        monto_con_iva = monto + comision

                                    my_balance = cliente[2].split("$")
                                    my_balance = float(my_balance[1])

                                    destinatario = db[n][2].split("$")
                                    destinatario = float(destinatario[1])
                                    monto_dolar_receptor = "$" + str(destinatario + monto)
                                    monto_dolar_emisor = "$" + str(my_balance - monto_con_iva)

                                    if monto <= my_balance:
 
                                        # tu = cliente[2] 

                                        cliente[2] = monto_dolar_emisor
                                        
                                        db[n][2] = monto_dolar_receptor

                                        descripcion = input("Ingrese el motivo de pago\n>>>")
                                        while len(descripcion) >20:
                                            descripcion = input("Tienen que ser menos de 20 caracteres, Ingrese el motivo de pago:\n>>> ")
                                
                                        fecha = fecha_trans()
                                        codigo_trans = code_trans()
                                        cuerpo = [[x[3],x[4],fecha,codigo_trans,monto,descripcion,comision,x[6]]]
                                        dic[cliente[3]]= cuerpo

                                        print(f'''
--------TRANSACCION--------
Receptor: {x[3]}
Correo: {x[4]}
Fecha y hora: {fecha}
Codigo de transaccion: {codigo_trans}
Monto emitido: {monto}
Descripcion: {descripcion} 
 ''')
                                n+=1
                        #CAMBIAR EMAIL
                        elif seleccion =="2":
                            print(f"Su correo es {cliente[4]}\n")
                            while True:
                                seleccion = input("1. Cambiar correo\n2. Volver\n>>>")
                                while (not seleccion.isnumeric()) or (int(seleccion) not in range(1,3)):

                                    seleccion = input("Por favor ingrese un valor válido:\n>>> ")
                                if seleccion=="1":
                                    nuevo_correo = input("Ingrese su nuevo correo:\n>>> ")
                                    cliente[4] = nuevo_correo
                                    # db[n][4] = nuevo_correo

                                else:
                                    break

                        #ver solicitudes de pago
                        elif seleccion =="3":
                            print("---Solicitudes de pago---\n")

                            w=0
                            for x in solicitudes:
                                                        
                                if x[0] == cliente[4]:
                                    while True:
                                        


                                        print(f"-Tiene una solicitud de: {x[4]}\n-Monto: {x[2]}\n-Descripcion: {x[1]}\n-Estado: {x[3]}\n")
                                        seleccion = input("1. Para pagar\n2.Para rechazar\n3. Volver\n")
                                        while (not seleccion.isnumeric()) or (int(seleccion) not in range(1,4)):
                                            seleccion = input("Por favor ingrese un valor válido:\n>>> ")
                                        
                                        if seleccion =="1":
                                            
                                            
                                            monto = x[2]

                                            if str(monto) == str(monto)[::-1]:
                                                pass
                                            else:
                                                comision = monto * 0.1
                                                monto_con_iva = monto + comision
                                            

                                            my_balance = cliente[2].split("$")
                                            my_balance = float(my_balance[1])

                                            j=0
                                            for y in db:
                                                if y[4] == x[4]:

                                                    destinatario = db[j][2].split("$")
                                                    destinatario = float(destinatario[1])

                                                    monto_dolar_receptor = "$" + str(destinatario+monto)
                                                    monto_dolar_emisor = "$" + str(my_balance-monto_con_iva)

                                                    if monto <= my_balance:
                                                        cliente[2] = monto_dolar_emisor
                                                        db[j][2] = monto_dolar_receptor
                                                        solicitudes[w][3] = "Aceptada"
                                                        
                                                        break
                                                    else:
                                                        break
                                                j+=1



                                        elif seleccion=="2":
                                            solicitudes[w][3] = "Rechazada"
                                            break
                                            
                                        else:
                                            break
                                w+=1


                            

                        #ver directorio de contactos
                        elif seleccion=="4":

                            for key,value in dic.items():

                                if key == cliente[3]:

                                    print("Lista de contactos:\n")

                                    for x in value:
                                        print(f"-{x[0]}")
                        #SOLICITAR PAGO
                        elif seleccion =="5":
                            correo = input("Ingrese el correo del usuario a solicitar el pago:\n>>> ")
                            descripcion = input("Ingrese una descripcion a esta solicitud:\n>>> ")
                            monto = input("Ingrese el monto a solicitar:\n>>> ")
                            estado = "pendiente" 

                            solicitudes.append([correo,descripcion,monto,estado,cliente[4]])

                        else: 
                            break  
                 
        
        else:
            break
            

    return db

     