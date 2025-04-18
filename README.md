# 🖼️ Visualizador e Transformador de Imagens com Streamlit

Este aplicativo web foi desenvolvido usando **Streamlit** e permite **carregar imagens** nos formatos **PBM, PNG, JPG ou JPEG**, aplicar transformações visuais e **visualizar os resultados diretamente no navegador**.

---

## ✨ Funcionalidades

- 📂 **Upload de Imagens** (`.pbm`, `.png`, `.jpg`, `.jpeg`)
- 🔄 **Transformações disponíveis:**
  - Rotação de 90°, 180° e 270°
  - Espelhamento horizontal
  - Espelhamento vertical
- 👁️ Visualização em galeria lado a lado
- 🖤 Suporte para imagens PBM com inversão automática de cores
- 🌈 Suporte completo a imagens coloridas

---

## 🧠 Como funciona?

- Se a imagem enviada for `.pbm`, ela será tratada como **preto e branco binária** (0 = branco, 1 = preto).
- Se for qualquer outro formato, a imagem é convertida para RGB e exibida **colorida**.
- As transformações são feitas com **NumPy** e exibidas com **Matplotlib** embutido no Streamlit.

---

## 🚀 Como executar localmente

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Crie e ative um ambiente virtual (opcional mas recomendado):

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o aplicativo:

```bash
streamlit run app_imagem_transformada.py
```

---

## 🧾 Requisitos

O arquivo `requirements.txt` deve conter:

```
streamlit
pillow
numpy
matplotlib
```

---

## 🛠️ Tecnologias utilizadas

- [Streamlit](https://streamlit.io)
- [Pillow (PIL)](https://pillow.readthedocs.io/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

---

## 📄 Licença

Este projeto é de código aberto, sob a licença MIT. Sinta-se livre para usar, modificar e contribuir!

