from Separa import Separa

def split(splits):
    #Lista de objetos Separa
    people = []

    while True:
            
        print("\n1. Agregar\n2. Calcular\n")

        seleccion = input("Ingrese el número correspondiente a su selección:\n>>> ")

        while (not seleccion.isnumeric()) or (int(seleccion) not in range(1,3)):
            seleccion = input("Por favor ingrese un valor válido:\n>>> ")
                
        print("\n")
            
        if seleccion =="1":
            #Se agregan los inputs
            name = input("ingrese el nombre\n>>> ")#Dato dado
            spent = float(input("ingrese cuanto gasto\n>>> "))#dato dato
            has_to_recieve = 0 #Inicializado en 0
            split = [] #Lista inicializada vacia
            people.append(Separa(name,spent,has_to_recieve,split)) #se agrega el objeto a la lista people

        elif seleccion=="2":

            break
    #Inicializar total
    total = 0
    #Calcular total
    for person in people:
        total = total + person.spent
        
    #calcula cuanto tiene que pagar cada uno
    individual_payment = total/len(people)
    #Listas auxiliares
    have_to_pay = []
    have_to_recieve = []

    for person in people:
        #Calcular disponible a pagar
        person.has_to_recieve = person.spent - individual_payment
        #unicar en la lista
        if person.has_to_recieve >= 0:
            have_to_recieve.append(person)

        else:
            have_to_pay.append(person)

    #ordenar la lista de mayor a menor
    have_to_pay.sort(key=lambda person: person.has_to_recieve, reverse=True)
    #Ordenar la lista de menor a mayor
    have_to_recieve.sort(key=lambda person: person.has_to_recieve)

    #Para cada persona que debe pagar se hace:
    for person in have_to_pay:
        #Hasta que haya pagado toda su deuda (o no quede nadie a quien pagarle) se hace:
        while abs(person.has_to_recieve)>0 and len(have_to_recieve)>0:
            #si lo que tiene disponible es menor a lo que se le ha de pagar a la persona, entonces:
            if(abs(person.has_to_recieve)<=have_to_recieve[0].has_to_recieve):
                # actualiza que le va a pagar a X persona Y monto
                person.split.append({
                    'name': have_to_recieve[0].name,
                    'amount': abs(person.has_to_recieve)

                })
                #Se actualiza lo que se le debe a una perswona (el has to recieve del anterior es negativo, por eso se suma y no se resta)
                have_to_recieve[0].has_to_recieve = have_to_recieve[0].has_to_recieve + person.has_to_recieve
                #Se actualiza su disponible a 0
                person.has_to_recieve = 0

            else: 
                #Actualiza que le va a pagar a X persona Y monto

                person.split.append({
                    'name': have_to_recieve[0].name,
                    'amount': have_to_recieve[0].has_to_recieve 



                })
                #Se actualiza lo que ha de pagar esta persona
                person.has_to_recieve = person.has_to_recieve + have_to_recieve[0].has_to_recieve
                #Se actualiza su disponible a 0 y se elimina de la lista
                have_to_recieve[0].has_to_recieve = 0
                have_to_recieve.remove(have_to_recieve[0])


    for x in people:

        for y in x.split:
            a = y['amount']
            print(f"{(x.name).capitalize()} Le tiene que pagar a {(y['name']).capitalize()} un total de: ${'%.2f' % round(a,2)} ")
        

    splits.append("Split")