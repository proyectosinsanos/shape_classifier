
# 🟢 Clasificador de Formas: Círculo vs Cuadrado

Este proyecto en Python permite **clasificar objetos en tiempo real** usando la cámara de tu laptop, identificando si el objeto es un **círculo** o un **cuadrado**. Utiliza **visión artificial** con OpenCV y una **red neuronal convolucional (CNN)** construida con TensorFlow/Keras.

---

## 📁 Estructura del Proyecto

```
shape_classifier/
├── main.py                  # (opcional) menú de ejecución
├── requirements.txt         # librerías necesarias
├── .gitignore               # excluye dataset, venv y modelo
├── model/                   # modelo entrenado (no incluido en repo)
│   └── shape_model.h5       
├── dataset/                 # imágenes para entrenamiento (excluido del repo)
│   ├── circle/
│   └── square/
├── src/
│   ├── capture_dataset.py   # capturar imágenes desde cámara
│   ├── train_model.py       # entrenar red neuronal
│   └── shape_classifier.py  # clasificación en tiempo real
```

---

## ⚙️ Instalación

1. Crea y activa un entorno virtual:

```bash
python -m venv venv
venv\Scripts\activate   # En Windows
# o
source venv/bin/activate  # En Linux/macOS
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

---

## 📸 Captura de Imágenes

Ejecuta este script y presiona `s` para guardar una imagen y `q` para salir:

```bash
python src/capture_dataset.py
```

Se te pedirá indicar si capturas `circle` o `square`.

---

## 🧠 Entrenamiento del Modelo

Una vez tengas suficientes imágenes (recomendado: 50–100 por clase):

```bash
python src/train_model.py
```

Esto entrenará una CNN y guardará el modelo en `model/shape_model.h5`.

---

## 🔍 Clasificación en Tiempo Real

Después de entrenar el modelo, clasifica en vivo desde tu cámara:

```bash
python src/shape_classifier.py
```

El resultado se mostrará en pantalla sobre la imagen.

---

## 📌 Notas

- La carpeta `dataset/` está excluida del repositorio (.gitignore).
- El modelo entrenado también se mantiene local (`model/shape_model.h5`).
- Asegúrate de tener buena iluminación y el objeto enfocado.

---

## 🚀 Tecnologías Usadas

- [Python 3](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [TensorFlow / Keras](https://www.tensorflow.org/)
- [NumPy](https://numpy.org/)

---
