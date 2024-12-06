import time
import os
carpeta = input("Escribe la ruta: ")
array = os.listdir(carpeta)
for i in array:
	if i.startswith("IMG"):
		if i.endswith(".jpg"):
			M=int(i[8:10])
			d=i[10:12]
			h=i[13:15]
			m=i[15:17]
			s=i[17:19]
			meses = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
			mes = meses[M-1]
		nuevo =mes+" "+d+" - "+h+"_"+m+"_"+s
		carpetaAnt = carpeta+"\\"+i
		carpetaNueva = carpeta+"\\"+nuevo+".jpg"
		os.rename(carpetaAnt, carpetaNueva)