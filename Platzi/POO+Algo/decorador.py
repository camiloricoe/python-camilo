def funcion_decoradora(funcion):
	def wrapper():
		print("Este es el último mensaje...")
		funcion()
		print("Este es el primer mensaje ;)")
	return wrapper

@funcion_decoradora
def zumbido():
	print("Buzzzzzz")


zumbido()

"""
#estos dos codigos funcionan igual 

def funcion_decoradora(funcion):
	def wrapper():
		print("Este es el último mensaje...")
		funcion()
		print("Este es el primer mensaje ;)")
	return wrapper


def zumbido():
	print("Buzzzzzz")


zumbido = funcion_decoradora(zumbido)
zumbido()



"""


