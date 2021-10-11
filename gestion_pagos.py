

db = [['bank of Saman', 1234, '$2000', 'Carolina Broadberrie', 'massi', '2112', False, '13/9/2011', 'M'], ['Avila Bank', 1212, '$800', 'Saman Cola', 'saman', '1234', True]]
db2 = []

# for x in db:
#     monto = x[2].split("$")
#     monto2 = int(monto[1])
#     nombre = x[3]

#     db2.append([nombre, monto2])

# print(db2)

vector = [3,5,3,2]
vector2 =[]


def insertionsort(vector):
    n = len(vector)
    for i in range(1,n):
        for j in range(0, n-1):
            if vector[j] > vector[j+1]:
                aux = vector[j]
                vector[j] = vector[j+1]
                vector[j+1] = aux

x = insertionsort(vector)

print(x)

        
# from fecha_y_hora import *

# def transferencia(db,dic):

#     i=0
#     while i==0:
        
#         mail= input("ingrese su correo electronico")
#         psw = input("ingrese su psw")

#         for z in db:
            
#             if mail == z[4] and psw == z[5]:
#                 i+=1
#             else:
#                 pass

#     for cliente in db:

#                     print(db)
#                     print(cliente)
#                     print(dic)


#                     # while mail != cliente[4] or psw != cliente[5]:
#                     #     mail= input("ingrese su correo electronico")
#                     #     psw = input("ingrese su psw")
                    

#                     if cliente[6] == False and cliente[4] == mail and cliente[5] == psw:
#                         print(f'''
                        
#                         banco: {cliente[0]}
#                         codigo: {cliente[1]}
#                         balance: {cliente[2]}
#                         nombre: {cliente[3]}
#                         correo: {cliente[4]}
#                         contraseña: {cliente[5]}
#                         Empresa: {cliente[6]}
#                         Fecha nacimiento: {cliente[7]}
#                         sexo: {cliente[8]}
                        

#                         ''')
#                         correo = input("Ingrese el correo al que desea transferir")

#                         n=0
#                         for x in db:
#                         # print(x)
#                         # print("flag")
            
            
#                             if str(correo) == str(x[4]):
#                                 monto = float(input("Ingrese el monto a transferir"))


#                                 my_balance = cliente[2].split("$")
#                                 my_balance = float(my_balance[1])
#                                 destinatario = db[n][2].split("$")
#                                 destinatario = float(destinatario[1])

#                                 if monto <= my_balance:
#                                     cliente[2] = my_balance - monto
#                                     db[n][2] = destinatario + monto
                

#                                     descripcion = input("Ingrese el motivo de pago")
#                                     while len(descripcion) >20:
#                                         descripcion = input("Tienen que ser menos de 20 caracteres, Ingrese el motivo de pago")
                    
#                                     fecha = fecha_trans()
#                                     codigo_trans = code_trans()
#                                     cuerpo = [[x[4],fecha,codigo_trans,monto,descripcion]]
#                                     dic[x[3]]= cuerpo
                                        
                                    


#                             n+=1
#                     elif cliente[6] == True and cliente[4] == mail and cliente[5] == psw:
#                         print(f'''
                        
#                         banco: {cliente[0]}
#                         codigo: {cliente[1]}
#                         balance: {cliente[2]}
#                         nombre: {cliente[3]}
#                         correo: {cliente[4]}
#                         contraseña: {cliente[5]}
#                         Empresa: {cliente[6]}
                        

#                         ''')
#                         correo = input("Ingrese el correo al que desea transferir")

#                         n=0
#                         for x in db:
#                         # print(x)
#                         # print("flag")
            
            
#                             if str(correo) == str(x[4]):
#                                 monto = float(input("Ingrese el monto a transferir"))
                                
#                                 if 


#                                 my_balance = cliente[2].split("$")
#                                 my_balance = float(my_balance[1])
#                                 destinatario = db[n][2].split("$")
#                                 destinatario = float(destinatario[1])

#                                 if monto <= my_balance:
#                                     cliente[2] = my_balance - monto
#                                     db[n][2] = destinatario + monto
                

#                                     descripcion = input("Ingrese el motivo de pago")
#                                     while len(descripcion) >20:
#                                         descripcion = input("Tienen que ser menos de 20 caracteres, Ingrese el motivo de pago")
                    
#                                     fecha = fecha_trans()
#                                     codigo_trans = code_trans()
#                                     cuerpo = [[x[4],fecha,codigo_trans,monto,descripcion]]
#                                     dic[x[3]]= cuerpo