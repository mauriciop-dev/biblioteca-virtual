# main.py
from models.library import Library
from models.book import Book
from models.user import User

def menu():
    print("\n=== Biblioteca Virtual ===")
    print("1. Registrar usuario")
    print("2. Agregar libro")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Mostrar libros disponibles")
    print("6. Mostrar libros prestados")
    print("0. Salir")

if __name__ == "__main__":
    biblioteca = Library("Biblioteca ProDig")

    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del usuario: ")
            usuario = User(nombre)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "2":
            titulo = input("Título del libro: ")
            autor = input("Autor: ")
            libro = Book(titulo, autor)
            biblioteca.agregar_libro(libro)

        elif opcion == "3":
            nombre_usuario = input("Nombre del usuario: ")
            titulo_libro = input("Título del libro: ")
            biblioteca.prestar_libro(nombre_usuario, titulo_libro)

        elif opcion == "4":
            nombre_usuario = input("Nombre del usuario: ")
            titulo_libro = input("Título del libro: ")
            biblioteca.devolver_libro(nombre_usuario, titulo_libro)

        elif opcion == "5":
            biblioteca.mostrar_disponibles()

        elif opcion == "6":
            biblioteca.mostrar_prestados()

        elif opcion == "0":
            print("Gracias por usar la biblioteca virtual.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
