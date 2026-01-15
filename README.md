# 🪙 Contador de Moedas em Tempo Real com YOLOv8

## 🎥 Demonstração

[▶️ Assista ao vídeo completo](https://youtu.be/4mbWwbWrljY)

---

## 📌 Descrição do Projeto

Este projeto implementa um sistema de **contagem de moedas em tempo real** a partir de vídeo, utilizando **visão computacional** e **deep learning**.

O modelo foi treinado para detectar moedas brasileiras e realizar a contagem durante a execução do vídeo, exibindo os resultados frame a frame.

### Moedas reconhecidas
- 🪙 R$ 1,00
- 🪙 R$ 0,50
- 🪙 R$ 0,25

---

## 🧠 Tecnologias Utilizadas

- Python
- OpenCV
- YOLOv8n (Ultralytics)
- PyTorch

---

## 📂 Estrutura do Projeto

    contador-de-moedas
    ├── data
    │   ├── train
    │   ├──  valid
    │   ├── data.yaml
    │   └── treinamento_detectar_moedas.py
    ├── yolo_runs
    │   └── moedas2
    ├── contador_moedas.py
    ├── requirements.txt
    └── README.md

---

## 🧠 Pesos do Modelo

Os pesos do modelo (`best.pt`) foram treinados utilizando o **Brazilian Currency Dataset**, disponibilizado por Elaine Silva no Roboflow Universe.

Autor do dataset: Elaine Silva  
Link: https://universe.roboflow.com/elainesilva/brazilian-currency  
Licença do dataset: Creative Commons Attribution 4.0 International (CC BY 4.0)

Os pesos são fornecidos exclusivamente para fins educacionais e de demonstração.

## ⚙️ Treinamento do Modelo

O treinamento foi realizado utilizando a arquitetura **YOLOv8n**, com três classes:

- `1_real`
- `50_centavos`
- `25_centavos`

Os pesos e resultados do treinamento estão armazenados em:

    yolo_runs/moedas2

---

## ▶️ Execução

1. Clone o repositório:

        git clone https://github.com/seu-usuario/contador-de-moedas.git

2. Instale as dependências:

        pip install -r requirements.txt

3. Execute o programa:

        python contador_moedas.py

---

## 📈 Limitações

- A contagem é baseada em **detecção por frame**, sem rastreamento persistente.
- Pode ocorrer **dupla contagem** da mesma moeda.
- O desempenho é sensível a:
  - Iluminação
  - Sobreposição de moedas
  - Qualidade do vídeo

---

## 🚀 Possíveis Melhorias

- Implementação de **object tracking**.
- Inclusão de novos valores de moedas.
- Expansão e refinamento do dataset.
- Cálculo automático do valor total detectado.
- Otimização para dispositivos embarcados.

---

## 👤 Antony Reis

Projeto desenvolvido para fins **acadêmicos e educacionais**, com foco em **visão computacional** e **deep learning**.
