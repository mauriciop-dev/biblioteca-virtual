import streamlit as st
from models.library import Library
from models.book import Book
from models.user import User
from ia.recomendador import RecomendadorLibros

# Configuración de la página
st.set_page_config(page_title="Biblioteca ProDig", layout="wide")
st.title("📚 Biblioteca Virtual ProDig")

# Cargar datos
if "biblioteca" not in st.session_state:
    st.session_state.biblioteca = Library("Biblioteca ProDig")
    st.session_state.biblioteca.cargar_datos()
    st.session_state.recomendador = RecomendadorLibros(st.session_state.biblioteca.libros)

biblioteca = st.session_state.biblioteca

# Sidebar
menu = st.sidebar.selectbox("Menú", [
    "Registrar usuario", "Agregar libro", "Prestar libro", 
    "Devolver libro", "Libros disponibles", "Libros prestados", 
    "Recomendaciones IA"
])

# Funciones de visualización
def mostrar_libros(libros, titulo):
    if libros:
        st.subheader(titulo)
        cols = st.columns(3)
        for i, libro in enumerate(libros):
            cols[i % 3].write(f"📖 **{libro.titulo}**\n*{libro.autor}*")
    else:
        st.warning(f"No hay {titulo.lower()}.")

# Lógica del menú
if menu == "Registrar usuario":
    nombre = st.text_input("Nombre del usuario")
    if st.button("Registrar"):
        biblioteca.registrar_usuario(User(nombre))
        biblioteca.guardar_datos()

elif menu == "Agregar libro":
    titulo = st.text_input("Título del libro")
    autor = st.text_input("Autor")
    if st.button("Agregar"):
        biblioteca.agregar_libro(Book(titulo, autor))
        biblioteca.guardar_datos()

elif menu == "Recomendaciones IA":
    if biblioteca.libros:
        libro_elegido = st.selectbox("Selecciona un libro que te guste:", 
                                   [libro.titulo for libro in biblioteca.libros])
        if st.button("Generar recomendaciones"):
            idx = [libro.titulo for libro in biblioteca.libros].index(libro_elegido)
            recomendados = st.session_state.recomendador.recomendar(idx)
            mostrar_libros(recomendados, "Libros recomendados:")
    else:
        st.warning("¡Añade libros primero!")