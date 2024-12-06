import time
import requests
arch = open(r"C:\Users\Juan\Desktop\uniq\miniproyectos\01_mc names\spanish_2.txt", "r")
texto = arch.read().splitlines()
arch.close()
cant =len(texto)
abcda = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
player = ""
i=0
attempt=1
def erasing(x):
	x.pop(0)
	arch = open(r"C:\Users\Juan\Desktop\uniq\miniproyectos\01_mc names\spanish_2.txt", "w")
	for escribir in x:
		arch.write(escribir+"\n")
	arch.close()
	
for i in range(0,cant):
	faltan = len(texto)
	quedan = (cant-faltan)+1
	player = texto[0]
	url = "https://api.mojang.com/users/profiles/minecraft/"+player	
	try:
		r = requests.get(url)
		data = r.json()
		if data == {'error': 'TooManyRequestsException', 'errorMessage': 'The client has sent too many requests within a certain amount of time'}:
			print("")
			print("Error: server busy")
			print("")
			print("Intentando de nuevo en 15 segundos")
			print("")
			for i in range(10,0,-1):
				time.sleep(1)
				
			for i in range(5,0,-1):
				print("Intentando de nuevo en",i,"segundos")
				time.sleep(1)
			print("")
		else:
			print("                  NO",player, "NO")
			erasing(texto)
			print("Faltan",faltan)
			
	except Exception:
		print("                                         **",player, "**")
		erasing(texto)
		with open("palabras encontradas.txt", "a") as m:
			m.write(player+"\n")
		print("Faltan",faltan)
print("")
print("La busqueda ha terminado satisfactoriamente")