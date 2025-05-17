"""Matrices en Juegos y Imágenes con Python"""
"""
 Las matrices son estructuras de datos bidimensionales que se utilizan para representar imágenes, gráficos y otros tipos de datos en dos dimensiones
 En Python, las matrices se pueden representar como listas de listas
 Las matrices se utilizan en juegos para representar el estado del juego, como el tablero de un juego de mesa, el mapa de un juego de aventuras, etc.
 En imágenes, las matrices se utilizan para representar los píxeles de una imagen, donde cada elemento de la matriz representa un píxel y su valor representa el color del píxel
 Las matrices se pueden manipular utilizando operaciones matemáticas y funciones de Python, como la biblioteca NumPy, que proporciona una forma eficiente de trabajar con matrices y realizar operaciones matemáticas en ellas
 Las matrices se pueden utilizar para realizar operaciones matemáticas, como la suma, resta, multiplicación y división de matrices
 Las matrices se pueden utilizar para realizar operaciones de transformación, como la rotación, escalado y traslación de imágenes
 Las matrices se pueden utilizar para realizar operaciones de filtrado, como el desenfoque, el afilado y la detección de bordes en imágenes
 Las matrices se pueden utilizar para realizar operaciones de convolución, que son utilizadas en el procesamiento de imágenes y en redes neuronales
 Las matrices se pueden utilizar para realizar operaciones de interpolación, que son utilizadas en el procesamiento de imágenes y en gráficos por computadora
 Las matrices se pueden utilizar para realizar operaciones de segmentación, que son utilizadas en el procesamiento de imágenes y en visión por computadora
 Las matrices se pueden utilizar para realizar operaciones de clasificación, que son utilizadas en el aprendizaje automático y en la inteligencia artificial
 Las matrices se pueden utilizar para realizar operaciones de regresión, que son utilizadas en el aprendizaje automático y en la inteligencia artificial
 Las matrices se pueden utilizar para realizar operaciones de agrupamiento, que son utilizadas en el aprendizaje automático y en la inteligencia artificial
 Las matrices se pueden utilizar para realizar operaciones de reducción de dimensionalidad, que son utilizadas en el aprendizaje automático y en la inteligencia artificial
 Las matrices se pueden utilizar para realizar operaciones de optimización, que son utilizadas en el aprendizaje automático y en la inteligencia artificial
 Las matrices se pueden utilizar para realizar operaciones de análisis de datos, que son utilizadas en el aprendizaje automático y en la inteligencia artificial
"""
chess_board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]
# Representación de un tablero de ajedrez
# Las letras minúsculas representan las piezas negras y las mayúsculas representan las piezas blancas
print(chess_board)


image = [
    [255, 0, 0, 0, 255],
    [0, 255, 0, 255, 0],
    [0, 0, 255, 0, 0],
    [0, 255, 0, 255, 0],
    [255, 0, 0, 0, 255]
]

print(image)