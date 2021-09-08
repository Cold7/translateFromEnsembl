from glob import glob

if __name__ == "__main__":
	print("Este programa toma como input una carpeta (ejemplo ./mt_4s_1_2_3/) donde dentro de esta carpeta estan varios los resultados de los archivos de conteo realizado con HTSeq-count y que finalmente entrega los genes que se estan expresando en todas las condiciones (count  mayor que 0")
	print("\n\n")
	carpeta = input("Ingrese nombre de carpeta a analizar. Recuerde agregar el / al final del nombre de la carpeta: ")
	archivos = glob(carpeta+"*.log")
	archivo_salida = input("Ingrese nombre del nombre del archivo de salida (ejemplo ./mt_4s_1_2_3.log): ")
	salida = open(archivo_salida,"w")
	diccionario_genes = {} #este diccionario tendra el id de los genes y en cuantas condiciones esta
	for nombre_archivo in archivos:
		archivo = open(nombre_archivo, "r")
		for linea in archivo:
			if "ENS" in linea: #asi se evitan las lineas que no tengan los id de los genes
				linea = linea[:-1].split(",")
				if int(linea[1]) > 0:
					id = linea[0]
					if id in diccionario_genes:
						diccionario_genes[id] += 1
					else:
						diccionario_genes[id] = 1
		archivo.close()
						
	#ahora se recorre el diccionario_genes y se ve los genes que estan en los 3 archivos
	for id in diccionario_genes:
		if diccionario_genes[id] == len(archivos):
			salida.write(id+"\n")

	print("\nListo!!")
	salida.close()
