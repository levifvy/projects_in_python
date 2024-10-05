'''Exercici 6: Validació de dates en format DD/MM/AAAA 
Objectiu: Escriu un regex per validar dates en format DD/MM/AAAA. 
Entrada: 25/12/2021, 01/01/1999, 31/02/2020, 30/04/2020, 31/02/2024, 54/20/2024
'''
import re

#patro = re.compile(r"(?:^|\s|,)[0-9]{2}\/[0-9]{2}\/[0-9]{4}(?=$|\s|,|\.)")
patro = re.compile(r"(?:^|\s|,)(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/([0-9]{4})(?=$|\s|,|\.)")

entrada = input("Ingresa un texto con fechas: ")

resultado = patro.findall(entrada)

def es_anio_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def es_fecha_valida(dia, mes, anio):
    dia = int(dia)
    mes = int(mes)
    anio = int(anio)

    if mes < 1 or mes > 12:
        return False

    # ternaria
    dias_por_mes = [31, 29 if es_anio_bisiesto(anio) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if dia < 1 or dia > dias_por_mes[mes - 1]:
        return False

    return True

fechas_validas = [print('/'.join(fecha)) for fecha in resultado if es_fecha_valida(*fecha)]
