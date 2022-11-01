'''
Ejercitación Encapsulamiento
Crear una clase Atleta, que tenga su nombre, apellido, altura, peso y teléfono.
Decidir que atributos deben ser públicos y cuales privados. Crear los métodos get y set que crea necesarios.
'''

class Atleta:

  def __init__(self, nombre, apellido, altura, peso, telefono):
    self.nombre = nombre
    self.apellido = apellido
    self.altura = altura
    self.__peso = peso
    self.__telefono = telefono

  def get_altura(self):
    return self.__altura

  def get_peso(self):
    return self.__peso

  def get_telefono(self):
    return self.__telefono

  def set_altura(self,altura):
    self.__altura = altura

  def set_peso(self,peso):
    self.__peso = peso

  def set_telefono(self, telefono):
    self.__telefono = telefono

  def __str__(self):
    return "Atleta: " + self.nombre + " " + self.apellido

atleta1 = Atleta("María","Cruz", 1.70, 55, 351645512)

print (atleta1)

print(atleta1.nombre)

print(atleta1.get_peso())

print(atleta1.get_telefono())

atleta1.set_altura(1.72)

print(atleta1.get_altura())