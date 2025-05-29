# models/book.py
class Book:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False

    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"{self.titulo} por {self.autor} - {estado}"

    def prestar(self):
        self.prestado = True

    def devolver(self):
        self.prestado = False
