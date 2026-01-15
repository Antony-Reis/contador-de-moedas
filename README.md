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

## 🧪 Dataset

O modelo foi treinado utilizando um **dataset obtido na internet**, contendo imagens anotadas de moedas brasileiras.

### 📌 Créditos do Dataset

[INSIRA AQUI OS CRÉDITOS DO DATASET]

Autor:  [Elaine Silva](https://universe.roboflow.com/elainesilva)
Link:  https://universe.roboflow.com/elainesilva/brazilian-currency
Licença:  

---

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

## 👤 Autor

Projeto desenvolvido para fins **acadêmicos e educacionais**, com foco em **visão computacional** e **deep learning**.

---

## 🧠 Nota Técnica

Este projeto tem como foco **detecção de objetos**, não rastreamento.

Para aplicações que exigem contagem precisa por objeto único, recomenda-se a integração de algoritmos de **tracking**.
