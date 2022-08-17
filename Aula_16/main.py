from modelos.documentos import Book, Document, EMail
from modelos.plantas import Arvore, Alface

def run_system():
    doc1 = Document()
    doc2 = EMail(to = 'gabricouto@gmail.com', authors=["Jose"])
    doc3 = Book(title = "Design Pattern", authors=["Murilo", "Couto", "Davi", "Golias"])
    print (doc2)
    print(doc3)

if __name__ == "__main__":
    # planta1 = Arvore('Carvalho')
    # planta2 = Alface(nome = 'Hamburguer de siri do futuro')

    # print(planta1.ola())
    # print(planta2.ola())

    run_system()