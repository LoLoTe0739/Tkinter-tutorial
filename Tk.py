from tkinter import *

#ventana
ventana = Tk()
ventana.geometry('700x700')
ventana.title('TK PRUEBA')

#botones y etiquetas
texto = Label(ventana, text="HOLA MUNDO xd")
texto.pack()
boton = Button(ventana, text="boton inservible XD")
boton.pack()



ventana.mainloop()