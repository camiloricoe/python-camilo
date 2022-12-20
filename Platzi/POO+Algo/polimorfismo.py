class Persona:
    def __init__(self,nombre):
        self.nombre=nombre

    def avanza(self):
        print('Ando caminado')


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Ando moviendome en mi bici')

def main():
    perosna = Persona('Camilo')
    perosna.avanza()

    ciclista = Ciclista('Diego')
    ciclista.avanza()

if __name__ == '__main__':
    main()
