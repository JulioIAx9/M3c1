nombres = [
    "Harry Houdini",
    "Newton",
    "David Blaine",
    "Hawking",
    "Messi",
    "Teller",
    "Einstein",
    "Pele",
    "Juanes"
]

otros = []  # Lista para almacenar los nombres que no son magos ni científicos

def hacer_grandioso(nombre):
    """
    Agrega 'El gran' antes del nombre proporcionado.
    """
    return "El gran " + nombre

def imprimir_nombres(titulo, lista):
    """
    Imprime el nombre de cada persona en la lista proporcionada.
    """
    print(titulo)
    for nombre in lista:
        print(nombre)

# Definir lista de magos y científicos
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]

# Crear lista de magos grandiosos
magos_grandiosos = [hacer_grandioso(mago) for mago in magos]

# Separar los nombres en grupos y añadir a la lista "otros" si no son magos ni científicos
for nombre in nombres:
    if nombre in magos:
        continue
    elif nombre in cientificos:
        continue
    else:
        otros.append(nombre)

# Imprimir los nombres en cada categoría antes de ser modificados
imprimir_nombres("Lista completa de nombres:", nombres)

# Imprimir los nombres de los magos grandiosos
imprimir_nombres("\nNombres de los magos grandiosos:", magos_grandiosos)

# Imprimir los nombres de los científicos
imprimir_nombres("\nNombres de los científicos:", cientificos)

# Imprimir la lista de otros nombres
imprimir_nombres("\nLista de otros nombres:", otros)
