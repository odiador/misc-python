import sys
import requests
import random
import time
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
import tkinter as tk
import tkinter.ttk as ttk


def carganding():
	C = Canvas(ventana2, height = 600, width = 600)
	C.grid(column = 4,row = 0, padx = 5, pady=5,columnspan=1)
	ventana2.update()
	coord = 100, 100, 400, 400
	arc = C.create_arc(coord, start = 0, extent = 50, fill = "red")
	oval = C.create_oval(120,120,380,380,  fill = "white")
	x = 50
	i=0
	onn= True
	while i <360:
		time.sleep(0.041666)
		C.itemconfig(arc, start = i, extent = x)
		if x>360:
			x=0
		x=x+10
		ventana2.update()
		i=i+5
		
def textos(x,y,z,a,b,c):
	space = ttk.Label(ventana, text=b,font="12")
	space.grid(column = x,row = y, padx = z, pady=a,columnspan=c)

def textos2(x,y,z,a,b,c):
	space = ttk.Label(ventana2, text=b,font="12")
	space.grid(column = x,row = y, padx = z, pady=a,columnspan=c)

def botonPres():
	tiponame = int(tiponameVar.get())
	try:
		n = int(entry1.get())
		guion = int(guionVar.get())
		cadena = int(entry2.get())
		ventana2.title('Calculando...')
		ventanas(ventana2,ventana)
		
	except Exception:
		messagebox.showerror("Advertencia", "Error: Diligencia bien los datos")
	if guion ==0:
		abc123 = abc123ConG
		abcda = abcdaConG
		a123 = a123ConG
	else:
		abc123 = abc123SinG
		abcda = abcdaSinG
		a123 = a123SinG
	player = ""
	attempt=1
	i = n
	found = 0
	nombres = ""
	global nombresEnter
	nombresEnter = ""
	while i>0:
		finded = False
		while finded ==False:
			f = cadena
			player = ""
			while f>0:
				if tiponame == 0:
					player = player+random.choice(abcda)
				else:
					if tiponame == 1 :
						player = player+random.choice(a123)
					else:
						player = player+random.choice(abc123)
				f=f-1
			url = "https://api.mojang.com/users/profiles/minecraft/"+player	
			try:
				r = requests.get(url)
				ventana2.update()
				textsbus= ['Busqueda',str(attempt),':',str(player),'- encontrados:',str(found)]
				insertar = ''
				for s in textsbus:
					insertar += s + ' '
				lista.insert(END,insertar)
				data = r.json()
				lista.insert(END,"Failure")
				numLista = lista.size()-1
				lista.itemconfig(numLista, {'fg':'blue'})
				if data == {'error': 'TooManyRequestsException', 'errorMessage': 'The client has sent too many requests within a certain amount of time'}:
					cantnames = ['Cantidad de nombres:',str(found),'de',str(n)]
					insertar = ''
					for s in cantnames:
						insertar += s + ' '
					
					lista.insert(END,insertar)
					lista.insert(END,"Nombres encontrados:")
					lista.insert(END,nombres)
					messagebox.showerror("Error", "Error: servidor ocupado")
			except Exception:
				ventana2.update()
				lista.insert(END,"Success")
				numLista = lista.size()-1
				lista.itemconfig(numLista, {'fg':'green'})
				finded = True
				nombres = nombres+player+" "
				nombresEnter = nombresEnter+player+"\n"
				found=found+1
				with open("01_output.txt", "a") as m:
					m.write(player+"\n")
			
			attempt=attempt+1
		i=i-1
	lista.insert(END,"")
	insertar = ''
	cantnames = ['Cantidad de nombres:',str(found),'de',str(n)]
	for s in cantnames:
		insertar += s + ' '
					
	lista.insert(END,insertar)
	lista.insert(END,"Nombres encontrados:")
	lista.insert(END,nombres)
	ventana2.title('Programa')

def cerrar():
	sys.exit()

def ventanas(x,y):
		x.update()
		x.deiconify()
		y.withdraw()

def botonAceptar():
	lista.delete(0,END)
	ventanas(ventana,ventana2)

def guardar():
	arch = asksaveasfilename(title="Guardar Archivo",defaultextension=("Documentos de Texto","*.txt"), filetypes=(("Documentos de Texto", "*.txt"),("Todos los Archivos", "*.*") ))
	if arch:
		f = open(arch, 'a')
		contents = lista.get(0, 'end')
		insertar = ''
		for s in contents:
			insertar += s + '\n'
		f.write(nombresEnter)
		f.close()

def enterPres(event):
	botonPres()



ventana = Tk()
ventana.grid_columnconfigure(0, weight=1)
ventana.title('Programa')

ventana2 = Tk()
ventana2.grid_columnconfigure(0, weight=1)
ventana2.grid_rowconfigure(0, weight=1)
ventanas(ventana,ventana2)


abc123SinG = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
abc123ConG = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','_']
abcdaSinG = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
abcdaConG = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','_']
a123SinG = ['0','1','2','3','4','5','6','7','8','9']
a123ConG = ['0','1','2','3','4','5','6','7','8','9','_']

textos(0,0,10,3,"Insert titIe",3)
textos(0,1,5,5,"Cuantos nombres quieres encontrar?",1)

entry1 = ttk.Entry(ventana,font="12",width=5,justify=CENTER)
entry1.grid(column = 0,row = 2, padx = 5, pady=5,columnspan=1)

textos(1,1,5,5,"De cuantas letras lo(s) necesitas?",2)

entry2 = ttk.Entry(ventana,font="12",width=5,justify=CENTER)
entry2.grid(column = 1,row = 2, padx = 5, pady=5,columnspan=2)

textos(0,3,5,5,"Lo(s) quieres con solo letras numeros o ambas?",1)

tiponameVar = IntVar()
R1 = Radiobutton(ventana, text="Letras", variable=tiponameVar, value=0)
R1.grid(column = 0,row = 4, padx = 20, pady=5,columnspan=1,sticky=W)

R2 = Radiobutton(ventana, text="Numeros", variable=tiponameVar, value=1)
R2.grid(column = 0,row = 5, padx = 20, pady=5,columnspan=1,sticky=W)

R3 = Radiobutton(ventana, text="Ambas", variable=tiponameVar, value=2)
R3.grid(column = 0,row = 6, padx = 20, pady=5,columnspan=1,sticky=W)

guionVar = IntVar()
entry4 = ttk.Checkbutton(ventana,text="Con guion bajo o sin?",onvalue=0,offvalue=1,variable=guionVar,cursor="crosshair")
entry4.grid(column = 1,row = 3, padx = 5, pady=5,columnspan=2,rowspan=2)



boton = ttk.Button(ventana,text="Calcular",command=lambda:botonPres())
boton.grid(column = 1,row = 5, padx = 5, pady=5,rowspan=2,sticky=E)

ventana.bind('<Return>', enterPres)

boton2 = ttk.Button(ventana,text="Cerrar",command=lambda:cerrar())
boton2.grid(column = 2,row = 5, padx = 5, pady=5,rowspan=2,sticky=W)

frameWait = Frame(ventana2) 
frameWait.pack()
frameWait.grid(row=0, column=0, sticky=N+E+S+W)

frame = Frame(ventana2) 
texto2 = Label(frame, text ='x')  
scrol = Scrollbar(frame,orient="vertical") 
scrol2 = Scrollbar(frame,orient="horizontal") 
lista = Listbox(frame,width=120,height= 20)
lista.configure(yscrollcommand = scrol.set,xscrollcommand = scrol2.set)


scrol.config(command = lista.yview)
scrol2.config(command = lista.xview)

texto2.pack(side=TOP,fill=BOTH)


scrol2.pack(side=BOTTOM, fill=X)
scrol.pack(side=RIGHT, fill=Y)
lista.pack(side=LEFT, fill=BOTH, expand=1)
frame.grid(row=0, column=0, rowspan=1,columnspan=3, sticky=N+E+S+W)





boton3_2 =ttk.Button(ventana2,text="Aceptar",command=lambda:botonAceptar())
boton3_2.grid(column = 0,row = 2, padx = 5, pady=5,columnspan=1,sticky="SE")

boton4_2 =ttk.Button(ventana2,text="Guardar",command=lambda:guardar())
boton4_2.grid(column = 1,row = 2, padx = 5, pady=5,columnspan=1,sticky="SE")

boton5_2 =ttk.Button(ventana2,text="Cerrar",command=lambda:cerrar())
boton5_2.grid(column = 2,row = 2, padx = 5, pady=5,columnspan=1,sticky="SE")


ventana.mainloop()
ventana2.mainloop()