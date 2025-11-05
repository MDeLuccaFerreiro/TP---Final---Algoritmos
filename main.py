import os, time

class Hashtable:
    def __init__(self, size=10): #tamaño 10 porque para armar el hash lo voy a hacer con modulo 10, por lo que solo pueden dar 10 valores max
        self.size = size
        self.buckets = [[] for _ in range(size)]  #dentro de cada valor se necesitan listas por si hay dos comics con mismo hash

    def funcion_hash(self, codigo):
        suma_ascii = sum(int(char) for char in codigo if char.isdigit())
        return suma_ascii % 10

    def agregar_y_editar(self, codigo, value):
        index = self.funcion_hash(codigo)
        bucket = self.buckets[index]
        for valor, valor_hash in enumerate(bucket):
            if valor_hash == codigo:
                bucket[valor] = (codigo, value)  
                return
        bucket.append((codigo, value)) 

    def obtener_valor(self, codigo):   
        index = self.funcion_hash(codigo)
        bucket = self.buckets[index]
        for valor_hash, nombre in bucket:
            if valor_hash == codigo:
                return nombre
        return None  

    def eliminar(self, codigo):
        index = self.funcion_hash(codigo)
        bucket = self.buckets[index]
        for valor, (valor_hash, nombre) in enumerate(bucket):
            if valor_hash == codigo:
                del bucket[valor]
                return nombre

    def mostrar_productos(self):
        for bucket in self.buckets:
            for codigo, datos in bucket:
                print(f"Codigo: {codigo}")
                print(f"Título: {datos['titulo']}")
                print(f"Género: {datos['genero']}")
                print(f"Tipo: {datos['tipo']}")
                print(f"Editorial: {datos['editorial']}")
                print(f"Alineación: {datos['alineacion']}")
                print(f"Personaje/Equipo: {datos['personaje_equipo']}")
                print("-----------------------------")

catalogo_productos = [
    {
        "codigo": "C001",
        "tipo": "cómic",
        "editorial": "DC Comics",
        "genero": "Acción",
        "alineacion": "Héroe",
        "personaje_equipo": "Batman",
        "titulo": "Batman: Año Uno"
    },
    {
        "codigo": "C002",
        "tipo": "cómic",
        "editorial": "Marvel Comics",
        "genero": "Aventura",
        "alineacion": "Héroe",
        "personaje_equipo": "Spider-Man",
        "titulo": "The Amazing Spider-Man #1"
    },
    {
        "codigo": "C003",
        "tipo": "cómic",
        "editorial": "DC Comics",
        "genero": "Fantasía",
        "alineacion": "Héroe",
        "personaje_equipo": "Wonder Woman",
        "titulo": "Wonder Woman: Renacimiento"
    },
    {
        "codigo": "C004",
        "tipo": "cómic",
        "editorial": "Marvel Comics",
        "genero": "Ciencia Ficción",
        "alineacion": "Héroes",
        "personaje_equipo": "Los Vengadores",
        "titulo": "Avengers: La Era de Ultrón"
    },
    {
        "codigo": "M001",
        "tipo": "manga",
        "editorial": "Shueisha",
        "genero": "Acción",
        "alineacion": "Héroe",
        "personaje_equipo": "Goku",
        "titulo": "Dragon Ball Vol. 1"
    },
    {
        "codigo": "M002",
        "tipo": "manga",
        "editorial": "Shueisha",
        "genero": "Aventura",
        "alineacion": "Héroes",
        "personaje_equipo": "Luffy y Sombrero de Paja",
        "titulo": "One Piece Vol. 1"
    },
    {
        "codigo": "M003",
        "tipo": "manga",
        "editorial": "Kodansha",
        "genero": "Acción",
        "alineacion": "Neutral",
        "personaje_equipo": "Eren Yeager",
        "titulo": "Attack on Titan Vol. 1"
    },
    {
        "codigo": "M004",
        "tipo": "manga",
        "editorial": "Shueisha",
        "genero": "Aventura",
        "alineacion": "Héroe",
        "personaje_equipo": "Naruto Uzumaki",
        "titulo": "Naruto Vol. 1"
    },
    {
        "codigo": "C005",
        "tipo": "cómic",
        "editorial": "Image Comics",
        "genero": "Acción / Fantasía",
        "alineacion": "Anti-héroe",
        "personaje_equipo": "Spawn",
        "titulo": "Spawn #1"
    },
    {
        "codigo": "M005",
        "tipo": "manga",
        "editorial": "VIZ Media",
        "genero": "Acción / Misterio",
        "alineacion": "Neutral",
        "personaje_equipo": "Light Yagami",
        "titulo": "Death Note Vol. 1"
    }

]

def menu():
    os.system ("cls")
    while True:
        opciones = {
        "1": mostrar_catalogo,
        "2": eliminar_producto,
        "3": actualizar_info,
        "4": realizar_pedido
        }

        print("=== Catálogo de Cómics y Manga ===")
        print("1. Ver el catalogo de productos")
        print("2. Buscar por código y eliminar producto")
        print("3. Actualizar información de un producto")
        print("4. Realizar un pedido")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == str(len(opciones) + 1):
            print("Saliendo del programa...")
            break
        elif opcion in opciones:
            opciones[opcion]()
        else:
            print("\nOpción inválida. Intente de nuevo.")
            input("Presione Enter para continuar...")

    

def mostrar_catalogo():
    os.system ("cls")
    print("\n--- Catálogo de Productos ---")
    tabla.mostrar_productos()
    input("Presione Enter para continuar...") 

def eliminar_producto():
    os.system ("cls")
    codigo = input("Escriba el código del producto: ")
    nombre = tabla.eliminar(codigo)

    if nombre: #si encuentra el producto
        print(f"\nSe ha eliminado {nombre['titulo']} correctamente.")

    else:
    
        print("\nEl código no existe o es incorrecto.")

    print("-----------------------------\n")
    input("Presione Enter para continuar...") 

def actualizar_info():
    pass

def realizar_pedido():
    pass

tabla = Hashtable()

for producto in catalogo_productos:
   tabla.agregar_y_editar(producto["codigo"], producto)

menu()