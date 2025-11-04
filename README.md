# TP---Final---Algoritmos

#  Tienda Online “Nadie se salva solo”  
**Trabajo Práctico Final N°5 - Laboratorio de Algoritmos y Estructuras de Datos**

---

##  Descripción del proyecto

Este proyecto implementa el **núcleo lógico (backend)** de una tienda online de cómics llamada *“Nadie se salva solo”*.  
El objetivo es simular el funcionamiento interno del sistema sin necesidad de una interfaz gráfica.  
El sistema permite:

- Gestionar productos del inventario.  
- Procesar pedidos de clientes en el orden de llegada.  
- Mantener un historial de los últimos productos vistos.  
- Organizar los productos en una jerarquía de categorías.

Todas estas funcionalidades se desarrollaron aplicando estructuras de datos eficientes y adecuadas para cada caso, según lo aprendido en la materia y lo recomendado por la página [W3Schools - Data Structures](https://www.w3schools.com/dsa/).

---

##  Instrucciones de ejecución

1. Clonar el repositorio:  
   ```bash
   git clone https://github.com/mateodelucca/TP-final-Algoritmos.git
   cd TP-final-Algoritmos

2. Ejecutar el programa principal:  
   ```bash
   python main.py


##  Decisiones de diseño

### 1. Gestión de productos → **Hash Table**
**Estructura:** Diccionario o tabla hash.  
**Justificación:**  
Cada producto posee un código único. Las tablas hash permiten **accesos, inserciones y eliminaciones en tiempo O(1)** promedio, lo cual es ideal para búsquedas rápidas por código.

---

### 2. Procesamiento de pedidos → **Queue (Cola)**
**Estructura:** Cola implementada con una lista enlazada o `collections.deque`.  
**Justificación:**  
Los pedidos deben procesarse **en el orden en que llegan (FIFO: First In, First Out)**.  
Las colas garantizan que el primer pedido en entrar sea el primero en salir, representando fielmente el flujo real de atención al cliente.

---

### 3. Historial de productos vistos → **Stack (Pila)**
**Estructura:** Pila implementada con lista o estructura propia.  
**Justificación:**  
El historial mantiene solo los **últimos 5 productos** vistos.  
Una pila permite **apilar y desapilar** elementos fácilmente.  
Si la pila alcanza su límite, se elimina el más antiguo antes de agregar uno nuevo, manteniendo la lógica **LIFO (Last In, First Out)**.

---

### 4. Categorización jerárquica → **Tree (Árbol)**
**Estructura:** Árbol general (cada nodo puede tener varios hijos).  
**Justificación:**  
Los productos se organizan jerárquicamente (por ejemplo: *Cómics → DC → Batman*).  
El árbol permite **recorrer categorías y subcategorías** de manera eficiente, mostrando todos los productos que pertenezcan a una rama determinada.


## 📚 Bibliografía

- [W3Schools - Data Structures and Algorithms](https://www.w3schools.com/dsa/)

