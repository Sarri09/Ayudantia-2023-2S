import os
import wikipediaapi
import random

def obtener_documentos_wikipedia(cantidad=30):

    wiki_wiki = wikipediaapi.Wikipedia(user_agent='Hadoop familiarization project (vichogk@gmail.com)', language='en')
    
    # Lista de términos de búsqueda relacionados con TI
    terminos_de_busqueda_base = [
        'AI', 'Python', 'Data science', 'Distributed Systems', 'Hadoop',
        'Machine Learning', 'Big Data', 'Cloud Computing', 'Cybersecurity',
        'Blockchain', 'Apache Kafka', 'Redis', 'Natural Language Processing',
        'Internet of Things', 'Automata Computer Sciencie', 'Cache', 'Parallel Computing',
        'Software Development', 'Operating Systems', 'Memory', 'Virtualization',
        'IT Infrastructure', 'Web Development', 'Turing Machine', 'Quantum Computing',
        'File System', 'Software Engeneering', 'Software Architecture', 'APIs', 'Java'
    ]
    
    # Asegurarse de que la cantidad no sea mayor que la longitud de la lista
    cantidad = min(cantidad, len(terminos_de_busqueda_base))

    # Seleccionar aleatoriamente términos de búsqueda
    terminos_de_busqueda = random.sample(terminos_de_busqueda_base, cantidad)

    documentos = []

    for i, termino in enumerate(terminos_de_busqueda, start=1):
        page_py = wiki_wiki.page(termino)
        
        if page_py.exists():
            contenido = page_py.text
            documentos.append(contenido)

            # Nombre del archivo con el número del documento
            nombre_archivo = f"doc{i}.txt"

            # Directorio de destino basado en la posición del documento
            directorio_destino = "carpeta1" if i <= cantidad // 2 else "carpeta2"

            # Ruta completa del archivo de salida
            ruta_archivo = os.path.join(directorio_destino, nombre_archivo)

            # Asegurarse de que el directorio de destino exista
            os.makedirs(directorio_destino, exist_ok=True)

            # Guardar el documento en el archivo correspondiente
            with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
                archivo.write(contenido)

            if i >= cantidad:
                break

    return documentos

documentos = obtener_documentos_wikipedia(cantidad=30)

