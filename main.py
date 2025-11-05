import os

class Hashtable:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def funcion_hash(self, codigo):
        suma_ascii = sum(int(char) for char in codigo if char.isdigit())
        return suma_ascii % 10

    def agregar(self, codigo, value):
        index = self.funcion_hash(codigo)
        self.buckets[index].append((codigo, value))

    def editar(self, codigo):
        os.system('cls')
        index = self.funcion_hash(codigo)
        bucket = self.buckets[index]
        for valor, (valor_hash, nombre) in enumerate(bucket):
            if valor_hash == codigo:
                print(f"\nProducto: {nombre['titulo']}")
                print("Campos disponibles para editar:")
                for key in nombre.keys():
                    if key != "codigo":
                        print(f"- {key}")
                campo = input("\nIngrese el nombre del campo que desea modificar: ").strip().lower()
                if campo in nombre:
                    if campo in ["stock", "precio"]:
                        while True:
                            nuevo_valor = input(f"Ingrese el nuevo valor para '{campo}': ").strip()

                            if nuevo_valor.isdigit():
                                if campo == "stock":
                                    nombre[campo] = int(nuevo_valor)
                                    
                                else:
                                    nombre[campo] = f"${nuevo_valor}"
                                
                                break
                            else:
                                print("El stock debe ser un número entero.")
                          
                              
                                    
                               
                    else:
                        nuevo_valor = input(f"Ingrese el nuevo valor para '{campo}': ")
                        nombre[campo] = nuevo_valor
                    bucket[valor] = (codigo, nombre)
                    print("\nProducto actualizado correctamente.")
                else:
                    print("\nCampo no válido.")
                return
        print("\nEl código ingresado no existe.")

    
    def eliminar(self, codigo):
        index = self.funcion_hash(codigo)
        bucket = self.buckets[index]
        for valor, (valor_hash, nombre) in enumerate(bucket):
            if valor_hash == codigo:
                del bucket[valor]
                return nombre

    def mostrar_productos(self):
        productos_mostrados = False
        for bucket in self.buckets:
            for codigo, datos in bucket:
                print(f"Título: {datos['titulo']}")
                print(f"Codigo: {codigo}")
                print(f"Género: {datos['genero']}")
                print(f"Tipo: {datos['tipo']}")
                print(f"Editorial: {datos['editorial']}")
                print(f"Alineación: {datos['alineacion']}")
                print(f"Personaje/Equipo: {datos['personaje_equipo']}")
                print(f"Stock: {datos['stock']}")
                print(f"Precio: {datos['precio']}")
                print("-----------------------------\n")
                productos_mostrados = True
        if not productos_mostrados:
            print("No hay productos cargados.")

catalogo_productos = [
    {
        "codigo": "C001",
        "tipo": "cómic",
        "editorial": "DC Comics",
        "genero": "Acción",
        "alineacion": "Héroe",
        "personaje_equipo": "Batman",
        "titulo": "Batman: Año Uno",
        "stock": 10,
        "precio": "$1500"
    },
    {
        "codigo": "C002",
        "tipo": "cómic",
        "editorial": "Marvel Comics",
        "genero": "Aventura",
        "alineacion": "Héroe",
        "personaje_equipo": "Spider-Man",
        "titulo": "The Amazing Spider-Man #1",
        "stock": 7,
        "precio": "$1800"
    },
    {
        "codigo": "M001",
        "tipo": "manga",
        "editorial": "Shueisha",
        "genero": "Acción",
        "alineacion": "Héroe",
        "personaje_equipo": "Goku",
        "titulo": "Dragon Ball Vol. 1",
        "stock": 15,
        "precio": "$2200"
    },
    {
        "codigo": "M002",
        "tipo": "manga",
        "editorial": "Shueisha",
        "genero": "Aventura",
        "alineacion": "Héroes",
        "personaje_equipo": "Luffy y Sombrero de Paja",
        "titulo": "One Piece Vol. 1",
        "stock": 12,
        "precio": "$2100"
    }
]

def menu():
    os.system('cls')
    while True:
        opciones = {
            "1": mostrar_catalogo,
            "2": eliminar_producto,
            "3": actualizar_info,
            "4": realizar_pedido
        }

        print("=== Catálogo de Cómics y Manga ===")
        print("1. Ver el catálogo de productos")
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
    os.system("cls")
    print("\n--- Catálogo de Productos ---")
    tabla.mostrar_productos()

    input("Presione Enter para continuar...")


def eliminar_producto():
    os.system("cls")
    codigo = input("Escriba el código del producto: ")
    nombre = tabla.eliminar(codigo)
    if nombre:
        print(f"\nSe ha eliminado {nombre['titulo']} correctamente.")
    else:
        print("\nEl código no existe o es incorrecto.")

    print("-----------------------------\n")
    input("Presione Enter para continuar...")


def actualizar_info():
    os.system("cls")
    codigo = input("Ingrese el código del producto a editar: ")
    tabla.editar(codigo)
    
    print("-----------------------------\n")
    input("Presione Enter para continuar...")


def realizar_pedido():
    pass

tabla = Hashtable()
for producto in catalogo_productos:
    tabla.agregar(producto["codigo"], producto)

menu()
