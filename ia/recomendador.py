from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RecomendadorLibros:
    def __init__(self, libros):
        self.vectorizer = TfidfVectorizer()
        self.libros = libros
        self.matriz = self._entrenar()

    def _entrenar(self):
        textos = [f"{libro.titulo} {libro.autor}" for libro in self.libros]
        return self.vectorizer.fit_transform(textos)

    def recomendar(self, libro_id, n=3):
        similitudes = cosine_similarity(self.matriz[libro_id:libro_id+1], self.matriz).flatten()
        indices = similitudes.argsort()[-n-1:-1][::-1]
        return [self.libros[i] for i in indices if i != libro_id]