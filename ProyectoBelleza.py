print("Menú")
print("1: Comprar")
print("2: Catálogo")
print("3: Agendar Cita")
print("4: Servicio a Domicilio")
print("5: Cancelación de Cita")
x=int(input("Digíte una opción: "))
if x==1:
    print("¿Está registrado?")
    print("1: Si")
    print("2: No")
    y=int(input("Digíte una opción: "))
    if x==1:
        q=int(input("Digíte su identificación: "))
        print("Gracias por su compra")
elif x==2:
    print("Productos de cuidado personal: shampoo, tratamientos, aseo personal, jabones")
elif x==3:
    v=float(input("¿A qué hora desearía agendar una cita con nosotros?"))
    print("Su cita se ha agendado exitósamente")
elif x==4: 
    print("Compras a domicilio")
    w=int(input("Digite opcion: "))
    if w==1:
        print("Desea que su compra sea a domicilio 1 para si, 2 para no ")
        z=int(input("Digite su opcion: "))
        if z==1:
            e=str(input("Digite direccion: "))
        elif z==2:
            print("Acerquese a nuestros puntos oficiales que mas se acerquen a su necesidad")
elif x==5:        
    print("1 para cancerla cita o 2 para reasignar cita")
    n=int(input("Digite opccion: "))
    if n==1:
        a=int(input("Digite numero de reserva:"))
        print("Su cita ha sido cancelada: ")
    elif n==2:
        p=int(input("Digite numero de reserva: "))
        k=float(input("Digite hora nueva: "))
        print("Su cita ha sido reaccinada")
