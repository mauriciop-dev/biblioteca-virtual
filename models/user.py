# models/user.py
class User:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre}, Libros prestados: {len(self.libros_prestados)}"

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, titulo):
        self.libros_prestados = [l for l in self.libros_prestados if l.titulo != titulo]
