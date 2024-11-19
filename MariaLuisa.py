# ===================================================================
# Título del trabajo: Seguimiento 1 PII
# Nombre: [Maria Luisa Londoño Moncada]
# Fecha de creación: Noviembre 18, 2024
# Descripción: Este archivo contiene soluciones para diversos ejercicios de manipulación de listas para seguimiento 1 PII C2
# ===================================================================

# -------------------------------------------------------------------
# solución de ejercicios
# -------------------------------------------------------------------

# Ejercicio 1: Crear una lista con los nombres de 5 frutas colombianas favoritas y mostrarla por pantalla.
frutas = ["Lulo", "Guanábana", "Mango", "Borojó", "Maracuyá"]
print(frutas)  # Muestra la lista de frutas.

# Ejercicio 2: Acceder al segundo y cuarto elemento de la lista anterior e imprimirlos.
print(frutas[1])  # Muestra el segundo elemento.
print(frutas[3])  # Muestra el cuarto elemento.

# Ejercicio 3: Crear una lista con los números del 1 al 10 y mostrar su longitud.
numeros = list(range(1, 11))  # Lista del 1 al 10.
print(len(numeros))  # Muestra la longitud de la lista.

# Ejercicio 4: Concatenar las dos listas creadas en los ejercicios 1 y 3.
concatenada = frutas + numeros  # Combina ambas listas.
print(concatenada)  # Muestra la lista concatenada.

# Ejercicio 5: Modificar el tercer elemento de la lista del ejercicio 4 al valor 100.
concatenada[2] = 100  # Cambia el tercer elemento a 100.
print(concatenada)  # Muestra la lista modificada.

# Ejercicio 6: Borrar el último elemento de la lista del ejercicio 4.
concatenada.pop()  # Elimina el último elemento.
print(concatenada)  # Muestra la lista actualizada.

# Ejercicio 7: Crear una lista con 3 números enteros y multiplicar cada elemento por 5.
enteros = [2, 4, 6]
multiplicados = [x * 5 for x in enteros]  # Multiplica cada elemento por 5.
print(multiplicados)

# Ejercicio 8: Crear dos listas con 5 números enteros cada una y multiplicar los elementos correspondientes.
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
resultado = [a * b for a, b in zip(lista1, lista2)]  # Multiplica elementos correspondientes.
print(resultado)

# Ejercicio 9: Crear una lista de listas anidadas y acceder al segundo elemento de la segunda lista.
listas_anidadas = [[1, 2], [3, 4], [5, 6]]
print(listas_anidadas[1][1])  # Accede al segundo elemento de la segunda lista.

# Ejercicio 10: Crear una lista a partir de la lista del ejercicio 3, tomando los elementos del índice 2 al 6.
sublista = numeros[2:7]  # Toma elementos de índice 2 al 6.
print(sublista)

# Ejercicio 11: Usar el método .append() para agregar un nuevo elemento al final de la lista del ejercicio 1.
frutas.append("Guayaba")  # Agrega un nuevo elemento.
print(frutas)

# Ejercicio 12: Usar el método .insert() para agregar un nuevo elemento en la posición 2 de la lista del ejercicio 3.
numeros.insert(2, 20)  # Inserta el número 20 en la posición 2.
print(numeros)

# Ejercicio 13: Usar el método .remove() para eliminar un elemento específico de la lista del ejercicio 7.
multiplicados.remove(10)  # Elimina el valor 10 si existe.
print(multiplicados)

# Ejercicio 14: Usar el método .reverse() para invertir el orden de la lista del ejercicio 4.
concatenada.reverse()  # Invierte el orden de la lista.
print(concatenada)

# Ejercicio 15: Usar el método .sort() para ordenar de forma ascendente la lista del ejercicio 7.
multiplicados.sort()  # Ordena la lista de forma ascendente.
print(multiplicados)

# Ejercicio 16: Usar el método .pop() para eliminar y obtener el último elemento de la lista del ejercicio 4.
ultimo = concatenada.pop()  # Elimina y guarda el último elemento.
print(ultimo)  # Muestra el elemento eliminado.
print(concatenada)  # Muestra la lista actualizada.

# Ejercicio 17: Usar el método .count() para contar cuántas veces aparece un elemento específico en la lista del ejercicio 7.
print(multiplicados.count(15))  # Cuenta cuántas veces aparece el valor 15.

# Ejercicio 18: Usar el método .index() para obtener el índice de un elemento específico en la lista del ejercicio 4.
# Si algún elemento existe, como "100".
print(concatenada.index(100))

# Ejercicio 19: Usar el método .clear() para eliminar todos los elementos de la lista del ejercicio 1.
frutas.clear()  # Elimina todos los elementos de la lista.
print(frutas)  # Muestra la lista vacía.

# Ejercicio 20: Crear una lista vacía y utilizar un bucle for para agregar los números del 1 al 10.
lista_vacia = []  # Crea una lista vacía.
for i in range(1, 11):  # Itera del 1 al 10.
    lista_vacia.append(i)  # Agrega cada número a la lista.
print(lista_vacia)  # Muestra la lista.

# Ejercicio 21: Crear una lista de números enteros y utilizar un bucle while para eliminar los elementos impares.
enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Lista de enteros.
i = 0  # Índice inicial.
while i < len(enteros):  # Mientras haya elementos en la lista.
    if enteros[i] % 2 != 0:  # Si el elemento es impar.
        enteros.pop(i)  # Elimina el elemento.
    else:
        i += 1  # Avanza al siguiente índice si no se elimina.
print(enteros)  # Muestra la lista sin números impares.

# Ejercicio 22: Crear una lista con los nombres de 5 materias favoritas y ordenarlas alfabéticamente.
materias = ["Matemáticas", "Física", "Historia", "Arte", "Programación"]
materias.sort()  # Ordena la lista alfabéticamente.
print(materias)

# Ejercicio 23: Crear una lista con los números del 1 al 15 y mostrar solo los múltiplos de 3.
numeros = list(range(1, 16))  # Lista del 1 al 15.
multiplos_de_3 = [x for x in numeros if x % 3 == 0]  # Filtra múltiplos de 3.
print(multiplos_de_3)

# Ejercicio 24: Crear una lista con los nombres de 10 artistas favoritos y utilizar un bucle for para imprimir cada nombre en mayúsculas.
artistas = ["Shakira", "Juanes", "Carlos Vives", "Maluma", "J Balvin", "Karol G", "Fonseca", "Silvestre Dangond", "Andrés Cepeda", "Sebastián Yatra"]
for artista in artistas:  # Recorre cada artista.
    print(artista.upper())  # Imprime el nombre en mayúsculas.

# Ejercicio 25: Crear una lista con los números del 1 al 20 y utilizar una comprensión de listas para crear una nueva lista con solo los números pares.
numeros = list(range(1, 21))  # Lista del 1 al 20.
pares = [x for x in numeros if x % 2 == 0]  # Filtra números pares.
print(pares)

# Ejercicio 26: Crear una lista con los nombres de los municipios del departamento de Arauca y utilizar un bucle for para imprimir cada nombre en orden inverso.
municipios = ["Arauca", "Arauquita", "Tame", "Saravena", "Fortul", "Cravo Norte", "Puerto Rondón"]
for municipio in municipios:  # Recorre cada municipio.
    print(municipio[::-1])  # Imprime el nombre en orden inverso.

# Ejercicio 27: Crear una lista con los números del 1 al 12 y utilizar una comprensión de listas para crear una nueva lista con los cuadrados de cada número.
numeros = list(range(1, 13))  # Lista del 1 al 12.
cuadrados = [x ** 2 for x in numeros]  # Calcula los cuadrados.
print(cuadrados)

# Ejercicio 28: Crear una lista con los meses del año y utilizar el método .index() para obtener el índice del mes "Junio".
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
print(meses.index("Junio"))  # Obtiene el índice de "Junio".

# Ejercicio 29: Crear una lista con los nombres que usted le pondría a 6 mascotas y utilizar el método .remove() para eliminar una mascota de la lista.
mascotas = ["Luna", "Max", "Bella", "Charlie", "Rocky", "Sasha"]
mascotas.remove("Max")  # Elimina "Max" de la lista.
print(mascotas)

# Ejercicio 30: Crear una lista con los números del 1 al 20 y utilizar el método .sort(reverse=True) para ordenarla de forma descendente.
numeros = list(range(1, 21))  # Lista del 1 al 20.
numeros.sort(reverse=True)  # Ordena de forma descendente.
print(numeros)

# Ejercicio 31: Crear una lista con los nombres de 4 libros favoritos y utilizar el método .append() para agregar un nuevo libro al final de la lista.
libros = ["Cien años de soledad", "Don Quijote", "1984", "El principito"]
libros.append("La Odisea")  # Agrega un nuevo libro.
print(libros)

# Ejercicio 32: Crear una lista con los números del 1 al 15 y utilizar una comprensión de listas para crear una nueva lista con los números impares.
numeros = list(range(1, 16))  # Lista del 1 al 15.
impares = [x for x in numeros if x % 2 != 0]  # Filtra números impares.
print(impares)

# Ejercicio 33: Crear una lista con los nombres de 7 comidas favoritas y utilizar el método .insert() para agregar una nueva comida en la posición 3.
comidas = ["Arepas", "Bandeja Paisa", "Sancocho", "Tamales", "Empanadas", "Lechona", "Chorizo"]
comidas.insert(3, "Ajiaco")  # Inserta una comida en la posición 3.
print(comidas)

# Ejercicio 34: Crear una lista con los números del 1 al 10 y utilizar el método .extend() para agregar una segunda lista con los números del 11 al 15.
numeros = list(range(1, 11))  # Lista del 1 al 10.
numeros.extend(range(11, 16))  # Agrega los números del 11 al 15.
print(numeros)
# Ejercicio 35: Crear una lista con los nombres de 6 compañeros y utilizar el método .count() para contar cuántas veces aparece un nombre específico en la lista.
compañeros = ["Juan", "María", "Luis", "Ana", "Luis", "Pedro"]
print(compañeros.count("Luis"))  # Cuenta cuántas veces aparece "Luis".

# Ejercicio 36: Crear una lista con los números del 1 al 12 y utilizar una comprensión de listas para crear una nueva lista con los números divisibles por 3.
numeros = list(range(1, 13))  # Lista del 1 al 12.
divisibles_por_3 = [x for x in numeros if x % 3 == 0]  # Filtra divisibles por 3.
print(divisibles_por_3)

# Ejercicio 37: Crear una lista con los nombres de 5 artistas musicales favoritos y utilizar el método .reverse() para invertir el orden de la lista.
artistas = ["Shakira", "Juanes", "Karol G", "Maluma", "J Balvin"]
artistas.reverse()  # Invierte el orden de la lista.
print(artistas)

# Ejercicio 38: Crear una lista con los números del 1 al 20 y utilizar una función lambda y el método .sort() para ordenar la lista de forma descendente.
numeros = list(range(1, 21))  # Lista del 1 al 20.
numeros.sort(key=lambda x: -x)  # Ordena de forma descendente usando lambda.
print(numeros)

# Ejercicio 39: Crear una lista con las materias de la universidad y utilizar el método .pop() para eliminar y obtener el último elemento de la lista.
materias = ["Matemáticas", "Física", "Programación", "Historia", "Arte"]
ultima_materia = materias.pop()  # Elimina y guarda el último elemento.
print(ultima_materia)  # Muestra la materia eliminada.
print(materias)  # Muestra la lista actualizada.

# Ejercicio 40: Crear una lista con los números del 1 al 25 y utilizar una comprensión de listas para crear una nueva lista con los números múltiplos de 5.
numeros = list(range(1, 26))  # Lista del 1 al 25.
multiplos_de_5 = [x for x in numeros if x % 5 == 0]  # Filtra múltiplos de 5.
print(multiplos_de_5)

# Ejercicio 41: Crear una lista con los nombres de 8 deportes y utilizar una función anónima y el método .sort() para ordenar la lista.
deportes = ["Fútbol", "Baloncesto", "Tenis", "Voleibol", "Natación", "Béisbol", "Atletismo", "Ciclismo"]
deportes.sort(key=lambda deporte: deporte)  # Ordena alfabéticamente usando una función lambda.
print(deportes)

# Ejercicio 42: Crear una lista con los números del 1 al 15 y utilizar el método .clear() para eliminar todos los elementos de la lista.
numeros = list(range(1, 16))  # Lista del 1 al 15.
numeros.clear()  # Elimina todos los elementos.
print(numeros)  # Muestra la lista vacía.

# Ejercicio 43: Crear una lista con los nombres de 6 países y utilizar un bucle for para imprimir cada nombre en minúsculas.
paises = ["Colombia", "Argentina", "Brasil", "Chile", "Perú", "México"]
for pais in paises:  # Recorre cada país.
    print(pais.lower())  # Imprime el nombre en minúsculas.

# Ejercicio 44: Crear una lista con los números del 1 al 20 y utilizar una comprensión de listas para crear una nueva lista con los cuadrados de los números pares.
numeros = list(range(1, 21))  # Lista del 1 al 20.
cuadrados_pares = [x**2 for x in numeros if x % 2 == 0]  # Calcula cuadrados de números pares.
print(cuadrados_pares)

# Ejercicio 45: Crear una lista con los nombres de 10 videojuegos y utilizar el método .index() para obtener el índice de un juego específico.
videojuegos = ["Minecraft", "FIFA", "Call of Duty", "Fortnite", "Valorant", "Among Us", "The Sims", "GTA V", "PUBG", "Zelda"]
print(videojuegos.index("Fortnite"))  # Obtiene el índice de "Fortnite".

# Ejercicio 46: Crear una lista con los números del 1 al 12 y utilizar el método .remove() para eliminar un número específico de la lista.
numeros = list(range(1, 13))  # Lista del 1 al 12.
numeros.remove(6)  # Elimina el número 6.
print(numeros)

# Ejercicio 47: Crear una lista con los nombres de 7 monumentos colombianos y utilizar una función lambda y el método .sort(key=len) para ordenar la lista por longitud de nombre.
monumentos = ["La Candelaria", "El Peñol", "Cristo Rey", "Monserrate", "Ciudad Perdida", "Parque Tayrona", "Santuario de Las Lajas"]
monumentos.sort(key=lambda m: len(m))  # Ordena por longitud de nombre.
print(monumentos)

# Ejercicio 48: Crear una lista con los números del 1 al 18 y utilizar una comprensión de listas para crear una nueva lista con los números múltiplos de 3 y 5.
numeros = list(range(1, 19))  # Lista del 1 al 18.
multiplos_3_5 = [x for x in numeros if x % 3 == 0 and x % 5 == 0]  # Filtra múltiplos de 3 y 5.
print(multiplos_3_5)

# Ejercicio 49: Crear una lista con los nombres de 6 asignaturas que le parecen interesantes de la carrera y utilizar el método .append() para agregar un nuevo nombre al final de la lista.
asignaturas = ["Algoritmos", "Base de Datos", "Redes", "Seguridad Informática", "Inteligencia Artificial", "Machine Learning"]
asignaturas.append("Ciencia de Datos")  # Agrega una nueva asignatura.
print(asignaturas)

# Ejercicio 50: Crear una lista con los números del 1 al 25 y utilizar el método .pop() para eliminar y obtener el elemento de la posición 7.
numeros = list(range(1, 26))  # Lista del 1 al 25.
elemento_eliminado = numeros.pop(7)  # Elimina y guarda el elemento de la posición 7.
print(elemento_eliminado)  # Muestra el elemento eliminado.
print(numeros)  # Muestra la lista actualizada.


# ===================================================================
# Título del trabajo: Seguimiento 1 PII
# Nombre: [Maria Luisa Londoño Moncada]
# Fecha de creación: Noviembre 18, 2024
# Descripción: Este archivo contiene soluciones para diversos ejercicios de manipulación de listas para seguimiento 1 PII C2
# ===================================================================

# -------------------------------------------------------------------
# solución de ejercicios
# -------------------------------------------------------------------

# Ejercicio 1: Crear una lista con los nombres de 5 frutas colombianas favoritas y mostrarla por pantalla.
frutas = ["Lulo", "Guanábana", "Mango", "Borojó", "Maracuyá"]
print(frutas)  # Muestra la lista de frutas.

# Ejercicio 2: Acceder al segundo y cuarto elemento de la lista anterior e imprimirlos.
print(frutas[1])  # Muestra el segundo elemento.
print(frutas[3])  # Muestra el cuarto elemento.

# Ejercicio 3: Crear una lista con los números del 1 al 10 y mostrar su longitud.
numeros = list(range(1, 11))  # Lista del 1 al 10.
print(len(numeros))  # Muestra la longitud de la lista.

# Ejercicio 4: Concatenar las dos listas creadas en los ejercicios 1 y 3.
concatenada = frutas + numeros  # Combina ambas listas.
print(concatenada)  # Muestra la lista concatenada.

# Ejercicio 5: Modificar el tercer elemento de la lista del ejercicio 4 al valor 100.
concatenada[2] = 100  # Cambia el tercer elemento a 100.
print(concatenada)  # Muestra la lista modificada.

# Ejercicio 6: Borrar el último elemento de la lista del ejercicio 4.
concatenada.pop()  # Elimina el último elemento.
print(concatenada)  # Muestra la lista actualizada.

# Ejercicio 7: Crear una lista con 3 números enteros y multiplicar cada elemento por 5.
enteros = [2, 4, 6]
multiplicados = [x * 5 for x in enteros]  # Multiplica cada elemento por 5.
print(multiplicados)

# Ejercicio 8: Crear dos listas con 5 números enteros cada una y multiplicar los elementos correspondientes.
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
resultado = [a * b for a, b in zip(lista1, lista2)]  # Multiplica elementos correspondientes.
print(resultado)

# Ejercicio 9: Crear una lista de listas anidadas y acceder al segundo elemento de la segunda lista.
listas_anidadas = [[1, 2], [3, 4], [5, 6]]
print(listas_anidadas[1][1])  # Accede al segundo elemento de la segunda lista.

# Ejercicio 10: Crear una lista a partir de la lista del ejercicio 3, tomando los elementos del índice 2 al 6.
sublista = numeros[2:7]  # Toma elementos de índice 2 al 6.
print(sublista)

# Ejercicio 11: Usar el método .append() para agregar un nuevo elemento al final de la lista del ejercicio 1.
frutas.append("Guayaba")  # Agrega un nuevo elemento.
print(frutas)

# Ejercicio 12: Usar el método .insert() para agregar un nuevo elemento en la posición 2 de la lista del ejercicio 3.
numeros.insert(2, 20)  # Inserta el número 20 en la posición 2.
print(numeros)

# Ejercicio 13: Usar el método .remove() para eliminar un elemento específico de la lista del ejercicio 7.
multiplicados.remove(10)  # Elimina el valor 10 si existe.
print(multiplicados)

# Ejercicio 14: Usar el método .reverse() para invertir el orden de la lista del ejercicio 4.
concatenada.reverse()  # Invierte el orden de la lista.
print(concatenada)

# Ejercicio 15: Usar el método .sort() para ordenar de forma ascendente la lista del ejercicio 7.
multiplicados.sort()  # Ordena la lista de forma ascendente.
print(multiplicados)

# Ejercicio 16: Usar el método .pop() para eliminar y obtener el último elemento de la lista del ejercicio 4.
ultimo = concatenada.pop()  # Elimina y guarda el último elemento.
print(ultimo)  # Muestra el elemento eliminado.
print(concatenada)  # Muestra la lista actualizada.

# Ejercicio 17: Usar el método .count() para contar cuántas veces aparece un elemento específico en la lista del ejercicio 7.
print(multiplicados.count(15))  # Cuenta cuántas veces aparece el valor 15.

# Ejercicio 18: Usar el método .index() para obtener el índice de un elemento específico en la lista del ejercicio 4.
# Si algún elemento existe, como "100".
print(concatenada.index(100))

# Ejercicio 19: Usar el método .clear() para eliminar todos los elementos de la lista del ejercicio 1.
frutas.clear()  # Elimina todos los elementos de la lista.
print(frutas)  # Muestra la lista vacía.

# Ejercicio 20: Crear una lista vacía y utilizar un bucle for para agregar los números del 1 al 10.
lista_vacia = []  # Crea una lista vacía.
for i in range(1, 11):  # Itera del 1 al 10.
    lista_vacia.append(i)  # Agrega cada número a la lista.
print(lista_vacia)  # Muestra la lista.

# Ejercicio 21: Crear una lista de números enteros y utilizar un bucle while para eliminar los elementos impares.
enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Lista de enteros.
i = 0  # Índice inicial.
while i < len(enteros):  # Mientras haya elementos en la lista.
    if enteros[i] % 2 != 0:  # Si el elemento es impar.
        enteros.pop(i)  # Elimina el elemento.
    else:
        i += 1  # Avanza al siguiente índice si no se elimina.
print(enteros)  # Muestra la lista sin números impares.

# Ejercicio 22: Crear una lista con los nombres de 5 materias favoritas y ordenarlas alfabéticamente.
materias = ["Matemáticas", "Física", "Historia", "Arte", "Programación"]
materias.sort()  # Ordena la lista alfabéticamente.
print(materias)

# Ejercicio 23: Crear una lista con los números del 1 al 15 y mostrar solo los múltiplos de 3.
numeros = list(range(1, 16))  # Lista del 1 al 15.
multiplos_de_3 = [x for x in numeros if x % 3 == 0]  # Filtra múltiplos de 3.
print(multiplos_de_3)

# Ejercicio 24: Crear una lista con los nombres de 10 artistas favoritos y utilizar un bucle for para imprimir cada nombre en mayúsculas.
artistas = ["Shakira", "Juanes", "Carlos Vives", "Maluma", "J Balvin", "Karol G", "Fonseca", "Silvestre Dangond", "Andrés Cepeda", "Sebastián Yatra"]
for artista in artistas:  # Recorre cada artista.
    print(artista.upper())  # Imprime el nombre en mayúsculas.

# Ejercicio 25: Crear una lista con los números del 1 al 20 y utilizar una comprensión de listas para crear una nueva lista con solo los números pares.
numeros = list(range(1, 21))  # Lista del 1 al 20.
pares = [x for x in numeros if x % 2 == 0]  # Filtra números pares.
print(pares)

# Ejercicio 26: Crear una lista con los nombres de los municipios del departamento de Arauca y utilizar un bucle for para imprimir cada nombre en orden inverso.
municipios = ["Arauca", "Arauquita", "Tame", "Saravena", "Fortul", "Cravo Norte", "Puerto Rondón"]
for municipio in municipios:  # Recorre cada municipio.
    print(municipio[::-1])  # Imprime el nombre en orden inverso.

# Ejercicio 27: Crear una lista con los números del 1 al 12 y utilizar una comprensión de listas para crear una nueva lista con los cuadrados de cada número.
numeros = list(range(1, 13))  # Lista del 1 al 12.
cuadrados = [x ** 2 for x in numeros]  # Calcula los cuadrados.
print(cuadrados)

# Ejercicio 28: Crear una lista con los meses del año y utilizar el método .index() para obtener el índice del mes "Junio".
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
print(meses.index("Junio"))  # Obtiene el índice de "Junio".

# Ejercicio 29: Crear una lista con los nombres que usted le pondría a 6 mascotas y utilizar el método .remove() para eliminar una mascota de la lista.
mascotas = ["Luna", "Max", "Bella", "Charlie", "Rocky", "Sasha"]
mascotas.remove("Max")  # Elimina "Max" de la lista.
print(mascotas)

# Ejercicio 30: Crear una lista con los números del 1 al 20 y utilizar el método .sort(reverse=True) para ordenarla de forma descendente.
numeros = list(range(1, 21))  # Lista del 1 al 20.
numeros.sort(reverse=True)  # Ordena de forma descendente.
print(numeros)

# Ejercicio 31: Crear una lista con los nombres de 4 libros favoritos y utilizar el método .append() para agregar un nuevo libro al final de la lista.
libros = ["Cien años de soledad", "Don Quijote", "1984", "El principito"]
libros.append("La Odisea")  # Agrega un nuevo libro.
print(libros)

# Ejercicio 32: Crear una lista con los números del 1 al 15 y utilizar una comprensión de listas para crear una nueva lista con los números impares.
numeros = list(range(1, 16))  # Lista del 1 al 15.
impares = [x for x in numeros if x % 2 != 0]  # Filtra números impares.
print(impares)

# Ejercicio 33: Crear una lista con los nombres de 7 comidas favoritas y utilizar el método .insert() para agregar una nueva comida en la posición 3.
comidas = ["Arepas", "Bandeja Paisa", "Sancocho", "Tamales", "Empanadas", "Lechona", "Chorizo"]
comidas.insert(3, "Ajiaco")  # Inserta una comida en la posición 3.
print(comidas)

# Ejercicio 34: Crear una lista con los números del 1 al 10 y utilizar el método .extend() para agregar una segunda lista con los números del 11 al 15.
numeros = list(range(1, 11))  # Lista del 1 al 10.
numeros.extend(range(11, 16))  # Agrega los números del 11 al 15.
print(numeros)
# Ejercicio 35: Crear una lista con los nombres de 6 compañeros y utilizar el método .count() para contar cuántas veces aparece un nombre específico en la lista.
compañeros = ["Juan", "María", "Luis", "Ana", "Luis", "Pedro"]
print(compañeros.count("Luis"))  # Cuenta cuántas veces aparece "Luis".

# Ejercicio 36: Crear una lista con los números del 1 al 12 y utilizar una comprensión de listas para crear una nueva lista con los números divisibles por 3.
numeros = list(range(1, 13))  # Lista del 1 al 12.
divisibles_por_3 = [x for x in numeros if x % 3 == 0]  # Filtra divisibles por 3.
print(divisibles_por_3)

# Ejercicio 37: Crear una lista con los nombres de 5 artistas musicales favoritos y utilizar el método .reverse() para invertir el orden de la lista.
artistas = ["Shakira", "Juanes", "Karol G", "Maluma", "J Balvin"]
artistas.reverse()  # Invierte el orden de la lista.
print(artistas)

# Ejercicio 38: Crear una lista con los números del 1 al 20 y utilizar una función lambda y el método .sort() para ordenar la lista de forma descendente.
numeros = list(range(1, 21))  # Lista del 1 al 20.
numeros.sort(key=lambda x: -x)  # Ordena de forma descendente usando lambda.
print(numeros)

# Ejercicio 39: Crear una lista con las materias de la universidad y utilizar el método .pop() para eliminar y obtener el último elemento de la lista.
materias = ["Matemáticas", "Física", "Programación", "Historia", "Arte"]
ultima_materia = materias.pop()  # Elimina y guarda el último elemento.
print(ultima_materia)  # Muestra la materia eliminada.
print(materias)  # Muestra la lista actualizada.

# Ejercicio 40: Crear una lista con los números del 1 al 25 y utilizar una comprensión de listas para crear una nueva lista con los números múltiplos de 5.
numeros = list(range(1, 26))  # Lista del 1 al 25.
multiplos_de_5 = [x for x in numeros if x % 5 == 0]  # Filtra múltiplos de 5.
print(multiplos_de_5)

# Ejercicio 41: Crear una lista con los nombres de 8 deportes y utilizar una función anónima y el método .sort() para ordenar la lista.
deportes = ["Fútbol", "Baloncesto", "Tenis", "Voleibol", "Natación", "Béisbol", "Atletismo", "Ciclismo"]
deportes.sort(key=lambda deporte: deporte)  # Ordena alfabéticamente usando una función lambda.
print(deportes)

# Ejercicio 42: Crear una lista con los números del 1 al 15 y utilizar el método .clear() para eliminar todos los elementos de la lista.
numeros = list(range(1, 16))  # Lista del 1 al 15.
numeros.clear()  # Elimina todos los elementos.
print(numeros)  # Muestra la lista vacía.

# Ejercicio 43: Crear una lista con los nombres de 6 países y utilizar un bucle for para imprimir cada nombre en minúsculas.
paises = ["Colombia", "Argentina", "Brasil", "Chile", "Perú", "México"]
for pais in paises:  # Recorre cada país.
    print(pais.lower())  # Imprime el nombre en minúsculas.

# Ejercicio 44: Crear una lista con los números del 1 al 20 y utilizar una comprensión de listas para crear una nueva lista con los cuadrados de los números pares.
numeros = list(range(1, 21))  # Lista del 1 al 20.
cuadrados_pares = [x**2 for x in numeros if x % 2 == 0]  # Calcula cuadrados de números pares.
print(cuadrados_pares)

# Ejercicio 45: Crear una lista con los nombres de 10 videojuegos y utilizar el método .index() para obtener el índice de un juego específico.
videojuegos = ["Minecraft", "FIFA", "Call of Duty", "Fortnite", "Valorant", "Among Us", "The Sims", "GTA V", "PUBG", "Zelda"]
print(videojuegos.index("Fortnite"))  # Obtiene el índice de "Fortnite".

# Ejercicio 46: Crear una lista con los números del 1 al 12 y utilizar el método .remove() para eliminar un número específico de la lista.
numeros = list(range(1, 13))  # Lista del 1 al 12.
numeros.remove(6)  # Elimina el número 6.
print(numeros)

# Ejercicio 47: Crear una lista con los nombres de 7 monumentos colombianos y utilizar una función lambda y el método .sort(key=len) para ordenar la lista por longitud de nombre.
monumentos = ["La Candelaria", "El Peñol", "Cristo Rey", "Monserrate", "Ciudad Perdida", "Parque Tayrona", "Santuario de Las Lajas"]
monumentos.sort(key=lambda m: len(m))  # Ordena por longitud de nombre.
print(monumentos)

# Ejercicio 48: Crear una lista con los números del 1 al 18 y utilizar una comprensión de listas para crear una nueva lista con los números múltiplos de 3 y 5.
numeros = list(range(1, 19))  # Lista del 1 al 18.
multiplos_3_5 = [x for x in numeros if x % 3 == 0 and x % 5 == 0]  # Filtra múltiplos de 3 y 5.
print(multiplos_3_5)

# Ejercicio 49: Crear una lista con los nombres de 6 asignaturas que le parecen interesantes de la carrera y utilizar el método .append() para agregar un nuevo nombre al final de la lista.
asignaturas = ["Algoritmos", "Base de Datos", "Redes", "Seguridad Informática", "Inteligencia Artificial", "Machine Learning"]
asignaturas.append("Ciencia de Datos")  # Agrega una nueva asignatura.
print(asignaturas)

# Ejercicio 50: Crear una lista con los números del 1 al 25 y utilizar el método .pop() para eliminar y obtener el elemento de la posición 7.
numeros = list(range(1, 26))  # Lista del 1 al 25.
elemento_eliminado = numeros.pop(7)  # Elimina y guarda el elemento de la posición 7.
print(elemento_eliminado)  # Muestra el elemento eliminado.
print(numeros)  # Muestra la lista actualizada.


# ===================================================================
# Título del trabajo: Seguimiento 1 PII
# Nombre: [Maria Luisa Londoño Moncada]
# Fecha de creación: Noviembre 18, 2024
# Descripción: Este archivo contiene soluciones para diversos ejercicios de manipulación de listas para seguimiento 1 PII C2
# ===================================================================

# -------------------------------------------------------------------
# solución de ejercicios
# -------------------------------------------------------------------

# Ejercicio 1: Crear una lista con los nombres de 5 frutas colombianas favoritas y mostrarla por pantalla.
frutas = ["Lulo", "Guanábana", "Mango", "Borojó", "Maracuyá"]
print(frutas)  # Muestra la lista de frutas.

# Ejercicio 2: Acceder al segundo y cuarto elemento de la lista anterior e imprimirlos.
print(frutas[1])  # Muestra el segundo elemento.
print(frutas[3])  # Muestra el cuarto elemento.

# Ejercicio 3: Crear una lista con los números del 1 al 10 y mostrar su longitud.
numeros = list(range(1, 11))  # Lista del 1 al 10.
print(len(numeros))  # Muestra la longitud de la lista.

# Ejercicio 4: Concatenar las dos listas creadas en los ejercicios 1 y 3.
concatenada = frutas + numeros  # Combina ambas listas.
print(concatenada)  # Muestra la lista concatenada.

# Ejercicio 5: Modificar el tercer elemento de la lista del ejercicio 4 al valor 100.
concatenada[2] = 100  # Cambia el tercer elemento a 100.
print(concatenada)  # Muestra la lista modificada.

# Ejercicio 6: Borrar el último elemento de la lista del ejercicio 4.
concatenada.pop()  # Elimina el último elemento.
print(concatenada)  # Muestra la lista actualizada.

# Ejercicio 7: Crear una lista con 3 números enteros y multiplicar cada elemento por 5.
enteros = [2, 4, 6]
multiplicados = [x * 5 for x in enteros]  # Multiplica cada elemento por 5.
print(multiplicados)

# Ejercicio 8: Crear dos listas con 5 números enteros cada una y multiplicar los elementos correspondientes.
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
resultado = [a * b for a, b in zip(lista1, lista2)]  # Multiplica elementos correspondientes.
print(resultado)

# Ejercicio 9: Crear una lista de listas anidadas y acceder al segundo elemento de la segunda lista.
listas_anidadas = [[1, 2], [3, 4], [5, 6]]
print(listas_anidadas[1][1])  # Accede al segundo elemento de la segunda lista.

# Ejercicio 10: Crear una lista a partir de la lista del ejercicio 3, tomando los elementos del índice 2 al 6.
sublista = numeros[2:7]  # Toma elementos de índice 2 al 6.
print(sublista)

# Ejercicio 11: Usar el método .append() para agregar un nuevo elemento al final de la lista del ejercicio 1.
frutas.append("Guayaba")  # Agrega un nuevo elemento.
print(frutas)

# Ejercicio 12: Usar el método .insert() para agregar un nuevo elemento en la posición 2 de la lista del ejercicio 3.
numeros.insert(2, 20)  # Inserta el número 20 en la posición 2.
print(numeros)

# Ejercicio 13: Usar el método .remove() para eliminar un elemento específico de la lista del ejercicio 7.
multiplicados.remove(10)  # Elimina el valor 10 si existe.
print(multiplicados)

# Ejercicio 14: Usar el método .reverse() para invertir el orden de la lista del ejercicio 4.
concatenada.reverse()  # Invierte el orden de la lista.
print(concatenada)

# Ejercicio 15: Usar el método .sort() para ordenar de forma ascendente la lista del ejercicio 7.
multiplicados.sort()  # Ordena la lista de forma ascendente.
print(multiplicados)

# Ejercicio 16: Usar el método .pop() para eliminar y obtener el último elemento de la lista del ejercicio 4.
ultimo = concatenada.pop()  # Elimina y guarda el último elemento.
print(ultimo)  # Muestra el elemento eliminado.
print(concatenada)  # Muestra la lista actualizada.

# Ejercicio 17: Usar el método .count() para contar cuántas veces aparece un elemento específico en la lista del ejercicio 7.
print(multiplicados.count(15))  # Cuenta cuántas veces aparece el valor 15.

# Ejercicio 18: Usar el método .index() para obtener el índice de un elemento específico en la lista del ejercicio 4.
# Si algún elemento existe, como "100".
print(concatenada.index(100))

# Ejercicio 19: Usar el método .clear() para eliminar todos los elementos de la lista del ejercicio 1.
frutas.clear()  # Elimina todos los elementos de la lista.
print(frutas)  # Muestra la lista vacía.

# Ejercicio 20: Crear una lista vacía y utilizar un bucle for para agregar los números del 1 al 10.
lista_vacia = []  # Crea una lista vacía.
for i in range(1, 11):  # Itera del 1 al 10.
    lista_vacia.append(i)  # Agrega cada número a la lista.
print(lista_vacia)  # Muestra la lista.

# Ejercicio 21: Crear una lista de números enteros y utilizar un bucle while para eliminar los elementos impares.
enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Lista de enteros.
i = 0  # Índice inicial.
while i < len(enteros):  # Mientras haya elementos en la lista.
    if enteros[i] % 2 != 0:  # Si el elemento es impar.
        enteros.pop(i)  # Elimina el elemento.
    else:
        i += 1  # Avanza al siguiente índice si no se elimina.
print(enteros)  # Muestra la lista sin números impares.

# Ejercicio 22: Crear una lista con los nombres de 5 materias favoritas y ordenarlas alfabéticamente.
materias = ["Matemáticas", "Física", "Historia", "Arte", "Programación"]
materias.sort()  # Ordena la lista alfabéticamente.
print(materias)

# Ejercicio 23: Crear una lista con los números del 1 al 15 y mostrar solo los múltiplos de 3.
numeros = list(range(1, 16))  # Lista del 1 al 15.
multiplos_de_3 = [x for x in numeros if x % 3 == 0]  # Filtra múltiplos de 3.
print(multiplos_de_3)

# Ejercicio 24: Crear una lista con los nombres de 10 artistas favoritos y utilizar un bucle for para imprimir cada nombre en mayúsculas.
artistas = ["Shakira", "Juanes", "Carlos Vives", "Maluma", "J Balvin", "Karol G", "Fonseca", "Silvestre Dangond", "Andrés Cepeda", "Sebastián Yatra"]
for artista in artistas:  # Recorre cada artista.
    print(artista.upper())  # Imprime el nombre en mayúsculas.

# Ejercicio 25: Crear una lista con los números del 1 al 20 y utilizar una comprensión de listas para crear una nueva lista con solo los números pares.
numeros = list(range(1, 21))  # Lista del 1 al 20.
pares = [x for x in numeros if x % 2 == 0]  # Filtra números pares.
print(pares)

# Ejercicio 26: Crear una lista con los nombres de los municipios del departamento de Arauca y utilizar un bucle for para imprimir cada nombre en orden inverso.
municipios = ["Arauca", "Arauquita", "Tame", "Saravena", "Fortul", "Cravo Norte", "Puerto Rondón"]
for municipio in municipios:  # Recorre cada municipio.
    print(municipio[::-1])  # Imprime el nombre en orden inverso.

# Ejercicio 27: Crear una lista con los números del 1 al 12 y utilizar una comprensión de listas para crear una nueva lista con los cuadrados de cada número.
numeros = list(range(1, 13))  # Lista del 1 al 12.
cuadrados = [x ** 2 for x in numeros]  # Calcula los cuadrados.
print(cuadrados)

# Ejercicio 28: Crear una lista con los meses del año y utilizar el método .index() para obtener el índice del mes "Junio".
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
print(meses.index("Junio"))  # Obtiene el índice de "Junio".

# Ejercicio 29: Crear una lista con los nombres que usted le pondría a 6 mascotas y utilizar el método .remove() para eliminar una mascota de la lista.
mascotas = ["Luna", "Max", "Bella", "Charlie", "Rocky", "Sasha"]
mascotas.remove("Max")  # Elimina "Max" de la lista.
print(mascotas)

# Ejercicio 30: Crear una lista con los números del 1 al 20 y utilizar el método .sort(reverse=True) para ordenarla de forma descendente.
numeros = list(range(1, 21))  # Lista del 1 al 20.
numeros.sort(reverse=True)  # Ordena de forma descendente.
print(numeros)

# Ejercicio 31: Crear una lista con los nombres de 4 libros favoritos y utilizar el método .append() para agregar un nuevo libro al final de la lista.
libros = ["Cien años de soledad", "Don Quijote", "1984", "El principito"]
libros.append("La Odisea")  # Agrega un nuevo libro.
print(libros)

# Ejercicio 32: Crear una lista con los números del 1 al 15 y utilizar una comprensión de listas para crear una nueva lista con los números impares.
numeros = list(range(1, 16))  # Lista del 1 al 15.
impares = [x for x in numeros if x % 2 != 0]  # Filtra números impares.
print(impares)

# Ejercicio 33: Crear una lista con los nombres de 7 comidas favoritas y utilizar el método .insert() para agregar una nueva comida en la posición 3.
comidas = ["Arepas", "Bandeja Paisa", "Sancocho", "Tamales", "Empanadas", "Lechona", "Chorizo"]
comidas.insert(3, "Ajiaco")  # Inserta una comida en la posición 3.
print(comidas)

# Ejercicio 34: Crear una lista con los números del 1 al 10 y utilizar el método .extend() para agregar una segunda lista con los números del 11 al 15.
numeros = list(range(1, 11))  # Lista del 1 al 10.
numeros.extend(range(11, 16))  # Agrega los números del 11 al 15.
print(numeros)
# Ejercicio 35: Crear una lista con los nombres de 6 compañeros y utilizar el método .count() para contar cuántas veces aparece un nombre específico en la lista.
compañeros = ["Juan", "María", "Luis", "Ana", "Luis", "Pedro"]
print(compañeros.count("Luis"))  # Cuenta cuántas veces aparece "Luis".

# Ejercicio 36: Crear una lista con los números del 1 al 12 y utilizar una comprensión de listas para crear una nueva lista con los números divisibles por 3.
numeros = list(range(1, 13))  # Lista del 1 al 12.
divisibles_por_3 = [x for x in numeros if x % 3 == 0]  # Filtra divisibles por 3.
print(divisibles_por_3)

# Ejercicio 37: Crear una lista con los nombres de 5 artistas musicales favoritos y utilizar el método .reverse() para invertir el orden de la lista.
artistas = ["Shakira", "Juanes", "Karol G", "Maluma", "J Balvin"]
artistas.reverse()  # Invierte el orden de la lista.
print(artistas)

# Ejercicio 38: Crear una lista con los números del 1 al 20 y utilizar una función lambda y el método .sort() para ordenar la lista de forma descendente.
numeros = list(range(1, 21))  # Lista del 1 al 20.
numeros.sort(key=lambda x: -x)  # Ordena de forma descendente usando lambda.
print(numeros)

# Ejercicio 39: Crear una lista con las materias de la universidad y utilizar el método .pop() para eliminar y obtener el último elemento de la lista.
materias = ["Matemáticas", "Física", "Programación", "Historia", "Arte"]
ultima_materia = materias.pop()  # Elimina y guarda el último elemento.
print(ultima_materia)  # Muestra la materia eliminada.
print(materias)  # Muestra la lista actualizada.

# Ejercicio 40: Crear una lista con los números del 1 al 25 y utilizar una comprensión de listas para crear una nueva lista con los números múltiplos de 5.
numeros = list(range(1, 26))  # Lista del 1 al 25.
multiplos_de_5 = [x for x in numeros if x % 5 == 0]  # Filtra múltiplos de 5.
print(multiplos_de_5)

# Ejercicio 41: Crear una lista con los nombres de 8 deportes y utilizar una función anónima y el método .sort() para ordenar la lista.
deportes = ["Fútbol", "Baloncesto", "Tenis", "Voleibol", "Natación", "Béisbol", "Atletismo", "Ciclismo"]
deportes.sort(key=lambda deporte: deporte)  # Ordena alfabéticamente usando una función lambda.
print(deportes)

# Ejercicio 42: Crear una lista con los números del 1 al 15 y utilizar el método .clear() para eliminar todos los elementos de la lista.
numeros = list(range(1, 16))  # Lista del 1 al 15.
numeros.clear()  # Elimina todos los elementos.
print(numeros)  # Muestra la lista vacía.

# Ejercicio 43: Crear una lista con los nombres de 6 países y utilizar un bucle for para imprimir cada nombre en minúsculas.
paises = ["Colombia", "Argentina", "Brasil", "Chile", "Perú", "México"]
for pais in paises:  # Recorre cada país.
    print(pais.lower())  # Imprime el nombre en minúsculas.

# Ejercicio 44: Crear una lista con los números del 1 al 20 y utilizar una comprensión de listas para crear una nueva lista con los cuadrados de los números pares.
numeros = list(range(1, 21))  # Lista del 1 al 20.
cuadrados_pares = [x**2 for x in numeros if x % 2 == 0]  # Calcula cuadrados de números pares.
print(cuadrados_pares)

# Ejercicio 45: Crear una lista con los nombres de 10 videojuegos y utilizar el método .index() para obtener el índice de un juego específico.
videojuegos = ["Minecraft", "FIFA", "Call of Duty", "Fortnite", "Valorant", "Among Us", "The Sims", "GTA V", "PUBG", "Zelda"]
print(videojuegos.index("Fortnite"))  # Obtiene el índice de "Fortnite".

# Ejercicio 46: Crear una lista con los números del 1 al 12 y utilizar el método .remove() para eliminar un número específico de la lista.
numeros = list(range(1, 13))  # Lista del 1 al 12.
numeros.remove(6)  # Elimina el número 6.
print(numeros)

# Ejercicio 47: Crear una lista con los nombres de 7 monumentos colombianos y utilizar una función lambda y el método .sort(key=len) para ordenar la lista por longitud de nombre.
monumentos = ["La Candelaria", "El Peñol", "Cristo Rey", "Monserrate", "Ciudad Perdida", "Parque Tayrona", "Santuario de Las Lajas"]
monumentos.sort(key=lambda m: len(m))  # Ordena por longitud de nombre.
print(monumentos)

# Ejercicio 48: Crear una lista con los números del 1 al 18 y utilizar una comprensión de listas para crear una nueva lista con los números múltiplos de 3 y 5.
numeros = list(range(1, 19))  # Lista del 1 al 18.
multiplos_3_5 = [x for x in numeros if x % 3 == 0 and x % 5 == 0]  # Filtra múltiplos de 3 y 5.
print(multiplos_3_5)

# Ejercicio 49: Crear una lista con los nombres de 6 asignaturas que le parecen interesantes de la carrera y utilizar el método .append() para agregar un nuevo nombre al final de la lista.
asignaturas = ["Algoritmos", "Base de Datos", "Redes", "Seguridad Informática", "Inteligencia Artificial", "Machine Learning"]
asignaturas.append("Ciencia de Datos")  # Agrega una nueva asignatura.
print(asignaturas)

# Ejercicio 50: Crear una lista con los números del 1 al 25 y utilizar el método .pop() para eliminar y obtener el elemento de la posición 7.
numeros = list(range(1, 26))  # Lista del 1 al 25.
elemento_eliminado = numeros.pop(7)  # Elimina y guarda el elemento de la posición 7.
print(elemento_eliminado)  # Muestra el elemento eliminado.
print(numeros)  # Muestra la lista actualizada.


# ===================================================================
# Título del trabajo: Seguimiento 1 PII
# Nombre: [Maria Luisa Londoño Moncada]
# Fecha de creación: Noviembre 18, 2024
# Descripción: Este archivo contiene soluciones para diversos ejercicios de manipulación de listas para seguimiento 1 PII C2
# ===================================================================

# -------------------------------------------------------------------
# solución de ejercicios
# -------------------------------------------------------------------

# Ejercicio 1: Crear una lista con los nombres de 5 frutas colombianas favoritas y mostrarla por pantalla.
frutas = ["Lulo", "Guanábana", "Mango", "Borojó", "Maracuyá"]
print(frutas)  # Muestra la lista de frutas.

# Ejercicio 2: Acceder al segundo y cuarto elemento de la lista anterior e imprimirlos.
print(frutas[1])  # Muestra el segundo elemento.
print(frutas[3])  # Muestra el cuarto elemento.

# Ejercicio 3: Crear una lista con los números del 1 al 10 y mostrar su longitud.
numeros = list(range(1, 11))  # Lista del 1 al 10.
print(len(numeros))  # Muestra la longitud de la lista.

# Ejercicio 4: Concatenar las dos listas creadas en los ejercicios 1 y 3.
concatenada = frutas + numeros  # Combina ambas listas.
print(concatenada)  # Muestra la lista concatenada.

# Ejercicio 5: Modificar el tercer elemento de la lista del ejercicio 4 al valor 100.
concatenada[2] = 100  # Cambia el tercer elemento a 100.
print(concatenada)  # Muestra la lista modificada.

# Ejercicio 6: Borrar el último elemento de la lista del ejercicio 4.
concatenada.pop()  # Elimina el último elemento.
print(concatenada)  # Muestra la lista actualizada.

# Ejercicio 7: Crear una lista con 3 números enteros y multiplicar cada elemento por 5.
enteros = [2, 4, 6]
multiplicados = [x * 5 for x in enteros]  # Multiplica cada elemento por 5.
print(multiplicados)

# Ejercicio 8: Crear dos listas con 5 números enteros cada una y multiplicar los elementos correspondientes.
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
resultado = [a * b for a, b in zip(lista1, lista2)]  # Multiplica elementos correspondientes.
print(resultado)

# Ejercicio 9: Crear una lista de listas anidadas y acceder al segundo elemento de la segunda lista.
listas_anidadas = [[1, 2], [3, 4], [5, 6]]
print(listas_anidadas[1][1])  # Accede al segundo elemento de la segunda lista.

# Ejercicio 10: Crear una lista a partir de la lista del ejercicio 3, tomando los elementos del índice 2 al 6.
sublista = numeros[2:7]  # Toma elementos de índice 2 al 6.
print(sublista)

# Ejercicio 11: Usar el método .append() para agregar un nuevo elemento al final de la lista del ejercicio 1.
frutas.append("Guayaba")  # Agrega un nuevo elemento.
print(frutas)

# Ejercicio 12: Usar el método .insert() para agregar un nuevo elemento en la posición 2 de la lista del ejercicio 3.
numeros.insert(2, 20)  # Inserta el número 20 en la posición 2.
print(numeros)

# Ejercicio 13: Usar el método .remove() para eliminar un elemento específico de la lista del ejercicio 7.
multiplicados.remove(10)  # Elimina el valor 10 si existe.
print(multiplicados)

# Ejercicio 14: Usar el método .reverse() para invertir el orden de la lista del ejercicio 4.
concatenada.reverse()  # Invierte el orden de la lista.
print(concatenada)

# Ejercicio 15: Usar el método .sort() para ordenar de forma ascendente la lista del ejercicio 7.
multiplicados.sort()  # Ordena la lista de forma ascendente.
print(multiplicados)

# Ejercicio 16: Usar el método .pop() para eliminar y obtener el último elemento de la lista del ejercicio 4.
ultimo = concatenada.pop()  # Elimina y guarda el último elemento.
print(ultimo)  # Muestra el elemento eliminado.
print(concatenada)  # Muestra la lista actualizada.

# Ejercicio 17: Usar el método .count() para contar cuántas veces aparece un elemento específico en la lista del ejercicio 7.
print(multiplicados.count(15))  # Cuenta cuántas veces aparece el valor 15.

# Ejercicio 18: Usar el método .index() para obtener el índice de un elemento específico en la lista del ejercicio 4.
# Si algún elemento existe, como "100".
print(concatenada.index(100))

# Ejercicio 19: Usar el método .clear() para eliminar todos los elementos de la lista del ejercicio 1.
frutas.clear()  # Elimina todos los elementos de la lista.
print(frutas)  # Muestra la lista vacía.

# Ejercicio 20: Crear una lista vacía y utilizar un bucle for para agregar los números del 1 al 10.
lista_vacia = []  # Crea una lista vacía.
for i in range(1, 11):  # Itera del 1 al 10.
    lista_vacia.append(i)  # Agrega cada número a la lista.
print(lista_vacia)  # Muestra la lista.

# Ejercicio 21: Crear una lista de números enteros y utilizar un bucle while para eliminar los elementos impares.
enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Lista de enteros.
i = 0  # Índice inicial.
while i < len(enteros):  # Mientras haya elementos en la lista.
    if enteros[i] % 2 != 0:  # Si el elemento es impar.
        enteros.pop(i)  # Elimina el elemento.
    else:
        i += 1  # Avanza al siguiente índice si no se elimina.
print(enteros)  # Muestra la lista sin números impares.

# Ejercicio 22: Crear una lista con los nombres de 5 materias favoritas y ordenarlas alfabéticamente.
materias = ["Matemáticas", "Física", "Historia", "Arte", "Programación"]
materias.sort()  # Ordena la lista alfabéticamente.
print(materias)

# Ejercicio 23: Crear una lista con los números del 1 al 15 y mostrar solo los múltiplos de 3.
numeros = list(range(1, 16))  # Lista del 1 al 15.
multiplos_de_3 = [x for x in numeros if x % 3 == 0]  # Filtra múltiplos de 3.
print(multiplos_de_3)

# Ejercicio 24: Crear una lista con los nombres de 10 artistas favoritos y utilizar un bucle for para imprimir cada nombre en mayúsculas.
artistas = ["Shakira", "Juanes", "Carlos Vives", "Maluma", "J Balvin", "Karol G", "Fonseca", "Silvestre Dangond", "Andrés Cepeda", "Sebastián Yatra"]
for artista in artistas:  # Recorre cada artista.
    print(artista.upper())  # Imprime el nombre en mayúsculas.

# Ejercicio 25: Crear una lista con los números del 1 al 20 y utilizar una comprensión de listas para crear una nueva lista con solo los números pares.
numeros = list(range(1, 21))  # Lista del 1 al 20.
pares = [x for x in numeros if x % 2 == 0]  # Filtra números pares.
print(pares)

# Ejercicio 26: Crear una lista con los nombres de los municipios del departamento de Arauca y utilizar un bucle for para imprimir cada nombre en orden inverso.
municipios = ["Arauca", "Arauquita", "Tame", "Saravena", "Fortul", "Cravo Norte", "Puerto Rondón"]
for municipio in municipios:  # Recorre cada municipio.
    print(municipio[::-1])  # Imprime el nombre en orden inverso.

# Ejercicio 27: Crear una lista con los números del 1 al 12 y utilizar una comprensión de listas para crear una nueva lista con los cuadrados de cada número.
numeros = list(range(1, 13))  # Lista del 1 al 12.
cuadrados = [x ** 2 for x in numeros]  # Calcula los cuadrados.
print(cuadrados)

# Ejercicio 28: Crear una lista con los meses del año y utilizar el método .index() para obtener el índice del mes "Junio".
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
print(meses.index("Junio"))  # Obtiene el índice de "Junio".

# Ejercicio 29: Crear una lista con los nombres que usted le pondría a 6 mascotas y utilizar el método .remove() para eliminar una mascota de la lista.
mascotas = ["Luna", "Max", "Bella", "Charlie", "Rocky", "Sasha"]
mascotas.remove("Max")  # Elimina "Max" de la lista.
print(mascotas)

# Ejercicio 30: Crear una lista con los números del 1 al 20 y utilizar el método .sort(reverse=True) para ordenarla de forma descendente.
numeros = list(range(1, 21))  # Lista del 1 al 20.
numeros.sort(reverse=True)  # Ordena de forma descendente.
print(numeros)

# Ejercicio 31: Crear una lista con los nombres de 4 libros favoritos y utilizar el método .append() para agregar un nuevo libro al final de la lista.
libros = ["Cien años de soledad", "Don Quijote", "1984", "El principito"]
libros.append("La Odisea")  # Agrega un nuevo libro.
print(libros)

# Ejercicio 32: Crear una lista con los números del 1 al 15 y utilizar una comprensión de listas para crear una nueva lista con los números impares.
numeros = list(range(1, 16))  # Lista del 1 al 15.
impares = [x for x in numeros if x % 2 != 0]  # Filtra números impares.
print(impares)

# Ejercicio 33: Crear una lista con los nombres de 7 comidas favoritas y utilizar el método .insert() para agregar una nueva comida en la posición 3.
comidas = ["Arepas", "Bandeja Paisa", "Sancocho", "Tamales", "Empanadas", "Lechona", "Chorizo"]
comidas.insert(3, "Ajiaco")  # Inserta una comida en la posición 3.
print(comidas)

# Ejercicio 34: Crear una lista con los números del 1 al 10 y utilizar el método .extend() para agregar una segunda lista con los números del 11 al 15.
numeros = list(range(1, 11))  # Lista del 1 al 10.
numeros.extend(range(11, 16))  # Agrega los números del 11 al 15.
print(numeros)
# Ejercicio 35: Crear una lista con los nombres de 6 compañeros y utilizar el método .count() para contar cuántas veces aparece un nombre específico en la lista.
compañeros = ["Juan", "María", "Luis", "Ana", "Luis", "Pedro"]
print(compañeros.count("Luis"))  # Cuenta cuántas veces aparece "Luis".

# Ejercicio 36: Crear una lista con los números del 1 al 12 y utilizar una comprensión de listas para crear una nueva lista con los números divisibles por 3.
numeros = list(range(1, 13))  # Lista del 1 al 12.
divisibles_por_3 = [x for x in numeros if x % 3 == 0]  # Filtra divisibles por 3.
print(divisibles_por_3)

# Ejercicio 37: Crear una lista con los nombres de 5 artistas musicales favoritos y utilizar el método .reverse() para invertir el orden de la lista.
artistas = ["Shakira", "Juanes", "Karol G", "Maluma", "J Balvin"]
artistas.reverse()  # Invierte el orden de la lista.
print(artistas)

# Ejercicio 38: Crear una lista con los números del 1 al 20 y utilizar una función lambda y el método .sort() para ordenar la lista de forma descendente.
numeros = list(range(1, 21))  # Lista del 1 al 20.
numeros.sort(key=lambda x: -x)  # Ordena de forma descendente usando lambda.
print(numeros)

# Ejercicio 39: Crear una lista con las materias de la universidad y utilizar el método .pop() para eliminar y obtener el último elemento de la lista.
materias = ["Matemáticas", "Física", "Programación", "Historia", "Arte"]
ultima_materia = materias.pop()  # Elimina y guarda el último elemento.
print(ultima_materia)  # Muestra la materia eliminada.
print(materias)  # Muestra la lista actualizada.

# Ejercicio 40: Crear una lista con los números del 1 al 25 y utilizar una comprensión de listas para crear una nueva lista con los números múltiplos de 5.
numeros = list(range(1, 26))  # Lista del 1 al 25.
multiplos_de_5 = [x for x in numeros if x % 5 == 0]  # Filtra múltiplos de 5.
print(multiplos_de_5)

# Ejercicio 41: Crear una lista con los nombres de 8 deportes y utilizar una función anónima y el método .sort() para ordenar la lista.
deportes = ["Fútbol", "Baloncesto", "Tenis", "Voleibol", "Natación", "Béisbol", "Atletismo", "Ciclismo"]
deportes.sort(key=lambda deporte: deporte)  # Ordena alfabéticamente usando una función lambda.
print(deportes)

# Ejercicio 42: Crear una lista con los números del 1 al 15 y utilizar el método .clear() para eliminar todos los elementos de la lista.
numeros = list(range(1, 16))  # Lista del 1 al 15.
numeros.clear()  # Elimina todos los elementos.
print(numeros)  # Muestra la lista vacía.

# Ejercicio 43: Crear una lista con los nombres de 6 países y utilizar un bucle for para imprimir cada nombre en minúsculas.
paises = ["Colombia", "Argentina", "Brasil", "Chile", "Perú", "México"]
for pais in paises:  # Recorre cada país.
    print(pais.lower())  # Imprime el nombre en minúsculas.

# Ejercicio 44: Crear una lista con los números del 1 al 20 y utilizar una comprensión de listas para crear una nueva lista con los cuadrados de los números pares.
numeros = list(range(1, 21))  # Lista del 1 al 20.
cuadrados_pares = [x**2 for x in numeros if x % 2 == 0]  # Calcula cuadrados de números pares.
print(cuadrados_pares)

# Ejercicio 45: Crear una lista con los nombres de 10 videojuegos y utilizar el método .index() para obtener el índice de un juego específico.
videojuegos = ["Minecraft", "FIFA", "Call of Duty", "Fortnite", "Valorant", "Among Us", "The Sims", "GTA V", "PUBG", "Zelda"]
print(videojuegos.index("Fortnite"))  # Obtiene el índice de "Fortnite".

# Ejercicio 46: Crear una lista con los números del 1 al 12 y utilizar el método .remove() para eliminar un número específico de la lista.
numeros = list(range(1, 13))  # Lista del 1 al 12.
numeros.remove(6)  # Elimina el número 6.
print(numeros)

# Ejercicio 47: Crear una lista con los nombres de 7 monumentos colombianos y utilizar una función lambda y el método .sort(key=len) para ordenar la lista por longitud de nombre.
monumentos = ["La Candelaria", "El Peñol", "Cristo Rey", "Monserrate", "Ciudad Perdida", "Parque Tayrona", "Santuario de Las Lajas"]
monumentos.sort(key=lambda m: len(m))  # Ordena por longitud de nombre.
print(monumentos)

# Ejercicio 48: Crear una lista con los números del 1 al 18 y utilizar una comprensión de listas para crear una nueva lista con los números múltiplos de 3 y 5.
numeros = list(range(1, 19))  # Lista del 1 al 18.
multiplos_3_5 = [x for x in numeros if x % 3 == 0 and x % 5 == 0]  # Filtra múltiplos de 3 y 5.
print(multiplos_3_5)

# Ejercicio 49: Crear una lista con los nombres de 6 asignaturas que le parecen interesantes de la carrera y utilizar el método .append() para agregar un nuevo nombre al final de la lista.
asignaturas = ["Algoritmos", "Base de Datos", "Redes", "Seguridad Informática", "Inteligencia Artificial", "Machine Learning"]
asignaturas.append("Ciencia de Datos")  # Agrega una nueva asignatura.
print(asignaturas)

# Ejercicio 50: Crear una lista con los números del 1 al 25 y utilizar el método .pop() para eliminar y obtener el elemento de la posición 7.
numeros = list(range(1, 26))  # Lista del 1 al 25.
elemento_eliminado = numeros.pop(7)  # Elimina y guarda el elemento de la posición 7.
print(elemento_eliminado)  # Muestra el elemento eliminado.
print(numeros)  # Muestra la lista actualizada.


# ===================================================================
# Título del trabajo: Seguimiento 1 PII
# Nombre: [Maria Luisa Londoño Moncada]
# Fecha de creación: Noviembre 18, 2024
# Descripción: Este archivo contiene soluciones para diversos ejercicios de manipulación de listas para seguimiento 1 PII C2
# ===================================================================

# -------------------------------------------------------------------
# solución de ejercicios
# -------------------------------------------------------------------

# Ejercicio 1: Crear una lista con los nombres de 5 frutas colombianas favoritas y mostrarla por pantalla.
frutas = ["Lulo", "Guanábana", "Mango", "Borojó", "Maracuyá"]
print(frutas)  # Muestra la lista de frutas.

# Ejercicio 2: Acceder al segundo y cuarto elemento de la lista anterior e imprimirlos.
print(frutas[1])  # Muestra el segundo elemento.
print(frutas[3])  # Muestra el cuarto elemento.

# Ejercicio 3: Crear una lista con los números del 1 al 10 y mostrar su longitud.
numeros = list(range(1, 11))  # Lista del 1 al 10.
print(len(numeros))  # Muestra la longitud de la lista.

# Ejercicio 4: Concatenar las dos listas creadas en los ejercicios 1 y 3.
concatenada = frutas + numeros  # Combina ambas listas.
print(concatenada)  # Muestra la lista concatenada.

# Ejercicio 5: Modificar el tercer elemento de la lista del ejercicio 4 al valor 100.
concatenada[2] = 100  # Cambia el tercer elemento a 100.
print(concatenada)  # Muestra la lista modificada.

# Ejercicio 6: Borrar el último elemento de la lista del ejercicio 4.
concatenada.pop()  # Elimina el último elemento.
print(concatenada)  # Muestra la lista actualizada.

# Ejercicio 7: Crear una lista con 3 números enteros y multiplicar cada elemento por 5.
enteros = [2, 4, 6]
multiplicados = [x * 5 for x in enteros]  # Multiplica cada elemento por 5.
print(multiplicados)

# Ejercicio 8: Crear dos listas con 5 números enteros cada una y multiplicar los elementos correspondientes.
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
resultado = [a * b for a, b in zip(lista1, lista2)]  # Multiplica elementos correspondientes.
print(resultado)

# Ejercicio 9: Crear una lista de listas anidadas y acceder al segundo elemento de la segunda lista.
listas_anidadas = [[1, 2], [3, 4], [5, 6]]
print(listas_anidadas[1][1])  # Accede al segundo elemento de la segunda lista.

# Ejercicio 10: Crear una lista a partir de la lista del ejercicio 3, tomando los elementos del índice 2 al 6.
sublista = numeros[2:7]  # Toma elementos de índice 2 al 6.
print(sublista)

# Ejercicio 11: Usar el método .append() para agregar un nuevo elemento al final de la lista del ejercicio 1.
frutas.append("Guayaba")  # Agrega un nuevo elemento.
print(frutas)

# Ejercicio 12: Usar el método .insert() para agregar un nuevo elemento en la posición 2 de la lista del ejercicio 3.
numeros.insert(2, 20)  # Inserta el número 20 en la posición 2.
print(numeros)

# Ejercicio 13: Usar el método .remove() para eliminar un elemento específico de la lista del ejercicio 7.
multiplicados.remove(10)  # Elimina el valor 10 si existe.
print(multiplicados)

# Ejercicio 14: Usar el método .reverse() para invertir el orden de la lista del ejercicio 4.
concatenada.reverse()  # Invierte el orden de la lista.
print(concatenada)

# Ejercicio 15: Usar el método .sort() para ordenar de forma ascendente la lista del ejercicio 7.
multiplicados.sort()  # Ordena la lista de forma ascendente.
print(multiplicados)

# Ejercicio 16: Usar el método .pop() para eliminar y obtener el último elemento de la lista del ejercicio 4.
ultimo = concatenada.pop()  # Elimina y guarda el último elemento.
print(ultimo)  # Muestra el elemento eliminado.
print(concatenada)  # Muestra la lista actualizada.

# Ejercicio 17: Usar el método .count() para contar cuántas veces aparece un elemento específico en la lista del ejercicio 7.
print(multiplicados.count(15))  # Cuenta cuántas veces aparece el valor 15.

# Ejercicio 18: Usar el método .index() para obtener el índice de un elemento específico en la lista del ejercicio 4.
# Si algún elemento existe, como "100".
print(concatenada.index(100))

# Ejercicio 19: Usar el método .clear() para eliminar todos los elementos de la lista del ejercicio 1.
frutas.clear()  # Elimina todos los elementos de la lista.
print(frutas)  # Muestra la lista vacía.

# Ejercicio 20: Crear una lista vacía y utilizar un bucle for para agregar los números del 1 al 10.
lista_vacia = []  # Crea una lista vacía.
for i in range(1, 11):  # Itera del 1 al 10.
    lista_vacia.append(i)  # Agrega cada número a la lista.
print(lista_vacia)  # Muestra la lista.

# Ejercicio 21: Crear una lista de números enteros y utilizar un bucle while para eliminar los elementos impares.
enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Lista de enteros.
i = 0  # Índice inicial.
while i < len(enteros):  # Mientras haya elementos en la lista.
    if enteros[i] % 2 != 0:  # Si el elemento es impar.
        enteros.pop(i)  # Elimina el elemento.
    else:
        i += 1  # Avanza al siguiente índice si no se elimina.
print(enteros)  # Muestra la lista sin números impares.

# Ejercicio 22: Crear una lista con los nombres de 5 materias favoritas y ordenarlas alfabéticamente.
materias = ["Matemáticas", "Física", "Historia", "Arte", "Programación"]
materias.sort()  # Ordena la lista alfabéticamente.
print(materias)

# Ejercicio 23: Crear una lista con los números del 1 al 15 y mostrar solo los múltiplos de 3.
numeros = list(range(1, 16))  # Lista del 1 al 15.
multiplos_de_3 = [x for x in numeros if x % 3 == 0]  # Filtra múltiplos de 3.
print(multiplos_de_3)

# Ejercicio 24: Crear una lista con los nombres de 10 artistas favoritos y utilizar un bucle for para imprimir cada nombre en mayúsculas.
artistas = ["Shakira", "Juanes", "Carlos Vives", "Maluma", "J Balvin", "Karol G", "Fonseca", "Silvestre Dangond", "Andrés Cepeda", "Sebastián Yatra"]
for artista in artistas:  # Recorre cada artista.
    print(artista.upper())  # Imprime el nombre en mayúsculas.

# Ejercicio 25: Crear una lista con los números del 1 al 20 y utilizar una comprensión de listas para crear una nueva lista con solo los números pares.
numeros = list(range(1, 21))  # Lista del 1 al 20.
pares = [x for x in numeros if x % 2 == 0]  # Filtra números pares.
print(pares)

# Ejercicio 26: Crear una lista con los nombres de los municipios del departamento de Arauca y utilizar un bucle for para imprimir cada nombre en orden inverso.
municipios = ["Arauca", "Arauquita", "Tame", "Saravena", "Fortul", "Cravo Norte", "Puerto Rondón"]
for municipio in municipios:  # Recorre cada municipio.
    print(municipio[::-1])  # Imprime el nombre en orden inverso.

# Ejercicio 27: Crear una lista con los números del 1 al 12 y utilizar una comprensión de listas para crear una nueva lista con los cuadrados de cada número.
numeros = list(range(1, 13))  # Lista del 1 al 12.
cuadrados = [x ** 2 for x in numeros]  # Calcula los cuadrados.
print(cuadrados)

# Ejercicio 28: Crear una lista con los meses del año y utilizar el método .index() para obtener el índice del mes "Junio".
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
print(meses.index("Junio"))  # Obtiene el índice de "Junio".

# Ejercicio 29: Crear una lista con los nombres que usted le pondría a 6 mascotas y utilizar el método .remove() para eliminar una mascota de la lista.
mascotas = ["Luna", "Max", "Bella", "Charlie", "Rocky", "Sasha"]
mascotas.remove("Max")  # Elimina "Max" de la lista.
print(mascotas)

# Ejercicio 30: Crear una lista con los números del 1 al 20 y utilizar el método .sort(reverse=True) para ordenarla de forma descendente.
numeros = list(range(1, 21))  # Lista del 1 al 20.
numeros.sort(reverse=True)  # Ordena de forma descendente.
print(numeros)

# Ejercicio 31: Crear una lista con los nombres de 4 libros favoritos y utilizar el método .append() para agregar un nuevo libro al final de la lista.
libros = ["Cien años de soledad", "Don Quijote", "1984", "El principito"]
libros.append("La Odisea")  # Agrega un nuevo libro.
print(libros)

# Ejercicio 32: Crear una lista con los números del 1 al 15 y utilizar una comprensión de listas para crear una nueva lista con los números impares.
numeros = list(range(1, 16))  # Lista del 1 al 15.
impares = [x for x in numeros if x % 2 != 0]  # Filtra números impares.
print(impares)

# Ejercicio 33: Crear una lista con los nombres de 7 comidas favoritas y utilizar el método .insert() para agregar una nueva comida en la posición 3.
comidas = ["Arepas", "Bandeja Paisa", "Sancocho", "Tamales", "Empanadas", "Lechona", "Chorizo"]
comidas.insert(3, "Ajiaco")  # Inserta una comida en la posición 3.
print(comidas)

# Ejercicio 34: Crear una lista con los números del 1 al 10 y utilizar el método .extend() para agregar una segunda lista con los números del 11 al 15.
numeros = list(range(1, 11))  # Lista del 1 al 10.
numeros.extend(range(11, 16))  # Agrega los números del 11 al 15.
print(numeros)
# Ejercicio 35: Crear una lista con los nombres de 6 compañeros y utilizar el método .count() para contar cuántas veces aparece un nombre específico en la lista.
compañeros = ["Juan", "María", "Luis", "Ana", "Luis", "Pedro"]
print(compañeros.count("Luis"))  # Cuenta cuántas veces aparece "Luis".

# Ejercicio 36: Crear una lista con los números del 1 al 12 y utilizar una comprensión de listas para crear una nueva lista con los números divisibles por 3.
numeros = list(range(1, 13))  # Lista del 1 al 12.
divisibles_por_3 = [x for x in numeros if x % 3 == 0]  # Filtra divisibles por 3.
print(divisibles_por_3)

# Ejercicio 37: Crear una lista con los nombres de 5 artistas musicales favoritos y utilizar el método .reverse() para invertir el orden de la lista.
artistas = ["Shakira", "Juanes", "Karol G", "Maluma", "J Balvin"]
artistas.reverse()  # Invierte el orden de la lista.
print(artistas)

# Ejercicio 38: Crear una lista con los números del 1 al 20 y utilizar una función lambda y el método .sort() para ordenar la lista de forma descendente.
numeros = list(range(1, 21))  # Lista del 1 al 20.
numeros.sort(key=lambda x: -x)  # Ordena de forma descendente usando lambda.
print(numeros)

# Ejercicio 39: Crear una lista con las materias de la universidad y utilizar el método .pop() para eliminar y obtener el último elemento de la lista.
materias = ["Matemáticas", "Física", "Programación", "Historia", "Arte"]
ultima_materia = materias.pop()  # Elimina y guarda el último elemento.
print(ultima_materia)  # Muestra la materia eliminada.
print(materias)  # Muestra la lista actualizada.

# Ejercicio 40: Crear una lista con los números del 1 al 25 y utilizar una comprensión de listas para crear una nueva lista con los números múltiplos de 5.
numeros = list(range(1, 26))  # Lista del 1 al 25.
multiplos_de_5 = [x for x in numeros if x % 5 == 0]  # Filtra múltiplos de 5.
print(multiplos_de_5)

# Ejercicio 41: Crear una lista con los nombres de 8 deportes y utilizar una función anónima y el método .sort() para ordenar la lista.
deportes = ["Fútbol", "Baloncesto", "Tenis", "Voleibol", "Natación", "Béisbol", "Atletismo", "Ciclismo"]
deportes.sort(key=lambda deporte: deporte)  # Ordena alfabéticamente usando una función lambda.
print(deportes)

# Ejercicio 42: Crear una lista con los números del 1 al 15 y utilizar el método .clear() para eliminar todos los elementos de la lista.
numeros = list(range(1, 16))  # Lista del 1 al 15.
numeros.clear()  # Elimina todos los elementos.
print(numeros)  # Muestra la lista vacía.

# Ejercicio 43: Crear una lista con los nombres de 6 países y utilizar un bucle for para imprimir cada nombre en minúsculas.
paises = ["Colombia", "Argentina", "Brasil", "Chile", "Perú", "México"]
for pais in paises:  # Recorre cada país.
    print(pais.lower())  # Imprime el nombre en minúsculas.

# Ejercicio 44: Crear una lista con los números del 1 al 20 y utilizar una comprensión de listas para crear una nueva lista con los cuadrados de los números pares.
numeros = list(range(1, 21))  # Lista del 1 al 20.
cuadrados_pares = [x**2 for x in numeros if x % 2 == 0]  # Calcula cuadrados de números pares.
print(cuadrados_pares)

# Ejercicio 45: Crear una lista con los nombres de 10 videojuegos y utilizar el método .index() para obtener el índice de un juego específico.
videojuegos = ["Minecraft", "FIFA", "Call of Duty", "Fortnite", "Valorant", "Among Us", "The Sims", "GTA V", "PUBG", "Zelda"]
print(videojuegos.index("Fortnite"))  # Obtiene el índice de "Fortnite".

# Ejercicio 46: Crear una lista con los números del 1 al 12 y utilizar el método .remove() para eliminar un número específico de la lista.
numeros = list(range(1, 13))  # Lista del 1 al 12.
numeros.remove(6)  # Elimina el número 6.
print(numeros)

# Ejercicio 47: Crear una lista con los nombres de 7 monumentos colombianos y utilizar una función lambda y el método .sort(key=len) para ordenar la lista por longitud de nombre.
monumentos = ["La Candelaria", "El Peñol", "Cristo Rey", "Monserrate", "Ciudad Perdida", "Parque Tayrona", "Santuario de Las Lajas"]
monumentos.sort(key=lambda m: len(m))  # Ordena por longitud de nombre.
print(monumentos)

# Ejercicio 48: Crear una lista con los números del 1 al 18 y utilizar una comprensión de listas para crear una nueva lista con los números múltiplos de 3 y 5.
numeros = list(range(1, 19))  # Lista del 1 al 18.
multiplos_3_5 = [x for x in numeros if x % 3 == 0 and x % 5 == 0]  # Filtra múltiplos de 3 y 5.
print(multiplos_3_5)

# Ejercicio 49: Crear una lista con los nombres de 6 asignaturas que le parecen interesantes de la carrera y utilizar el método .append() para agregar un nuevo nombre al final de la lista.
asignaturas = ["Algoritmos", "Base de Datos", "Redes", "Seguridad Informática", "Inteligencia Artificial", "Machine Learning"]
asignaturas.append("Ciencia de Datos")  # Agrega una nueva asignatura.
print(asignaturas)

# Ejercicio 50: Crear una lista con los números del 1 al 25 y utilizar el método .pop() para eliminar y obtener el elemento de la posición 7.
numeros = list(range(1, 26))  # Lista del 1 al 25.
elemento_eliminado = numeros.pop(7)  # Elimina y guarda el elemento de la posición 7.
print(elemento_eliminado)  # Muestra el elemento eliminado.
print(numeros)  # Muestra la lista actualizada.


# ===================================================================
# Título del trabajo: Seguimiento 1 PII
# Nombre: [Maria Luisa Londoño Moncada]
# Fecha de creación: Noviembre 18, 2024
# Descripción: Este archivo contiene soluciones para diversos ejercicios de manipulación de listas para seguimiento 1 PII C2
# ===================================================================

# -------------------------------------------------------------------
# solución de ejercicios
# -------------------------------------------------------------------

# Ejercicio 1: Crear una lista con los nombres de 5 frutas colombianas favoritas y mostrarla por pantalla.
frutas = ["Lulo", "Guanábana", "Mango", "Borojó", "Maracuyá"]
print(frutas)  # Muestra la lista de frutas.

# Ejercicio 2: Acceder al segundo y cuarto elemento de la lista anterior e imprimirlos.
print(frutas[1])  # Muestra el segundo elemento.
print(frutas[3])  # Muestra el cuarto elemento.

# Ejercicio 3: Crear una lista con los números del 1 al 10 y mostrar su longitud.
numeros = list(range(1, 11))  # Lista del 1 al 10.
print(len(numeros))  # Muestra la longitud de la lista.

# Ejercicio 4: Concatenar las dos listas creadas en los ejercicios 1 y 3.
concatenada = frutas + numeros  # Combina ambas listas.
print(concatenada)  # Muestra la lista concatenada.

# Ejercicio 5: Modificar el tercer elemento de la lista del ejercicio 4 al valor 100.
concatenada[2] = 100  # Cambia el tercer elemento a 100.
print(concatenada)  # Muestra la lista modificada.

# Ejercicio 6: Borrar el último elemento de la lista del ejercicio 4.
concatenada.pop()  # Elimina el último elemento.
print(concatenada)  # Muestra la lista actualizada.

# Ejercicio 7: Crear una lista con 3 números enteros y multiplicar cada elemento por 5.
enteros = [2, 4, 6]
multiplicados = [x * 5 for x in enteros]  # Multiplica cada elemento por 5.
print(multiplicados)

# Ejercicio 8: Crear dos listas con 5 números enteros cada una y multiplicar los elementos correspondientes.
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
resultado = [a * b for a, b in zip(lista1, lista2)]  # Multiplica elementos correspondientes.
print(resultado)

# Ejercicio 9: Crear una lista de listas anidadas y acceder al segundo elemento de la segunda lista.
listas_anidadas = [[1, 2], [3, 4], [5, 6]]
print(listas_anidadas[1][1])  # Accede al segundo elemento de la segunda lista.

# Ejercicio 10: Crear una lista a partir de la lista del ejercicio 3, tomando los elementos del índice 2 al 6.
sublista = numeros[2:7]  # Toma elementos de índice 2 al 6.
print(sublista)

# Ejercicio 11: Usar el método .append() para agregar un nuevo elemento al final de la lista del ejercicio 1.
frutas.append("Guayaba")  # Agrega un nuevo elemento.
print(frutas)

# Ejercicio 12: Usar el método .insert() para agregar un nuevo elemento en la posición 2 de la lista del ejercicio 3.
numeros.insert(2, 20)  # Inserta el número 20 en la posición 2.
print(numeros)

# Ejercicio 13: Usar el método .remove() para eliminar un elemento específico de la lista del ejercicio 7.
multiplicados.remove(10)  # Elimina el valor 10 si existe.
print(multiplicados)

# Ejercicio 14: Usar el método .reverse() para invertir el orden de la lista del ejercicio 4.
concatenada.reverse()  # Invierte el orden de la lista.
print(concatenada)

# Ejercicio 15: Usar el método .sort() para ordenar de forma ascendente la lista del ejercicio 7.
multiplicados.sort()  # Ordena la lista de forma ascendente.
print(multiplicados)

# Ejercicio 16: Usar el método .pop() para eliminar y obtener el último elemento de la lista del ejercicio 4.
ultimo = concatenada.pop()  # Elimina y guarda el último elemento.
print(ultimo)  # Muestra el elemento eliminado.
print(concatenada)  # Muestra la lista actualizada.

# Ejercicio 17: Usar el método .count() para contar cuántas veces aparece un elemento específico en la lista del ejercicio 7.
print(multiplicados.count(15))  # Cuenta cuántas veces aparece el valor 15.

# Ejercicio 18: Usar el método .index() para obtener el índice de un elemento específico en la lista del ejercicio 4.
# Si algún elemento existe, como "100".
print(concatenada.index(100))

# Ejercicio 19: Usar el método .clear() para eliminar todos los elementos de la lista del ejercicio 1.
frutas.clear()  # Elimina todos los elementos de la lista.
print(frutas)  # Muestra la lista vacía.

# Ejercicio 20: Crear una lista vacía y utilizar un bucle for para agregar los números del 1 al 10.
lista_vacia = []  # Crea una lista vacía.
for i in range(1, 11):  # Itera del 1 al 10.
    lista_vacia.append(i)  # Agrega cada número a la lista.
print(lista_vacia)  # Muestra la lista.

# Ejercicio 21: Crear una lista de números enteros y utilizar un bucle while para eliminar los elementos impares.
enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Lista de enteros.
i = 0  # Índice inicial.
while i < len(enteros):  # Mientras haya elementos en la lista.
    if enteros[i] % 2 != 0:  # Si el elemento es impar.
        enteros.pop(i)  # Elimina el elemento.
    else:
        i += 1  # Avanza al siguiente índice si no se elimina.
print(enteros)  # Muestra la lista sin números impares.

# Ejercicio 22: Crear una lista con los nombres de 5 materias favoritas y ordenarlas alfabéticamente.
materias = ["Matemáticas", "Física", "Historia", "Arte", "Programación"]
materias.sort()  # Ordena la lista alfabéticamente.
print(materias)

# Ejercicio 23: Crear una lista con los números del 1 al 15 y mostrar solo los múltiplos de 3.
numeros = list(range(1, 16))  # Lista del 1 al 15.
multiplos_de_3 = [x for x in numeros if x % 3 == 0]  # Filtra múltiplos de 3.
print(multiplos_de_3)

# Ejercicio 24: Crear una lista con los nombres de 10 artistas favoritos y utilizar un bucle for para imprimir cada nombre en mayúsculas.
artistas = ["Shakira", "Juanes", "Carlos Vives", "Maluma", "J Balvin", "Karol G", "Fonseca", "Silvestre Dangond", "Andrés Cepeda", "Sebastián Yatra"]
for artista in artistas:  # Recorre cada artista.
    print(artista.upper())  # Imprime el nombre en mayúsculas.

# Ejercicio 25: Crear una lista con los números del 1 al 20 y utilizar una comprensión de listas para crear una nueva lista con solo los números pares.
numeros = list(range(1, 21))  # Lista del 1 al 20.
pares = [x for x in numeros if x % 2 == 0]  # Filtra números pares.
print(pares)

# Ejercicio 26: Crear una lista con los nombres de los municipios del departamento de Arauca y utilizar un bucle for para imprimir cada nombre en orden inverso.
municipios = ["Arauca", "Arauquita", "Tame", "Saravena", "Fortul", "Cravo Norte", "Puerto Rondón"]
for municipio in municipios:  # Recorre cada municipio.
    print(municipio[::-1])  # Imprime el nombre en orden inverso.

# Ejercicio 27: Crear una lista con los números del 1 al 12 y utilizar una comprensión de listas para crear una nueva lista con los cuadrados de cada número.
numeros = list(range(1, 13))  # Lista del 1 al 12.
cuadrados = [x ** 2 for x in numeros]  # Calcula los cuadrados.
print(cuadrados)

# Ejercicio 28: Crear una lista con los meses del año y utilizar el método .index() para obtener el índice del mes "Junio".
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
print(meses.index("Junio"))  # Obtiene el índice de "Junio".

# Ejercicio 29: Crear una lista con los nombres que usted le pondría a 6 mascotas y utilizar el método .remove() para eliminar una mascota de la lista.
mascotas = ["Luna", "Max", "Bella", "Charlie", "Rocky", "Sasha"]
mascotas.remove("Max")  # Elimina "Max" de la lista.
print(mascotas)

# Ejercicio 30: Crear una lista con los números del 1 al 20 y utilizar el método .sort(reverse=True) para ordenarla de forma descendente.
numeros = list(range(1, 21))  # Lista del 1 al 20.
numeros.sort(reverse=True)  # Ordena de forma descendente.
print(numeros)

# Ejercicio 31: Crear una lista con los nombres de 4 libros favoritos y utilizar el método .append() para agregar un nuevo libro al final de la lista.
libros = ["Cien años de soledad", "Don Quijote", "1984", "El principito"]
libros.append("La Odisea")  # Agrega un nuevo libro.
print(libros)

# Ejercicio 32: Crear una lista con los números del 1 al 15 y utilizar una comprensión de listas para crear una nueva lista con los números impares.
numeros = list(range(1, 16))  # Lista del 1 al 15.
impares = [x for x in numeros if x % 2 != 0]  # Filtra números impares.
print(impares)

# Ejercicio 33: Crear una lista con los nombres de 7 comidas favoritas y utilizar el método .insert() para agregar una nueva comida en la posición 3.
comidas = ["Arepas", "Bandeja Paisa", "Sancocho", "Tamales", "Empanadas", "Lechona", "Chorizo"]
comidas.insert(3, "Ajiaco")  # Inserta una comida en la posición 3.
print(comidas)

# Ejercicio 34: Crear una lista con los números del 1 al 10 y utilizar el método .extend() para agregar una segunda lista con los números del 11 al 15.
numeros = list(range(1, 11))  # Lista del 1 al 10.
numeros.extend(range(11, 16))  # Agrega los números del 11 al 15.
print(numeros)
# Ejercicio 35: Crear una lista con los nombres de 6 compañeros y utilizar el método .count() para contar cuántas veces aparece un nombre específico en la lista.
compañeros = ["Juan", "María", "Luis", "Ana", "Luis", "Pedro"]
print(compañeros.count("Luis"))  # Cuenta cuántas veces aparece "Luis".

# Ejercicio 36: Crear una lista con los números del 1 al 12 y utilizar una comprensión de listas para crear una nueva lista con los números divisibles por 3.
numeros = list(range(1, 13))  # Lista del 1 al 12.
divisibles_por_3 = [x for x in numeros if x % 3 == 0]  # Filtra divisibles por 3.
print(divisibles_por_3)

# Ejercicio 37: Crear una lista con los nombres de 5 artistas musicales favoritos y utilizar el método .reverse() para invertir el orden de la lista.
artistas = ["Shakira", "Juanes", "Karol G", "Maluma", "J Balvin"]
artistas.reverse()  # Invierte el orden de la lista.
print(artistas)

# Ejercicio 38: Crear una lista con los números del 1 al 20 y utilizar una función lambda y el método .sort() para ordenar la lista de forma descendente.
numeros = list(range(1, 21))  # Lista del 1 al 20.
numeros.sort(key=lambda x: -x)  # Ordena de forma descendente usando lambda.
print(numeros)

# Ejercicio 39: Crear una lista con las materias de la universidad y utilizar el método .pop() para eliminar y obtener el último elemento de la lista.
materias = ["Matemáticas", "Física", "Programación", "Historia", "Arte"]
ultima_materia = materias.pop()  # Elimina y guarda el último elemento.
print(ultima_materia)  # Muestra la materia eliminada.
print(materias)  # Muestra la lista actualizada.

# Ejercicio 40: Crear una lista con los números del 1 al 25 y utilizar una comprensión de listas para crear una nueva lista con los números múltiplos de 5.
numeros = list(range(1, 26))  # Lista del 1 al 25.
multiplos_de_5 = [x for x in numeros if x % 5 == 0]  # Filtra múltiplos de 5.
print(multiplos_de_5)

# Ejercicio 41: Crear una lista con los nombres de 8 deportes y utilizar una función anónima y el método .sort() para ordenar la lista.
deportes = ["Fútbol", "Baloncesto", "Tenis", "Voleibol", "Natación", "Béisbol", "Atletismo", "Ciclismo"]
deportes.sort(key=lambda deporte: deporte)  # Ordena alfabéticamente usando una función lambda.
print(deportes)

# Ejercicio 42: Crear una lista con los números del 1 al 15 y utilizar el método .clear() para eliminar todos los elementos de la lista.
numeros = list(range(1, 16))  # Lista del 1 al 15.
numeros.clear()  # Elimina todos los elementos.
print(numeros)  # Muestra la lista vacía.

# Ejercicio 43: Crear una lista con los nombres de 6 países y utilizar un bucle for para imprimir cada nombre en minúsculas.
paises = ["Colombia", "Argentina", "Brasil", "Chile", "Perú", "México"]
for pais in paises:  # Recorre cada país.
    print(pais.lower())  # Imprime el nombre en minúsculas.

# Ejercicio 44: Crear una lista con los números del 1 al 20 y utilizar una comprensión de listas para crear una nueva lista con los cuadrados de los números pares.
numeros = list(range(1, 21))  # Lista del 1 al 20.
cuadrados_pares = [x**2 for x in numeros if x % 2 == 0]  # Calcula cuadrados de números pares.
print(cuadrados_pares)

# Ejercicio 45: Crear una lista con los nombres de 10 videojuegos y utilizar el método .index() para obtener el índice de un juego específico.
videojuegos = ["Minecraft", "FIFA", "Call of Duty", "Fortnite", "Valorant", "Among Us", "The Sims", "GTA V", "PUBG", "Zelda"]
print(videojuegos.index("Fortnite"))  # Obtiene el índice de "Fortnite".

# Ejercicio 46: Crear una lista con los números del 1 al 12 y utilizar el método .remove() para eliminar un número específico de la lista.
numeros = list(range(1, 13))  # Lista del 1 al 12.
numeros.remove(6)  # Elimina el número 6.
print(numeros)

# Ejercicio 47: Crear una lista con los nombres de 7 monumentos colombianos y utilizar una función lambda y el método .sort(key=len) para ordenar la lista por longitud de nombre.
monumentos = ["La Candelaria", "El Peñol", "Cristo Rey", "Monserrate", "Ciudad Perdida", "Parque Tayrona", "Santuario de Las Lajas"]
monumentos.sort(key=lambda m: len(m))  # Ordena por longitud de nombre.
print(monumentos)

# Ejercicio 48: Crear una lista con los números del 1 al 18 y utilizar una comprensión de listas para crear una nueva lista con los números múltiplos de 3 y 5.
numeros = list(range(1, 19))  # Lista del 1 al 18.
multiplos_3_5 = [x for x in numeros if x % 3 == 0 and x % 5 == 0]  # Filtra múltiplos de 3 y 5.
print(multiplos_3_5)

# Ejercicio 49: Crear una lista con los nombres de 6 asignaturas que le parecen interesantes de la carrera y utilizar el método .append() para agregar un nuevo nombre al final de la lista.
asignaturas = ["Algoritmos", "Base de Datos", "Redes", "Seguridad Informática", "Inteligencia Artificial", "Machine Learning"]
asignaturas.append("Ciencia de Datos")  # Agrega una nueva asignatura.
print(asignaturas)

# Ejercicio 50: Crear una lista con los números del 1 al 25 y utilizar el método .pop() para eliminar y obtener el elemento de la posición 7.
numeros = list(range(1, 26))  # Lista del 1 al 25.
elemento_eliminado = numeros.pop(7)  # Elimina y guarda el elemento de la posición 7.
print(elemento_eliminado)  # Muestra el elemento eliminado.
print(numeros)  # Muestra la lista actualizada.


# ===================================================================
# Título del trabajo: Seguimiento 1 PII
# Nombre: [Maria Luisa Londoño Moncada]
# Fecha de creación: Noviembre 18, 2024
# Descripción: Este archivo contiene soluciones para diversos ejercicios de manipulación de listas para seguimiento 1 PII C2
# ===================================================================

# -------------------------------------------------------------------
# solución de ejercicios
# -------------------------------------------------------------------

# Ejercicio 1: Crear una lista con los nombres de 5 frutas colombianas favoritas y mostrarla por pantalla.
frutas = ["Lulo", "Guanábana", "Mango", "Borojó", "Maracuyá"]
print(frutas)  # Muestra la lista de frutas.

# Ejercicio 2: Acceder al segundo y cuarto elemento de la lista anterior e imprimirlos.
print(frutas[1])  # Muestra el segundo elemento.
print(frutas[3])  # Muestra el cuarto elemento.

# Ejercicio 3: Crear una lista con los números del 1 al 10 y mostrar su longitud.
numeros = list(range(1, 11))  # Lista del 1 al 10.
print(len(numeros))  # Muestra la longitud de la lista.

# Ejercicio 4: Concatenar las dos listas creadas en los ejercicios 1 y 3.
concatenada = frutas + numeros  # Combina ambas listas.
print(concatenada)  # Muestra la lista concatenada.

# Ejercicio 5: Modificar el tercer elemento de la lista del ejercicio 4 al valor 100.
concatenada[2] = 100  # Cambia el tercer elemento a 100.
print(concatenada)  # Muestra la lista modificada.

# Ejercicio 6: Borrar el último elemento de la lista del ejercicio 4.
concatenada.pop()  # Elimina el último elemento.
print(concatenada)  # Muestra la lista actualizada.

# Ejercicio 7: Crear una lista con 3 números enteros y multiplicar cada elemento por 5.
enteros = [2, 4, 6]
multiplicados = [x * 5 for x in enteros]  # Multiplica cada elemento por 5.
print(multiplicados)

# Ejercicio 8: Crear dos listas con 5 números enteros cada una y multiplicar los elementos correspondientes.
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
resultado = [a * b for a, b in zip(lista1, lista2)]  # Multiplica elementos correspondientes.
print(resultado)

# Ejercicio 9: Crear una lista de listas anidadas y acceder al segundo elemento de la segunda lista.
listas_anidadas = [[1, 2], [3, 4], [5, 6]]
print(listas_anidadas[1][1])  # Accede al segundo elemento de la segunda lista.

# Ejercicio 10: Crear una lista a partir de la lista del ejercicio 3, tomando los elementos del índice 2 al 6.
sublista = numeros[2:7]  # Toma elementos de índice 2 al 6.
print(sublista)

# Ejercicio 11: Usar el método .append() para agregar un nuevo elemento al final de la lista del ejercicio 1.
frutas.append("Guayaba")  # Agrega un nuevo elemento.
print(frutas)

# Ejercicio 12: Usar el método .insert() para agregar un nuevo elemento en la posición 2 de la lista del ejercicio 3.
numeros.insert(2, 20)  # Inserta el número 20 en la posición 2.
print(numeros)

# Ejercicio 13: Usar el método .remove() para eliminar un elemento específico de la lista del ejercicio 7.
multiplicados.remove(10)  # Elimina el valor 10 si existe.
print(multiplicados)

# Ejercicio 14: Usar el método .reverse() para invertir el orden de la lista del ejercicio 4.
concatenada.reverse()  # Invierte el orden de la lista.
print(concatenada)

# Ejercicio 15: Usar el método .sort() para ordenar de forma ascendente la lista del ejercicio 7.
multiplicados.sort()  # Ordena la lista de forma ascendente.
print(multiplicados)

# Ejercicio 16: Usar el método .pop() para eliminar y obtener el último elemento de la lista del ejercicio 4.
ultimo = concatenada.pop()  # Elimina y guarda el último elemento.
print(ultimo)  # Muestra el elemento eliminado.
print(concatenada)  # Muestra la lista actualizada.

# Ejercicio 17: Usar el método .count() para contar cuántas veces aparece un elemento específico en la lista del ejercicio 7.
print(multiplicados.count(15))  # Cuenta cuántas veces aparece el valor 15.

# Ejercicio 18: Usar el método .index() para obtener el índice de un elemento específico en la lista del ejercicio 4.
# Si algún elemento existe, como "100".
print(concatenada.index(100))

# Ejercicio 19: Usar el método .clear() para eliminar todos los elementos de la lista del ejercicio 1.
frutas.clear()  # Elimina todos los elementos de la lista.
print(frutas)  # Muestra la lista vacía.

# Ejercicio 20: Crear una lista vacía y utilizar un bucle for para agregar los números del 1 al 10.
lista_vacia = []  # Crea una lista vacía.
for i in range(1, 11):  # Itera del 1 al 10.
    lista_vacia.append(i)  # Agrega cada número a la lista.
print(lista_vacia)  # Muestra la lista.

# Ejercicio 21: Crear una lista de números enteros y utilizar un bucle while para eliminar los elementos impares.
enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Lista de enteros.
i = 0  # Índice inicial.
while i < len(enteros):  # Mientras haya elementos en la lista.
    if enteros[i] % 2 != 0:  # Si el elemento es impar.
        enteros.pop(i)  # Elimina el elemento.
    else:
        i += 1  # Avanza al siguiente índice si no se elimina.
print(enteros)  # Muestra la lista sin números impares.

# Ejercicio 22: Crear una lista con los nombres de 5 materias favoritas y ordenarlas alfabéticamente.
materias = ["Matemáticas", "Física", "Historia", "Arte", "Programación"]
materias.sort()  # Ordena la lista alfabéticamente.
print(materias)

# Ejercicio 23: Crear una lista con los números del 1 al 15 y mostrar solo los múltiplos de 3.
numeros = list(range(1, 16))  # Lista del 1 al 15.
multiplos_de_3 = [x for x in numeros if x % 3 == 0]  # Filtra múltiplos de 3.
print(multiplos_de_3)

# Ejercicio 24: Crear una lista con los nombres de 10 artistas favoritos y utilizar un bucle for para imprimir cada nombre en mayúsculas.
artistas = ["Shakira", "Juanes", "Carlos Vives", "Maluma", "J Balvin", "Karol G", "Fonseca", "Silvestre Dangond", "Andrés Cepeda", "Sebastián Yatra"]
for artista in artistas:  # Recorre cada artista.
    print(artista.upper())  # Imprime el nombre en mayúsculas.

# Ejercicio 25: Crear una lista con los números del 1 al 20 y utilizar una comprensión de listas para crear una nueva lista con solo los números pares.
numeros = list(range(1, 21))  # Lista del 1 al 20.
pares = [x for x in numeros if x % 2 == 0]  # Filtra números pares.
print(pares)

# Ejercicio 26: Crear una lista con los nombres de los municipios del departamento de Arauca y utilizar un bucle for para imprimir cada nombre en orden inverso.
municipios = ["Arauca", "Arauquita", "Tame", "Saravena", "Fortul", "Cravo Norte", "Puerto Rondón"]
for municipio in municipios:  # Recorre cada municipio.
    print(municipio[::-1])  # Imprime el nombre en orden inverso.

# Ejercicio 27: Crear una lista con los números del 1 al 12 y utilizar una comprensión de listas para crear una nueva lista con los cuadrados de cada número.
numeros = list(range(1, 13))  # Lista del 1 al 12.
cuadrados = [x ** 2 for x in numeros]  # Calcula los cuadrados.
print(cuadrados)

# Ejercicio 28: Crear una lista con los meses del año y utilizar el método .index() para obtener el índice del mes "Junio".
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
print(meses.index("Junio"))  # Obtiene el índice de "Junio".

# Ejercicio 29: Crear una lista con los nombres que usted le pondría a 6 mascotas y utilizar el método .remove() para eliminar una mascota de la lista.
mascotas = ["Luna", "Max", "Bella", "Charlie", "Rocky", "Sasha"]
mascotas.remove("Max")  # Elimina "Max" de la lista.
print(mascotas)

# Ejercicio 30: Crear una lista con los números del 1 al 20 y utilizar el método .sort(reverse=True) para ordenarla de forma descendente.
numeros = list(range(1, 21))  # Lista del 1 al 20.
numeros.sort(reverse=True)  # Ordena de forma descendente.
print(numeros)

# Ejercicio 31: Crear una lista con los nombres de 4 libros favoritos y utilizar el método .append() para agregar un nuevo libro al final de la lista.
libros = ["Cien años de soledad", "Don Quijote", "1984", "El principito"]
libros.append("La Odisea")  # Agrega un nuevo libro.
print(libros)

# Ejercicio 32: Crear una lista con los números del 1 al 15 y utilizar una comprensión de listas para crear una nueva lista con los números impares.
numeros = list(range(1, 16))  # Lista del 1 al 15.
impares = [x for x in numeros if x % 2 != 0]  # Filtra números impares.
print(impares)

# Ejercicio 33: Crear una lista con los nombres de 7 comidas favoritas y utilizar el método .insert() para agregar una nueva comida en la posición 3.
comidas = ["Arepas", "Bandeja Paisa", "Sancocho", "Tamales", "Empanadas", "Lechona", "Chorizo"]
comidas.insert(3, "Ajiaco")  # Inserta una comida en la posición 3.
print(comidas)

# Ejercicio 34: Crear una lista con los números del 1 al 10 y utilizar el método .extend() para agregar una segunda lista con los números del 11 al 15.
numeros = list(range(1, 11))  # Lista del 1 al 10.
numeros.extend(range(11, 16))  # Agrega los números del 11 al 15.
print(numeros)
# Ejercicio 35: Crear una lista con los nombres de 6 compañeros y utilizar el método .count() para contar cuántas veces aparece un nombre específico en la lista.
compañeros = ["Juan", "María", "Luis", "Ana", "Luis", "Pedro"]
print(compañeros.count("Luis"))  # Cuenta cuántas veces aparece "Luis".

# Ejercicio 36: Crear una lista con los números del 1 al 12 y utilizar una comprensión de listas para crear una nueva lista con los números divisibles por 3.
numeros = list(range(1, 13))  # Lista del 1 al 12.
divisibles_por_3 = [x for x in numeros if x % 3 == 0]  # Filtra divisibles por 3.
print(divisibles_por_3)

# Ejercicio 37: Crear una lista con los nombres de 5 artistas musicales favoritos y utilizar el método .reverse() para invertir el orden de la lista.
artistas = ["Shakira", "Juanes", "Karol G", "Maluma", "J Balvin"]
artistas.reverse()  # Invierte el orden de la lista.
print(artistas)

# Ejercicio 38: Crear una lista con los números del 1 al 20 y utilizar una función lambda y el método .sort() para ordenar la lista de forma descendente.
numeros = list(range(1, 21))  # Lista del 1 al 20.
numeros.sort(key=lambda x: -x)  # Ordena de forma descendente usando lambda.
print(numeros)

# Ejercicio 39: Crear una lista con las materias de la universidad y utilizar el método .pop() para eliminar y obtener el último elemento de la lista.
materias = ["Matemáticas", "Física", "Programación", "Historia", "Arte"]
ultima_materia = materias.pop()  # Elimina y guarda el último elemento.
print(ultima_materia)  # Muestra la materia eliminada.
print(materias)  # Muestra la lista actualizada.

# Ejercicio 40: Crear una lista con los números del 1 al 25 y utilizar una comprensión de listas para crear una nueva lista con los números múltiplos de 5.
numeros = list(range(1, 26))  # Lista del 1 al 25.
multiplos_de_5 = [x for x in numeros if x % 5 == 0]  # Filtra múltiplos de 5.
print(multiplos_de_5)

# Ejercicio 41: Crear una lista con los nombres de 8 deportes y utilizar una función anónima y el método .sort() para ordenar la lista.
deportes = ["Fútbol", "Baloncesto", "Tenis", "Voleibol", "Natación", "Béisbol", "Atletismo", "Ciclismo"]
deportes.sort(key=lambda deporte: deporte)  # Ordena alfabéticamente usando una función lambda.
print(deportes)

# Ejercicio 42: Crear una lista con los números del 1 al 15 y utilizar el método .clear() para eliminar todos los elementos de la lista.
numeros = list(range(1, 16))  # Lista del 1 al 15.
numeros.clear()  # Elimina todos los elementos.
print(numeros)  # Muestra la lista vacía.

# Ejercicio 43: Crear una lista con los nombres de 6 países y utilizar un bucle for para imprimir cada nombre en minúsculas.
paises = ["Colombia", "Argentina", "Brasil", "Chile", "Perú", "México"]
for pais in paises:  # Recorre cada país.
    print(pais.lower())  # Imprime el nombre en minúsculas.

# Ejercicio 44: Crear una lista con los números del 1 al 20 y utilizar una comprensión de listas para crear una nueva lista con los cuadrados de los números pares.
numeros = list(range(1, 21))  # Lista del 1 al 20.
cuadrados_pares = [x**2 for x in numeros if x % 2 == 0]  # Calcula cuadrados de números pares.
print(cuadrados_pares)

# Ejercicio 45: Crear una lista con los nombres de 10 videojuegos y utilizar el método .index() para obtener el índice de un juego específico.
videojuegos = ["Minecraft", "FIFA", "Call of Duty", "Fortnite", "Valorant", "Among Us", "The Sims", "GTA V", "PUBG", "Zelda"]
print(videojuegos.index("Fortnite"))  # Obtiene el índice de "Fortnite".

# Ejercicio 46: Crear una lista con los números del 1 al 12 y utilizar el método .remove() para eliminar un número específico de la lista.
numeros = list(range(1, 13))  # Lista del 1 al 12.
numeros.remove(6)  # Elimina el número 6.
print(numeros)

# Ejercicio 47: Crear una lista con los nombres de 7 monumentos colombianos y utilizar una función lambda y el método .sort(key=len) para ordenar la lista por longitud de nombre.
monumentos = ["La Candelaria", "El Peñol", "Cristo Rey", "Monserrate", "Ciudad Perdida", "Parque Tayrona", "Santuario de Las Lajas"]
monumentos.sort(key=lambda m: len(m))  # Ordena por longitud de nombre.
print(monumentos)

# Ejercicio 48: Crear una lista con los números del 1 al 18 y utilizar una comprensión de listas para crear una nueva lista con los números múltiplos de 3 y 5.
numeros = list(range(1, 19))  # Lista del 1 al 18.
multiplos_3_5 = [x for x in numeros if x % 3 == 0 and x % 5 == 0]  # Filtra múltiplos de 3 y 5.
print(multiplos_3_5)

# Ejercicio 49: Crear una lista con los nombres de 6 asignaturas que le parecen interesantes de la carrera y utilizar el método .append() para agregar un nuevo nombre al final de la lista.
asignaturas = ["Algoritmos", "Base de Datos", "Redes", "Seguridad Informática", "Inteligencia Artificial", "Machine Learning"]
asignaturas.append("Ciencia de Datos")  # Agrega una nueva asignatura.
print(asignaturas)

# Ejercicio 50: Crear una lista con los números del 1 al 25 y utilizar el método .pop() para eliminar y obtener el elemento de la posición 7.
numeros = list(range(1, 26))  # Lista del 1 al 25.
elemento_eliminado = numeros.pop(7)  # Elimina y guarda el elemento de la posición 7.
print(elemento_eliminado)  # Muestra el elemento eliminado.
print(numeros)  # Muestra la lista actualizada.


# ===================================================================
# Título del trabajo: Seguimiento 1 PII
# Nombre: [Maria Luisa Londoño Moncada]
# Fecha de creación: Noviembre 18, 2024
# Descripción: Este archivo contiene soluciones para diversos ejercicios de manipulación de listas para seguimiento 1 PII C2
# ===================================================================

# -------------------------------------------------------------------
# solución de ejercicios
# -------------------------------------------------------------------

# Ejercicio 1: Crear una lista con los nombres de 5 frutas colombianas favoritas y mostrarla por pantalla.
frutas = ["Lulo", "Guanábana", "Mango", "Borojó", "Maracuyá"]
print(frutas)  # Muestra la lista de frutas.

# Ejercicio 2: Acceder al segundo y cuarto elemento de la lista anterior e imprimirlos.
print(frutas[1])  # Muestra el segundo elemento.
print(frutas[3])  # Muestra el cuarto elemento.

# Ejercicio 3: Crear una lista con los números del 1 al 10 y mostrar su longitud.
numeros = list(range(1, 11))  # Lista del 1 al 10.
print(len(numeros))  # Muestra la longitud de la lista.

# Ejercicio 4: Concatenar las dos listas creadas en los ejercicios 1 y 3.
concatenada = frutas + numeros  # Combina ambas listas.
print(concatenada)  # Muestra la lista concatenada.

# Ejercicio 5: Modificar el tercer elemento de la lista del ejercicio 4 al valor 100.
concatenada[2] = 100  # Cambia el tercer elemento a 100.
print(concatenada)  # Muestra la lista modificada.

# Ejercicio 6: Borrar el último elemento de la lista del ejercicio 4.
concatenada.pop()  # Elimina el último elemento.
print(concatenada)  # Muestra la lista actualizada.

# Ejercicio 7: Crear una lista con 3 números enteros y multiplicar cada elemento por 5.
enteros = [2, 4, 6]
multiplicados = [x * 5 for x in enteros]  # Multiplica cada elemento por 5.
print(multiplicados)

# Ejercicio 8: Crear dos listas con 5 números enteros cada una y multiplicar los elementos correspondientes.
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
resultado = [a * b for a, b in zip(lista1, lista2)]  # Multiplica elementos correspondientes.
print(resultado)

# Ejercicio 9: Crear una lista de listas anidadas y acceder al segundo elemento de la segunda lista.
listas_anidadas = [[1, 2], [3, 4], [5, 6]]
print(listas_anidadas[1][1])  # Accede al segundo elemento de la segunda lista.

# Ejercicio 10: Crear una lista a partir de la lista del ejercicio 3, tomando los elementos del índice 2 al 6.
sublista = numeros[2:7]  # Toma elementos de índice 2 al 6.
print(sublista)

# Ejercicio 11: Usar el método .append() para agregar un nuevo elemento al final de la lista del ejercicio 1.
frutas.append("Guayaba")  # Agrega un nuevo elemento.
print(frutas)

# Ejercicio 12: Usar el método .insert() para agregar un nuevo elemento en la posición 2 de la lista del ejercicio 3.
numeros.insert(2, 20)  # Inserta el número 20 en la posición 2.
print(numeros)

# Ejercicio 13: Usar el método .remove() para eliminar un elemento específico de la lista del ejercicio 7.
multiplicados.remove(10)  # Elimina el valor 10 si existe.
print(multiplicados)

# Ejercicio 14: Usar el método .reverse() para invertir el orden de la lista del ejercicio 4.
concatenada.reverse()  # Invierte el orden de la lista.
print(concatenada)

# Ejercicio 15: Usar el método .sort() para ordenar de forma ascendente la lista del ejercicio 7.
multiplicados.sort()  # Ordena la lista de forma ascendente.
print(multiplicados)

# Ejercicio 16: Usar el método .pop() para eliminar y obtener el último elemento de la lista del ejercicio 4.
ultimo = concatenada.pop()  # Elimina y guarda el último elemento.
print(ultimo)  # Muestra el elemento eliminado.
print(concatenada)  # Muestra la lista actualizada.

# Ejercicio 17: Usar el método .count() para contar cuántas veces aparece un elemento específico en la lista del ejercicio 7.
print(multiplicados.count(15))  # Cuenta cuántas veces aparece el valor 15.

# Ejercicio 18: Usar el método .index() para obtener el índice de un elemento específico en la lista del ejercicio 4.
# Si algún elemento existe, como "100".
print(concatenada.index(100))

# Ejercicio 19: Usar el método .clear() para eliminar todos los elementos de la lista del ejercicio 1.
frutas.clear()  # Elimina todos los elementos de la lista.
print(frutas)  # Muestra la lista vacía.

# Ejercicio 20: Crear una lista vacía y utilizar un bucle for para agregar los números del 1 al 10.
lista_vacia = []  # Crea una lista vacía.
for i in range(1, 11):  # Itera del 1 al 10.
    lista_vacia.append(i)  # Agrega cada número a la lista.
print(lista_vacia)  # Muestra la lista.

# Ejercicio 21: Crear una lista de números enteros y utilizar un bucle while para eliminar los elementos impares.
enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Lista de enteros.
i = 0  # Índice inicial.
while i < len(enteros):  # Mientras haya elementos en la lista.
    if enteros[i] % 2 != 0:  # Si el elemento es impar.
        enteros.pop(i)  # Elimina el elemento.
    else:
        i += 1  # Avanza al siguiente índice si no se elimina.
print(enteros)  # Muestra la lista sin números impares.

# Ejercicio 22: Crear una lista con los nombres de 5 materias favoritas y ordenarlas alfabéticamente.
materias = ["Matemáticas", "Física", "Historia", "Arte", "Programación"]
materias.sort()  # Ordena la lista alfabéticamente.
print(materias)

# Ejercicio 23: Crear una lista con los números del 1 al 15 y mostrar solo los múltiplos de 3.
numeros = list(range(1, 16))  # Lista del 1 al 15.
multiplos_de_3 = [x for x in numeros if x % 3 == 0]  # Filtra múltiplos de 3.
print(multiplos_de_3)

# Ejercicio 24: Crear una lista con los nombres de 10 artistas favoritos y utilizar un bucle for para imprimir cada nombre en mayúsculas.
artistas = ["Shakira", "Juanes", "Carlos Vives", "Maluma", "J Balvin", "Karol G", "Fonseca", "Silvestre Dangond", "Andrés Cepeda", "Sebastián Yatra"]
for artista in artistas:  # Recorre cada artista.
    print(artista.upper())  # Imprime el nombre en mayúsculas.

# Ejercicio 25: Crear una lista con los números del 1 al 20 y utilizar una comprensión de listas para crear una nueva lista con solo los números pares.
numeros = list(range(1, 21))  # Lista del 1 al 20.
pares = [x for x in numeros if x % 2 == 0]  # Filtra números pares.
print(pares)

# Ejercicio 26: Crear una lista con los nombres de los municipios del departamento de Arauca y utilizar un bucle for para imprimir cada nombre en orden inverso.
municipios = ["Arauca", "Arauquita", "Tame", "Saravena", "Fortul", "Cravo Norte", "Puerto Rondón"]
for municipio in municipios:  # Recorre cada municipio.
    print(municipio[::-1])  # Imprime el nombre en orden inverso.

# Ejercicio 27: Crear una lista con los números del 1 al 12 y utilizar una comprensión de listas para crear una nueva lista con los cuadrados de cada número.
numeros = list(range(1, 13))  # Lista del 1 al 12.
cuadrados = [x ** 2 for x in numeros]  # Calcula los cuadrados.
print(cuadrados)

# Ejercicio 28: Crear una lista con los meses del año y utilizar el método .index() para obtener el índice del mes "Junio".
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
print(meses.index("Junio"))  # Obtiene el índice de "Junio".

# Ejercicio 29: Crear una lista con los nombres que usted le pondría a 6 mascotas y utilizar el método .remove() para eliminar una mascota de la lista.
mascotas = ["Luna", "Max", "Bella", "Charlie", "Rocky", "Sasha"]
mascotas.remove("Max")  # Elimina "Max" de la lista.
print(mascotas)

# Ejercicio 30: Crear una lista con los números del 1 al 20 y utilizar el método .sort(reverse=True) para ordenarla de forma descendente.
numeros = list(range(1, 21))  # Lista del 1 al 20.
numeros.sort(reverse=True)  # Ordena de forma descendente.
print(numeros)

# Ejercicio 31: Crear una lista con los nombres de 4 libros favoritos y utilizar el método .append() para agregar un nuevo libro al final de la lista.
libros = ["Cien años de soledad", "Don Quijote", "1984", "El principito"]
libros.append("La Odisea")  # Agrega un nuevo libro.
print(libros)

# Ejercicio 32: Crear una lista con los números del 1 al 15 y utilizar una comprensión de listas para crear una nueva lista con los números impares.
numeros = list(range(1, 16))  # Lista del 1 al 15.
impares = [x for x in numeros if x % 2 != 0]  # Filtra números impares.
print(impares)

# Ejercicio 33: Crear una lista con los nombres de 7 comidas favoritas y utilizar el método .insert() para agregar una nueva comida en la posición 3.
comidas = ["Arepas", "Bandeja Paisa", "Sancocho", "Tamales", "Empanadas", "Lechona", "Chorizo"]
comidas.insert(3, "Ajiaco")  # Inserta una comida en la posición 3.
print(comidas)

# Ejercicio 34: Crear una lista con los números del 1 al 10 y utilizar el método .extend() para agregar una segunda lista con los números del 11 al 15.
numeros = list(range(1, 11))  # Lista del 1 al 10.
numeros.extend(range(11, 16))  # Agrega los números del 11 al 15.
print(numeros)
# Ejercicio 35: Crear una lista con los nombres de 6 compañeros y utilizar el método .count() para contar cuántas veces aparece un nombre específico en la lista.
compañeros = ["Juan", "María", "Luis", "Ana", "Luis", "Pedro"]
print(compañeros.count("Luis"))  # Cuenta cuántas veces aparece "Luis".

# Ejercicio 36: Crear una lista con los números del 1 al 12 y utilizar una comprensión de listas para crear una nueva lista con los números divisibles por 3.
numeros = list(range(1, 13))  # Lista del 1 al 12.
divisibles_por_3 = [x for x in numeros if x % 3 == 0]  # Filtra divisibles por 3.
print(divisibles_por_3)

# Ejercicio 37: Crear una lista con los nombres de 5 artistas musicales favoritos y utilizar el método .reverse() para invertir el orden de la lista.
artistas = ["Shakira", "Juanes", "Karol G", "Maluma", "J Balvin"]
artistas.reverse()  # Invierte el orden de la lista.
print(artistas)

# Ejercicio 38: Crear una lista con los números del 1 al 20 y utilizar una función lambda y el método .sort() para ordenar la lista de forma descendente.
numeros = list(range(1, 21))  # Lista del 1 al 20.
numeros.sort(key=lambda x: -x)  # Ordena de forma descendente usando lambda.
print(numeros)

# Ejercicio 39: Crear una lista con las materias de la universidad y utilizar el método .pop() para eliminar y obtener el último elemento de la lista.
materias = ["Matemáticas", "Física", "Programación", "Historia", "Arte"]
ultima_materia = materias.pop()  # Elimina y guarda el último elemento.
print(ultima_materia)  # Muestra la materia eliminada.
print(materias)  # Muestra la lista actualizada.

# Ejercicio 40: Crear una lista con los números del 1 al 25 y utilizar una comprensión de listas para crear una nueva lista con los números múltiplos de 5.
numeros = list(range(1, 26))  # Lista del 1 al 25.
multiplos_de_5 = [x for x in numeros if x % 5 == 0]  # Filtra múltiplos de 5.
print(multiplos_de_5)

# Ejercicio 41: Crear una lista con los nombres de 8 deportes y utilizar una función anónima y el método .sort() para ordenar la lista.
deportes = ["Fútbol", "Baloncesto", "Tenis", "Voleibol", "Natación", "Béisbol", "Atletismo", "Ciclismo"]
deportes.sort(key=lambda deporte: deporte)  # Ordena alfabéticamente usando una función lambda.
print(deportes)

# Ejercicio 42: Crear una lista con los números del 1 al 15 y utilizar el método .clear() para eliminar todos los elementos de la lista.
numeros = list(range(1, 16))  # Lista del 1 al 15.
numeros.clear()  # Elimina todos los elementos.
print(numeros)  # Muestra la lista vacía.

# Ejercicio 43: Crear una lista con los nombres de 6 países y utilizar un bucle for para imprimir cada nombre en minúsculas.
paises = ["Colombia", "Argentina", "Brasil", "Chile", "Perú", "México"]
for pais in paises:  # Recorre cada país.
    print(pais.lower())  # Imprime el nombre en minúsculas.

# Ejercicio 44: Crear una lista con los números del 1 al 20 y utilizar una comprensión de listas para crear una nueva lista con los cuadrados de los números pares.
numeros = list(range(1, 21))  # Lista del 1 al 20.
cuadrados_pares = [x**2 for x in numeros if x % 2 == 0]  # Calcula cuadrados de números pares.
print(cuadrados_pares)

# Ejercicio 45: Crear una lista con los nombres de 10 videojuegos y utilizar el método .index() para obtener el índice de un juego específico.
videojuegos = ["Minecraft", "FIFA", "Call of Duty", "Fortnite", "Valorant", "Among Us", "The Sims", "GTA V", "PUBG", "Zelda"]
print(videojuegos.index("Fortnite"))  # Obtiene el índice de "Fortnite".

# Ejercicio 46: Crear una lista con los números del 1 al 12 y utilizar el método .remove() para eliminar un número específico de la lista.
numeros = list(range(1, 13))  # Lista del 1 al 12.
numeros.remove(6)  # Elimina el número 6.
print(numeros)

# Ejercicio 47: Crear una lista con los nombres de 7 monumentos colombianos y utilizar una función lambda y el método .sort(key=len) para ordenar la lista por longitud de nombre.
monumentos = ["La Candelaria", "El Peñol", "Cristo Rey", "Monserrate", "Ciudad Perdida", "Parque Tayrona", "Santuario de Las Lajas"]
monumentos.sort(key=lambda m: len(m))  # Ordena por longitud de nombre.
print(monumentos)

# Ejercicio 48: Crear una lista con los números del 1 al 18 y utilizar una comprensión de listas para crear una nueva lista con los números múltiplos de 3 y 5.
numeros = list(range(1, 19))  # Lista del 1 al 18.
multiplos_3_5 = [x for x in numeros if x % 3 == 0 and x % 5 == 0]  # Filtra múltiplos de 3 y 5.
print(multiplos_3_5)

# Ejercicio 49: Crear una lista con los nombres de 6 asignaturas que le parecen interesantes de la carrera y utilizar el método .append() para agregar un nuevo nombre al final de la lista.
asignaturas = ["Algoritmos", "Base de Datos", "Redes", "Seguridad Informática", "Inteligencia Artificial", "Machine Learning"]
asignaturas.append("Ciencia de Datos")  # Agrega una nueva asignatura.
print(asignaturas)

# Ejercicio 50: Crear una lista con los números del 1 al 25 y utilizar el método .pop() para eliminar y obtener el elemento de la posición 7.
numeros = list(range(1, 26))  # Lista del 1 al 25.
elemento_eliminado = numeros.pop(7)  # Elimina y guarda el elemento de la posición 7.
print(elemento_eliminado)  # Muestra el elemento eliminado.
print(numeros)  # Muestra la lista actualizada.

