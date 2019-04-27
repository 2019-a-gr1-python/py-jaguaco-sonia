
import cruds

import os
from AgendarViaje import AgendarViaje
from lugar import lugar

def main():
	
	while True:
		os.system ("cls")
		
		print('\n**********AGENCIA DE VIAJES*********')
		print('\nMenu de opciones')
		print('\n1. Resgistrar')
		print('\n2. Actualizar')
		print('\n3. Buscar')
		print('\n4. Eliminar')
		print('\n5. Salir')

		numero_accion = int(input('\nIngrese el numero de la opcion escogida: '))

		os.system ("cls")
		

		if numero_accion is 1:
			cruds.registrar_elemento()
		elif numero_accion is 2:
			cruds.actualizar_destinoturistico()
		elif numero_accion is 3:
			cruds.menu_buscar()
		elif numero_accion is 4:
			cruds.eliminar_elemento()
		elif numero_accion is 5:
			break
		else:
		 print("Accion no valida")




main()