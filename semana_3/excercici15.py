import re
import io


arxiu = io.open(r"C:\\Users\\Alumne_mati1\\Documents\\python_cifo_septiembre_2024\\semana_3\\PRIMER_ESTUDI\\StudentPerformanceFactors.csv","r",encoding = 'utf-8')

llistadecadenes = arxiu.readlines()

print(len(llistadecadenes))

#usar otros dataset de gann cantidad de lineas, sugetrerncia movies#