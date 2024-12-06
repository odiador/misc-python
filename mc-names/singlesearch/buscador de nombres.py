import sys
import requests
abcda = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
player = ""
i=0
attempt=1
print("******************************")
print("*Search Available Names (SAN)*")
print("******************************")
print("")
player = str(input("Escribe el nombre del jugador: "))
url = "https://api.mojang.com/users/profiles/minecraft/"+player	
try:
	r = requests.get(url)
	data = r.json()
	print("El nombre",player, "esta ocupado")
	if data == {'error': 'TooManyRequestsException', 'errorMessage': 'The client has sent too many requests within a certain amount of time'}:
		print("")
		print("Error: server busy")
		sys.exit()
except Exception:
	print("El nombre",player, "esta libre")
	with open("nombres.txt", "a") as m:
		m.write(player+"\n")