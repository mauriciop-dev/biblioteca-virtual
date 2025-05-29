import streamlit as st
from models.library import Library
from models.book import Book
from models.user import User

st.set_page_config(page_title="Biblioteca ProDig")
st.title("📚 Biblioteca Virtual ProDig")

# Cargar y mantener la biblioteca en sesión
if "biblioteca" not in st.session_state:
    st.session_state.biblioteca = Library("Biblioteca ProDig")
    st.session_state.biblioteca.cargar_datos()

biblioteca = st.session_state.biblioteca

menu = st.sidebar.selectbox("Selecciona una acción:", (
    "Registrar usuario",
    "Agregar libro",
    "Prestar libro",
    "Devolver libro",
    "Ver libros disponibles",
    "Ver libros prestados"
))

if menu == "Registrar usuario":
    nombre = st.text_input("Nombre del usuario")
    if st.button("Registrar"):
        usuario = User(nombre)
        biblioteca.registrar_usuario(usuario)
        biblioteca.guardar_datos()

elif menu == "Agregar libro":
    titulo = st.text_input("Título del libro")
    autor = st.text_input("Autor")
    if st.button("Agregar libro"):
        libro = Book(titulo, autor)
        biblioteca.agregar_libro(libro)
        biblioteca.guardar_datos()

elif menu == "Prestar libro":
    usuario = st.text_input("Nombre del usuario")
    titulo = st.text_input("Título del libro")
    if st.button("Prestar"):
        biblioteca.prestar_libro(usuario, titulo)
        biblioteca.guardar_datos()

elif menu == "Devolver libro":
    usuario = st.text_input("Nombre del usuario")
    titulo = st.text_input("Título del libro")
    if st.button("Devolver"):
        biblioteca.devolver_libro(usuario, titulo)
        biblioteca.guardar_datos()

elif menu == "Ver libros disponibles":
    st.subheader("Libros disponibles")
    disponibles = [str(libro) for libro in biblioteca.libros if not libro.prestado]
    st.write("\n".join(disponibles) if disponibles else "No hay libros disponibles.")

elif menu == "Ver libros prestados":
    st.subheader("Libros prestados")
    prestados = [str(libro) for libro in biblioteca.libros if libro.prestado]
    st.write("\n".join(prestados) if prestados else "No hay libros prestados.")
