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
                                print("El valor debe ser un número.")
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



class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, element):
        self.stack.append(element)
        if len(self.stack) > 5:
            self.stack.pop(0)
    def mostrar(self):
        if not self.stack:
            print("No hay productos vistos recientemente.")
        else:
            print("\n--- Últimos productos vistos ---")
            for item in reversed(self.stack):
                print(f"- {item}")

class Queue:
    def __init__(self):
        self.queue = []
    def agregar_pedido(self, element):
        self.queue.append(element)
    def eliminar_pedidos(self):
        while self.queue:
            pedido = self.queue.pop(0)
            print(f"Pedido de '{pedido}' procesado.")
    def peek(self):
        if not self.queue:
            print("No hay pedidos en espera.")
        else:
            print("\n--- Pedidos pendientes ---")
            for pedido in self.queue:
                print(f"- {pedido}")



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
            "4": realizar_pedido,
            "5": pedidos
        }

        print("=== Catálogo de Cómics y Manga ===")
        print("1. Ver el catálogo de productos")
        print("2. Buscar por código y eliminar producto")
        print("3. Actualizar información de un producto")
        print("4. Realizar un pedido")
        print("5. Ver y procesar pedidos")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "6":
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
    historial.mostrar()
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
    os.system("cls")

    # árbol de categorías
    root = TreeNode("Categorías")
    comics = TreeNode("Cómics")
    manga = TreeNode("Manga")
    dc = TreeNode("DC Comics")
    marvel = TreeNode("Marvel Comics")
    shueisha = TreeNode("Shueisha")
    batman = TreeNode("Batman")
    spiderman = TreeNode("Spider-Man")
    goku = TreeNode("Goku")
    luffy = TreeNode("Luffy")

    root.left = comics
    root.right = manga

    comics.left = dc
    comics.right = marvel
    manga.left = shueisha

    dc.left = batman
    marvel.left = spiderman
    shueisha.left = goku
    shueisha.right = luffy

    actual = root
    while True:
        os.system("cls")
        print(f"\nEstás en: {actual.data}")
        if actual.left or actual.right:
            if actual.left: print(f"1. {actual.left.data}")
            if actual.right: print(f"2. {actual.right.data}")
            print("3. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1" and actual.left:
                actual = actual.left
            elif opcion == "2" and actual.right:
                actual = actual.right
            elif opcion == "3":
                return
            else:
                print("Opción inválida.")
                input("Enter para continuar...")
        else:
            os.system("cls")
            print(f"\n--- Producto seleccionado: {actual.data} ---")

            # Buscar producto correspondiente
            for codigo, datos in [(p["codigo"], p) for b in tabla.buckets for p in [b[i][1] for i in range(len(b))]]:
                if datos["personaje_equipo"].lower().startswith(actual.data.lower()):
                    print(f"Título: {datos['titulo']}")
                    print(f"Precio: {datos['precio']}")
                    historial.push(datos['titulo'])
                    break

            print("\n1. Realizar pedido")
            print("2. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                cola_pedidos.agregar_pedido(datos['titulo'])
                print(f"\nPedido de '{datos['titulo']}' agregado correctamente.")
                input("Presione Enter para continuar...")
                return
            elif opcion == "2":
                return
            else:
                print("Opción inválida.")
                input("Presione Enter para continuar...")


def pedidos():
    os.system("cls")
    print("--- Pedidos actuales ---")
    cola_pedidos.peek()
    print("\n1. Procesar pedidos")
    print("2. Volver al menú")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        cola_pedidos.eliminar_pedidos()
        input("Presione Enter para continuar...")



tabla = Hashtable()
for producto in catalogo_productos:
    tabla.agregar(producto["codigo"], producto)

historial = Stack()
cola_pedidos = Queue()

menu()
