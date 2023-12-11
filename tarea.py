class Animales:
    def _init_(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad  # Encapsulación

    def edad(self):
        return self.__edad

    def mostrar_informacion(self):
        print("Animales:", self.nombre)
        print("Edad", self.__edad)

class zoologico_A(Animales):
    def _init_(self, especie, edad, ayosC):
        super()._init_(especie, edad)
        self.__ayosC = ayosC           # Encapsulación

    def calcular_edadL(self):  # Polimorfismo
        return super().ayosC() - self.__edad

    def mostrar_informacion(self):  # Polimorfimo
        super().mostrar_informacion()
        print("Años en cautiberio", self.__edad)


class personal(Animales):
    def _init_(self, nombre, edad, Area):
        super()._init_(nombre, edad)
        self.Area = Area  # Abstracción

    def mostrar_informacion(self):  # Polimorfis-mo
        super().mostrar_informacion()
        print("Area  de trabajo:", self.Area)


# Uso de las clases
Animals = Animales("Juan", 50)
zoological_A = zoologico_A("raton", 70, 10)
personal = personal("Carlos", 60, "zotano")

# Mostrar información y salario de cada empleado
print("Información del Empleado:")
Animales.mostrar_informacion()
print("EDAD:", Animales.edad())

print("\nInformación del Gerente:")
zoologico_A.mostrar_informacion()
print("EDAD:", zoologico_A.edad())

print("\nInformación del Desarrollador:")
personal.mostrar_informacion()
print("EDAD:", personal.edad())
