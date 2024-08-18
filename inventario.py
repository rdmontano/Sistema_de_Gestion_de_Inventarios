class Inventario:
    def __init__(self):
        # Inicializa la lista de productos vacía.
        self.productos = []

    def añadir_producto(self, producto):
        # Verifica si el ID del producto es único antes de añadirlo.
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("-----------------------------------------------\n")
            print("ERROR: EL ID YA EXISTE.")
        else:
            # Si el ID es único, añade el producto al inventario.
            self.productos.append(producto)
            print("-----------------------------------------------\n")
            print("PRODUCTO AÑADIDO CON ÉXITO.")

    def eliminar_producto(self, id):
        # Elimina el producto cuyo ID coincida con el dado.
        self.productos = [p for p in self.productos if p.get_id() != id]
        print("-----------------------------------------------\n")
        print("PRODUCTO ELIMINADO CON ÉXITO.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        # Busca el producto por ID y actualiza su cantidad y/o precio.
        for p in self.productos:
            if p.get_id() == id:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("-----------------------------------------------\n")
                print("PRODUCTO ACTUALIZADO CON ÉXITO.")
                return
        # Si no se encuentra el producto, muestra un mensaje de error.
            print("-----------------------------------------------\n")
            print("ERROR: PRODUCTO NO ENCONTRADO.")

    def buscar_producto(self, nombre):
        # Busca productos cuyo nombre contenga la cadena dada.
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            # Muestra todos los productos que coinciden con la búsqueda.
            for p in resultados:
                print(p)
        else:
            # Si no se encuentra ningún producto, muestra un mensaje.
            print("NO SE ENCONTRARON PRODUCTOS.")

    def mostrar_todos(self):
        # Muestra todos los productos en el inventario.
        if self.productos:
            for p in self.productos:
                print(p)
        else:
            # Si el inventario está vacío, muestra un mensaje.
            print("EL INVENTARIO ESTÁ VACÍO.")
