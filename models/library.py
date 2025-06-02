import json
import os
from models.book import Book
from models.user import User

class Library:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.usuarios = {}

    def _cargar_o_crear_archivo(self, ruta):
        """Helper para manejar archivos."""
        if not os.path.exists(ruta):
            with open(ruta, "w", encoding="utf-8") as f:
                json.dump([] if "libros" in ruta else {}, f)
        return open(ruta, "r+", encoding="utf-8")

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

    def guardar_datos(self, ruta_usuarios="usuarios.json", ruta_libros="libros.json"):
        with self._cargar_o_crear_archivo(ruta_usuarios) as f:
            json.dump({u: [l.titulo for l in usr.libros_prestados] for u, usr in self.usuarios.items()}, f)

        with self._cargar_o_crear_archivo(ruta_libros) as f:
            json.dump([{"titulo": l.titulo, "autor": l.autor, "prestado": l.prestado} for l in self.libros], f)

    def cargar_datos(self, ruta_usuarios="usuarios.json", ruta_libros="libros.json"):
        try:
            with self._cargar_o_crear_archivo(ruta_usuarios) as f:
                usuarios_data = json.load(f)
                for nombre, libros in usuarios_data.items():
                    if nombre not in self.usuarios:
                        self.usuarios[nombre] = User(nombre)
        except json.JSONDecodeError:
            pass

        try:
            with self._cargar_o_crear_archivo(ruta_libros) as f:
                libros_data = json.load(f)
                for l in libros_data:
                    libro = Book(l["titulo"], l["autor"])
                    libro.prestado = l["prestado"]
                    self.libros.append(libro)
        except json.JSONDecodeError:
            pass