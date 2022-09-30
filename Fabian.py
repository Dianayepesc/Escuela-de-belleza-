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
