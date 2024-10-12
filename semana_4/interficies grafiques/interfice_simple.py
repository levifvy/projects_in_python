import tkinter as tk
from tkinter import font

def limitador():
    print("HOLA")

'''
5. Llegeix els quatre nombres que conformen una adreça IP, valida si és una IP 
correcta i ho escriu.
'''
import re

#text = input("Introduce IP\n")
patron = re.compile(r"(((?<!\S)((0|[1-9][0-9]?|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}(0|[1-9][0-9]?|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?!\S)))")

# Interfaz gráfica
# inicializador de root
root = tk.Tk()
amplada = root.winfo_screenwidth() // 2
alcada = root.winfo_screenheight() // 2
strink = '{}x{}'.format(amplada,alcada)
root.geometry(strink)
root.attributes('-fullscreen',False)

# inicializador Frame
frame1 = tk.Frame(root,bg='orange')
frame1.place(x=0, y=0, width = amplada, height = alcada)

#Definicio de Widget Entry
fuente = font.Font(family="Helvetica", size=20)

anchura = 0.5 * amplada // 10
espaciado = 20
extremo_izquierdo = 0.5 * amplada - (3 * (anchura + espaciado) + anchura) / 2
#extremo_izquierdo = mitad
entries = []
labels = []

# Primero, 3 entries y 3 puntos
for i in range(0, 3):
    entries.append(tk.Entry(frame1, font = fuente, command = limitador))
    entries[i].place( x = extremo_izquierdo + i * (anchura + espaciado), y = 7.5 * alcada // 10, width = anchura, height= 0.5 * alcada // 10)
    labels.append(tk.Label(frame1, text = ".", bg = frame1.cget('bg'), font=fuente))
    labels[i].place( x = anchura + extremo_izquierdo + i * (anchura + espaciado), y = 7.5 * alcada // 10, width = espaciado, height= 0.5 * alcada // 10)

# Ahora, el último entry
entries.append(tk.Entry(frame1, font=fuente))
entries[3].place( x = extremo_izquierdo + 3 * (anchura + espaciado), y = 7.5 * alcada // 10, width = anchura, height= 0.5 * alcada // 10)



#labels = []
#for i in range(0, 3):
#    labels.append(tk.Label(frame1, text = ".", bg = frame1.cget('bg'), font=fuente))
#    labels[i].place( x = extremo_izquierdo + i * (anchura + espaciado), y = 7.5 * alcada // 10, width = anchura, height= 0.5 * alcada // 10)





# mantenedor de root
root.mainloop()












'''
if len(patron.findall(text)) > 0:
    print(f"IP correcta ({patron.findall(text)[0][0]})")
#    print(f"IP correcta {text}")
else:
    print("Eso no es una IP")
    #print(patron.findall(text)[0][0])
    #print(f"IP correcta ({patron.findall(text)[0][0]})")
'''