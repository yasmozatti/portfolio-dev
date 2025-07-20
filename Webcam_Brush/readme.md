# WebCam Painter 🎨✋

Este é um projeto interativo em Python que utiliza visão computacional para transformar gestos da mão em traços de pincel na tela, como um "Paint" controlado por movimentos. O código é baseado na biblioteca **MediaPipe**, **OpenCV** e em um módulo auxiliar customizado para rastreamento de mãos.

## ✍️ Objetivo

Permitir que o usuário desenhe na tela usando apenas gestos capturados pela webcam, sem a necessidade de mouse ou touchscreen. Os gestos controlam:

- Seleção de cor
- Modo de desenho
- Borracha

## 🧠 Bibliotecas Utilizadas

- `cv2` (OpenCV) — Para capturar a imagem da webcam e desenhar na tela.
- `mediapipe` — Para rastreamento dos pontos da mão.
- `numpy` — Para manipulação da tela de desenho.
- `os`, `time`, `math` — Para operações auxiliares.


## ⚙️ Como Funciona

### 1. **Rastreamento de Mãos**

A classe `handDetector` (em `HandTrackingModule.py`) usa o MediaPipe para detectar e acompanhar os pontos das mãos, identificando:

- Posição de cada dedo
- Dedos levantados
- Distância entre pontos (útil para interações mais avançadas)

### 2. **Modos de Uso**

- **Modo Seleção**: Quando os dedos indicador e médio estão levantados (`fingers[1] and fingers[2]`), é possível escolher uma cor passando o dedo indicador pela faixa superior da tela.
  
- **Modo Desenho**: Quando apenas o dedo indicador está levantado (`fingers[1] and not fingers[2]`), o usuário pode desenhar com a cor selecionada.

- **Modo Borracha**: Quando o usuário escolhe a imagem da borracha, a cor preta é ativada com uma espessura maior (`eraserThickness`).

### 3. **Canvas e Camadas**

- `imgCanvas`: Camada onde o desenho é salvo.
- A imagem da webcam é combinada com o `imgCanvas` usando máscaras para preservar o fundo e sobrepor os desenhos.

### 4. **Barra Superior (Header)**

- Arquivos de imagem carregados de `WebCam_Brush/header`
- Cada área da barra ativa uma cor diferente conforme a posição X do dedo indicador.

## 🖥️ Execução

```bash
pip install opencv-python mediapipe numpy
python WebCamPainter.py


