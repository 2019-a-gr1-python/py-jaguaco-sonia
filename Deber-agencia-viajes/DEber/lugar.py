class lugar:
	nombre = ''
	descripcion = ''

	def __init__(self, nombre, descripcion):
		self.nombre = nombre
		self.descripcion = descripcion
		
	def __str__(self, modo):
		cadena = ''
		if modo is 'w':	
			cadena = f'{self.nombre};{self.descripcion}'
			return cadena

		else:
			cadena = f'Nombre: {self.nombre}\nDescripcion: {self.descripcion}\n'
			return cadena

	def set_nombre(self, nombre):
		self.nombre = nombre

	def set_descripcion(self, descripcion):
		self.descripcion = descripcion