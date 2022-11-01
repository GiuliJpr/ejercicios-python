'''
Ejercicio:
Crear una clase Persona.
Agregar 3 atributos de instancia y por lo menos 2 de clase.
Además el constructor y dos métodos(uno con parámetros y otro sin parámetros)
Luego instanciar a dos personas y mostrarlas.
'''

class Persona:
  trabajo = "Programador"

  def __init__(self, nombre, apellido, edad):

    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad

  def hablar(self):
    print("Soy programador/a!")

  def hobby(self, hobby):
    print("Mi hobby es {}.".format(hobby))


persona1 = Persona("Carlos","Perez",34)

print(persona1.nombre)
persona1.hablar()
persona1.hobby("pintar")


persona2 = Persona("María","Cruz",25)

print(persona2.edad)
persona2.hablar()
persona2.hobby("jugar videojuegos")