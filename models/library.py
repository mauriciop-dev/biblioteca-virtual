# models/library.py
class Library:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.usuarios = {}

    def registrar_usuario(self, usuario):
        if usuario.nombre not in self.usuarios:
            self.usuarios[usuario.nombre] = usuario
            print(f"Usuario '{usuario.nombre}' registrado correctamente.")
        else:
            print("Ese usuario ya existe.")

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def prestar_libro(self, nombre_usuario, titulo_libro):
        usuario = self.usuarios.get(nombre_usuario)
        if not usuario:
            print("Usuario no registrado.")
            return
        for libro in self.libros:
            if libro.titulo == titulo_libro and not libro.prestado:
                libro.prestar()
                usuario.prestar_libro(libro)
                print(f"Libro '{titulo_libro}' prestado a {nombre_usuario}.")
                return
        print("Libro no disponible o ya prestado.")

    def devolver_libro(self, nombre_usuario, titulo_libro):
        usuario = self.usuarios.get(nombre_usuario)
        if not usuario:
            print("Usuario no registrado.")
            return
        for libro in usuario.libros_prestados:
            if libro.titulo == titulo_libro:
                libro.devolver()
                usuario.devolver_libro(titulo_libro)
                print(f"Libro '{titulo_libro}' devuelto por {nombre_usuario}.")
                return
        print("Ese libro no está prestado a este usuario.")

    def mostrar_disponibles(self):
        disponibles = [libro for libro in self.libros if not libro.prestado]
        if disponibles:
            print("\nLibros disponibles:")
            for libro in disponibles:
                print(libro)
        else:
            print("No hay libros disponibles.")

    def mostrar_prestados(self):
        prestados = [libro for libro in self.libros if libro.prestado]
        if prestados:
            print("\nLibros prestados:")
            for libro in prestados:
                print(libro)
        else:
            print("No hay libros prestados.")
