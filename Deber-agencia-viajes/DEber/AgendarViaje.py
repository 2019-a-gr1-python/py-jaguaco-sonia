class AgendarViaje:
	nombre = ''
	lugar = ''
	#censura = 0
	precio = 0.00
	#plataforma = ''

	def __init__(self, nombre, lugar, #censura, 
		precio, #plataforma
		):
		self.nombre = nombre
		self.lugar = lugar
		
		self.precio = precio
	

	def __str__(self, modo):
		cadena = ''
		if modo is 'w':	
			
			cadena = f'{self.nombre};{self.lugar};{self.precio}'
			return cadena

		else:
			cadena = f'Nombre: {self.nombre}\nlugar: {self.lugar}\nPrecio: ${self.precio}\n'
			return cadena

	def set_nombre(self, nombre):
		self.nombre = nombre

	def set_lugar(self, lugar):
		self.lugar = lugar

	def set_precio(self, precio):
		self.precio = precio

