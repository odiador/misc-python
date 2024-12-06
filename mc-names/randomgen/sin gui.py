import sys
import requests
import random
abc123 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
abcda = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a123 = ['0','1','2','3','4','5','6','7','8','9']
print("*******************************************")
print("*Buscador de nombres libres para Minecraft*")
print("*******************************************")
n = int(input("Cuantos nombres quieres encontrar? "))
cadena = int(input("De cuantas letras lo(s) necesitas? "))
tiponame = int(input("Lo(s) quieres con solo letras (0), numeros (1) o ambas(2)? "))
guion = int(input("Con guion bajo (0) o sin (1)? "))
if guion ==0:
	abc123.append("_")
	abcda.append("_")
	a123.append("_")
player = ""
attempt=1
i = n
f = cadena
found = 0
nombres = ""
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
			print("Busqueda",attempt,":",player,"- encontrados:",found)
			data = r.json()
			if data == {'error': 'TooManyRequestsException', 'errorMessage': 'The client has sent too many requests within a certain amount of time'}:
				print("")
				print("Error: servidor ocupado")
				print("")
				print("Cantidad de nombres:",found,"de",n)
				print("Nombres encontrados:")
				print(nombres)
				sys.exit()
		except Exception:
			print("Success")
			finded = True
			nombres = nombres+player+" "
			found=found+1
			with open("singui_output.txt", "a") as m:
				m.write(player+"\n")
		attempt=attempt+1
	i=i-1
print("")
print("Cantidad de nombres encontrados:",found,"de",n)
print("Nombres encontrados:")
print(nombres)