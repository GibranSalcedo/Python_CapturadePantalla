import pyautogui
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

# Interfaz
def crearWidgets():
	etiquetaGuardar = Label(vn, text = 'Guardar como: ', font = ('', 10, 'bold'))
	etiquetaGuardar.grid(row = 1, column = 0, pady = 5, padx = 5)

	vn.textoGuardar = Entry(vn, width = 30)
	vn.textoGuardar.grid(row = 1, column = 1, pady = 5, padx = 5)

	botonGuardar = Button(vn, text = 'Navegar', width = 10, command = navegar)
	botonGuardar.grid(row = 1, column = 2, pady = 5, padx = 5)

	botonCaptura = Button(vn, text = 'Captura', width = 10, command = captura)
	botonCaptura.grid(row = 2, column = 1, pady = 5, padx = 5)

# Función para navegar y guardar la imagen
def navegar():
	vn.archivoNombre = filedialog.asksaveasfilename(title = 'Guardar como',
													initialdir = 'C:\\Users\\GJ\\Desktop',
													defaultextension = '.png',
													filetypes = (('Archivo PNG', '*.png'),('Todos los archivos', '*.*')))
	vn.textoGuardar.insert('1', vn.archivoNombre)


def captura():
	captura = pyautogui.screenshot()

	captura.save(vn.archivoNombre)
	messagebox.showinfo('Exito', 'Captura guardada')

vn = tk.Tk()
vn.title('Captura de pantalla')
crearWidgets()
vn.mainloop()