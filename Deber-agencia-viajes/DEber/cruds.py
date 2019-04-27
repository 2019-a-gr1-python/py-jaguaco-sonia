from AgendarViaje import AgendarViaje
from lugar import lugar
import os

path1 = "./registro_viaje.txt"

def ingresar_lugar():
	os.system ("cls")
	print('\n********** Nuevo lugar  *********')
	print('\n   Ingrese los siguientes datos ')
	
	nombre_lugar = input('\nNombre destino turistico: ')
	descripcion_lugar = input('\nDescripcion Geografica: ')

	os.system ("cls")

	return lugar(nombre_lugar, descripcion_lugar)


def ingresar_destinoturistico():
	os.system ("cls")
	print('\n********** Agendar *********')
	print('\nIngrese los siguientes datos del lugar: ')

	nombre = input('\nNombre Sitio a Visitar: ')
	lugar = input('\nUbicacion Geografica: ')
	
	precio = input('\nMonto: $')
	
	os.system ("cls")
	return AgendarViaje(nombre, lugar, precio)


def registrar_elemento():
	while(True):
		print('\n**************** Registro ***************')
		print('\nQue desea Ingresar')
		print('\n1. Nuevo Lugar')
		print('\n2. Agendar Viaje')
		print('\n\n3. Salir')

		numero_opcion = int(input('\nEscriba el numero de la opcion escogida: '))

		if numero_opcion is 1:
			registrar("./registro_lugar.txt", ingresar_lugar())
			break
		elif numero_opcion is 2:
			registrar("./registro_viaje.txt", ingresar_destinoturistico())
			break
		elif numero_opcion is 3:
			break
		else:
			os.system ("cls")
			print('Opcion no existe, ingrese un numero valido')

	return


def registrar(path1, objeto):
	file = open(path1, "a")
	file.write(objeto.__str__('w') + "\n")
	file.close()
	



def actualizar_destinoturistico():
	print('\n********** Actualizar Viaje Agendado *********')
	nombre = input('\nNombre Sitio a Visitar:  ')
	archivo_abierto = open(path1,"r")
	lineas_archivo = archivo_abierto.readlines()
	archivo_abierto.close()
	archivo_nuevo = open(path1,"w")
	archivo_nuevo.write("")
	archivo_nuevo.close()
	file = open(path1, "a")
	lineas_archivo_nuevo = []
	for linea in lineas_archivo:
		linea_leida = linea.split(";",1)
		if linea_leida[0] != nombre:
			file.write(str(linea))
		else:
			linea_leida = linea.split(";")
			destinoturistico = AgendarViaje(linea_leida[0], linea_leida[1],linea_leida[2])
			os.system ("cls")
			flag = True
			while (flag == True):
				print('\n**************** Actualizar Datos *******************')
				print('\nEscoja el dato que desee actualizar:')
				print('\n1. Nombre Sitio a Visitar')
				print('\n2. lugarbicacion Geografica')
				print('\n3. Monto')
				print('\n\n4. Cancelar')

				dato_a_actualizar = int(input('\nIngrese el numero de la opcion escogida: '))

				if dato_a_actualizar is 1:
					nombre = input('\nIngrese nuevo Destino a vijar: ')
					destinoturistico.set_nombre(nombre)
					file.write(destinoturistico.__str__('w'))
				elif dato_a_actualizar is 2:
					lugar = input('\nIngrese nueva Ubicacion Geografica: ')
					destinoturistico.set_lugar(lugar)
					file.write(destinoturistico.__str__('w'))
				elif dato_a_actualizar is 3:
					precio = input('\nIngrese nuevo Monto: ')
					destinoturistico.set_precio(precio)
					file.write(destinoturistico.__str__('w'))
				elif dato_a_actualizar is 4:
					break
	file.close()
	


def recorrer_archivo(lineas_archivo, nombre):
	for linea in lineas_archivo:
		linea_leida = linea.split(";",1)
		if linea_leida[0] == nombre:
			linea_leida = linea.split(";")
			return AgendarViaje(linea_leida[0], linea_leida[1],linea_leida[2])


def buscar_destinoturistico():
	
	while(True):
		os.system ("cls")
		print('\n********** Buscar Viajes Agendados ***********')
		print('\nIngrese el nombre del sitio a buscar')
		nombre = input('\nNombre del destino agendado: ')
		os.system ("cls")
		archivo_abierto = open(path1)
		print(recorrer_archivo(archivo_abierto.readlines(), nombre).__str__('p'))
		respuesta = input ('\n\n¿Desea realizar otra búsqueda? (S/N): ')
		
		archivo_abierto.close()

		if respuesta is 'S':
			continue
		elif respuesta is 'N':
			os.system ("cls")
			break

	return



def menu_buscar():
	while True:
		
		print('\n********** Buscar ***********')
		print('\nMenu de opciones de busqueda: ')
		print('\n1. Buscar destinoturistico por nombre')
		print('\n3. Salir')
		opcion_busqueda = int(input('\nIngrese el numero de la opcion escogida: '))


		if opcion_busqueda is 1:
			buscar_destinoturistico()
					
		elif opcion_busqueda is 3:
			break
		else:
			os.system ("cls")
			print('Opcion no existe, ingrese un numero valido')

	




def eliminar(elemento, path):
	print('\n********** Eliminar ' + elemento + ' ***********')
	print('\nIngrese el nombre del ' + elemento.lower() + ' a eliminar')
	nombre = input('\nNombre: ')
	os.system ("cls")
	archivo_abierto = open(path,"r")
	lineas_archivo = archivo_abierto.readlines()
	archivo_abierto = open(path,"w")
	archivo_abierto.write("")
	archivo_abierto = open(path, "a")
	
	for linea in lineas_archivo:
		linea_leida = linea.split(";",1)
		if linea_leida[0] != nombre:
			archivo_abierto.write(str(linea))
	
	archivo_abierto.close()
	return

def eliminar_elemento():
	
	elemento_elegido = ''
	path = ''
	
	while(True):
		print('\n**************** Eliminar ***************')
		print('\nElementos que se pueden eliminar')
		print('\n1. lugar')
		print('\n2. destinoturistico')
		print('\n3. Salir')

		numero_opcion = int(input('\nEscriba el numero de la opcion escogida: '))
		

		if numero_opcion is 1:
			elemento_elegido = 'lugar'
			path ='./registro_lugar.txt'
			break
		elif numero_opcion is 2:
			elemento_elegido = 'AgendarViaje'
			path ='./registro_viaje.txt'
			break
		elif numero_opcion is 3:
			return
		else:
			os.system ("cls")
			print('Opcion no existe, ingrese un numero valido')
	eliminar(elemento_elegido, path)
	return