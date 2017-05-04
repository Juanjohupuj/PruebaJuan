#1
def usura(valor, interes, numcuotas):

    """
    Esta función permite determinar el plan de negocios para un cliente n
    dependiendo sus facilidade de pago y condiciones del préstamo
    """

    int_acumulado=0
    pago_capital=0

    if (valor>0 and interes>= 1 and interes <=5 and numcuotas>0):
        cuota=0

        while (cuota<numcuotas):

            saldopendiente= valor -(pago_capital*cuota)
            pago_capital=valor/numcuotas

            pago_interes=saldopendiente*(interes/100)

            cuota_mensual= pago_capital + pago_interes
            cuota= cuota +1

            print("El numero de cuotas", " - ", cuota+1 , "Cuota mensual",  " -  " , cuota_mensual)

    print(int_acumulado)

usura(100000,3, 9)
#2
def distancia(Kilometros, Gasolina):
    """
    Kilómetros representa los km recorridos
    La Gasolina respresenta la Gasolina Utilizada para recorrer dichos kilómetros
    """
    distancia=Kilometros
    galones=Gasolina
    rendimiento=0

    while(galones>rendimiento and distancia>rendimiento):
        ditancia= distancia* (1/2*galones-1)
        rendimiento = rendimiento +distancia

        return distancia
