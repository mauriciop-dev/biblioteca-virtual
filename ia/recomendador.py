from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RecomendadorLibros:
    def __init__(self, libros):
        self.vectorizer = TfidfVectorizer()
        self.libros = libros
        self.matriz = self._entrenar()  # Corregido "matrix" → "matriz"

    def _entrenar(self):
        textos = [f"{l.titulo} {l.autor}" for l in self.libros]  # Corregido "1" → "l" y "title" → "titulo"
        return self.vectorizer.fit_transform(textos)

    def recomendar(self, libro_id, n=3):
        similitudes = cosine_similarity(self.matriz[libro_id], self.matriz)  # Añadido parámetro faltante
        indices = similitudes.argsort()[0][-n-1:-1][::-1]  # Corregido [:-1] → [::-1]
        return [self.libros[i] for i in indices]