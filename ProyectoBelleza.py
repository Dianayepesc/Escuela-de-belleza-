print("Menú")
print("2: Comprar")
print("3: Catálogo")
print("4: Agendar Cita")
print("5: Cancelacion de cita")
x=int(input("Digíte una opción: "))
if x==2:
    print("¿Está registrado?")
    print("1: Si")
    print("2: No")
    y=int(input("Digíte una opción: "))
    if x==1:
        q=int(input("Digíte su identificación: "))
        print("Gracias por su compra")
elif x==3:
    print("Productos de cuidado personal: shampoo, tratamientos, aseo personal, jabones")
elif x==4:
    print("¿Desea agendar una cita con nosotros?")
    print("Digite 1 para si, 2 para no: ")
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
