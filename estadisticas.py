
def estadisticas(db,dic,solicitudes,splits):
    total_comisiones = 0
    comisiones_persona = 0
    comisiones_empresa = 0
    total_capicua = 0
    usuarios_empresa = 0
    usuarios_persona = 0
    numero_splits= 0
    for key,value in dic.items():
        for transaccion in value:
            print(transaccion[6])
            print(type(transaccion[6]))
            if transaccion[7] == False:

                comisiones_persona += transaccion[6]

            else:
                comisiones_empresa += transaccion[6]


    total_comisiones = comisiones_empresa + comisiones_persona



    for key,value in dic.items():
        for transaccion in value:
            if transaccion[8] == "si":

                total_capicua += 1



    for x in db:
        if x[6]==True:
            usuarios_empresa +=1

        else:
            usuarios_persona+=1

    for y in splits:
        numero_splits+=1

    print(f'''

    --------------ESTADISTICAS--------------

    -Monto total recaudado por comisiones: {total_comisiones}
    -Monto total recaudado por tipo de usuario: Persona -${comisiones_persona}
                                                Empresa -${comisiones_empresa}
    -Cantidad de transferencias que fueron exoneradas por el hecho de ser un monto con números capicúa: {total_capicua}
    -Cantidad de usuarios por tipo: Persona -${usuarios_persona}
                                    Empresa -${usuarios_empresa}
    -Cantidad de Splits realizados: {numero_splits}

    ''')

