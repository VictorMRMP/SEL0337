# SEL0337
uatizap
#!/usr/bin/python3

import cv2 # Biblioteca OpenCV

import os # Biblioteca para operações do sistema

import time # Biblioteca de tempo

from picamera2 import Picamera2 # Biblioteca da câmera da Raspberry Pi

# Carrega o classificador para detecção facial (informar o caminho do arquivo)

face_detector = cv2.CascadeClassifier("/home/sel/haarcascade_frontalface_default.xml")

# Inicia uma thread para gerenciar janelas de visualização

cv2.startWindowThread()

# Inicializa a câmera da Raspberry Pi

picam2 = Picamera2()

# Configura a câmera para criar uma visualização com formato de representação

de cores 32 bits “XRGB8888” e resolução de 640x480 pixels

picam2.configure(picam2.create_preview_configuration(main={"format":

'XRGB8888', "size": (640, 480)})

# Inicia a câmera

picam2.start()

# Define o diretório onde as imagens com rostos detectados serão armazenadas

output_directory = "detected_faces"

# Cria o diretório, se ele não existir

os.makedirs(output_directory, exist_ok=True)

# Loop para captura e detecção de rostos

while True:

# Captura um quadro da câmera e armazena na variável

im = picam2.capture_array()

# Converte a imagem colorida para escala de cinza

grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# Usa o classificador em cascata para detectar rostos na imagem em escala

de cinza

faces = face_detector.detectMultiScale(grey, 1.1, 5)

# Loop para processar cada rosto detectado

for (x, y, w, h) in faces:

# Desenha um retângulo verde ao redor do rosto na imagem original

cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0))

# Gera um nome de arquivo único com base no carimbo de data/hora

timestamp = int(time.time())

filename = os.path.join(output_directory, f"face_{timestamp}.jpg")

# Salva apenas a porção da imagem que contém o rosto detectado como um

arquivo JPEG

cv2.imwrite(filename, im[y:y+h, x:x+w])

# Exibe a imagem com os retângulos desenhados em uma janela com o título

"Camera"

cv2.imshow("Camera", im)

# Aguarda 1 milissegundo antes de continuar o loop e capturar a próxima

imagem

cv2.waitKey(1)
