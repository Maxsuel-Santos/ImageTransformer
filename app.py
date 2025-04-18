import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Funçoes para ler imagem (PBM, PNG, JPG, JPEG)
def imagem_para_matriz(imagem_pil, tipo):
    if tipo == 'pbm':
        img = imagem_pil.convert('1')  # Preto e branco
        matriz = np.array(img, dtype=int)
        return 1 - matriz
    else:
        img = imagem_pil.convert('RGB')  # Colorido
        return np.array(img)

# Funções de transformação
def rotacionar_matriz(matriz, angulo):
    if angulo == 90:
        return np.rot90(matriz, k=3)
    elif angulo == 180:
        return np.rot90(matriz, k=2)
    elif angulo == 270:
        return np.rot90(matriz, k=1)
    return matriz

def espelhar_horizontal(matriz):
    return np.fliplr(matriz)

def espelhar_vertical(matriz):
    return np.flipud(matriz)

st.title("Visualizador de Imagens com Transformações")

# Upload
arquivo = st.file_uploader("📂 Envie uma imagem (PBM, PNG, JPG, JPEG)", type=["pbm", "png", "jpg", "jpeg"])

if arquivo:
    extensao = arquivo.name.split(".")[-1].lower()
    tipo = 'pbm' if extensao == 'pbm' else 'colorida'
    
    imagem = Image.open(arquivo)
    matriz = imagem_para_matriz(imagem, tipo)

    matrizes = [
        matriz,
        rotacionar_matriz(matriz, 90),
        rotacionar_matriz(matriz, 180),
        rotacionar_matriz(matriz, 270),
        espelhar_horizontal(matriz),
        espelhar_vertical(matriz)
    ]

    titulos = ['Original', '90°', '180°', '270°', 'Espelho H', 'Espelho V']

    # Exibição
    st.subheader("Transformações:")

    colunas = st.columns(len(matrizes))
    for i in range(len(matrizes)):
        with colunas[i]:
            fig, ax = plt.subplots()
            if tipo == 'pbm':
                ax.imshow(matrizes[i], cmap='gray', vmin=0, vmax=1)
            else:
                ax.imshow(matrizes[i])
            ax.axis('off')
            ax.set_title(titulos[i])
            st.pyplot(fig)
