'''
Ejercicio:
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física,
Química, Historia y Lengua) en una lista, PREGUNTE al usuario la nota que ha sacado en cada asignatura
y ELIMINE de la lista las asignaturas aprobadas. Al final el programa debe MOSTRAR por pantalla las
asignaturas que el usuario tiene que repetir.
'''

materias = ["Matematica", "Fisica", "Quimica", "Historia", "Lengua"]
notas = []

for materia in materias:
  nota = int(input("Ingresar nota de " + materia +": "))
  notas.append(nota)
for j in notas:
  n = notas.index(j)
  if j>=6:
    materias.pop(n)
    notas.pop(n)

print ("Tiene que repetir:", materias)