# YOLOv8 Real-Time Object Detection - Hack Açú 🚗

Este projeto utiliza o modelo YOLOv8 para realizar detecção de objetos em tempo real via webcam. O modelo foi integrado a um aplicativo de **agendamento de vagas de estacionamento** durante o evento **Hack Açú**.

O objetivo do projeto foi criar uma solução que permite detectar a ocupação das vagas de estacionamento utilizando a detecção de objetos, ajudando usuários a agendarem vagas disponíveis de forma eficiente e em tempo real.

## 🚀 Funcionalidades

- **Detecção em tempo real**: O modelo YOLOv8 é usado para identificar objetos no vídeo transmitido pela webcam.
- **Identificação de vagas ocupadas**: O sistema detecta automaticamente a ocupação das vagas de estacionamento através de imagens ao vivo.
- **Interface simples**: O código exibe as detecções de objetos em tempo real diretamente na tela, com caixas delimitadoras ao redor dos objetos detectados.

## 🔧 Tecnologias Utilizadas

- **Python**: Linguagem de programação principal para o projeto.
- **YOLOv8**: Modelo de detecção de objetos utilizado para identificar veículos e vagas ocupadas.
- **OpenCV**: Biblioteca para captura de vídeo e manipulação de imagens.
- **Ultralytics YOLO**: Framework para utilização do modelo YOLOv8.

## ⚙️ Como Executar

### 1. Instalar Dependências

Para rodar o projeto localmente, primeiro instale as dependências necessárias. Utilize o `pip` para instalar as bibliotecas necessárias.

### 2. Baixar o Modelo YOLOv8
Baixe o modelo YOLOv8 pré-treinado (yolov8x.pt) do repositório oficial ou utilize o modelo desejado para a detecção. Coloque o arquivo .pt na mesma pasta onde o script será executado.

### 3. Rodar o Código
Execute o script Python para iniciar a detecção de objetos via webcam. O código capturará o vídeo da sua webcam e exibirá as detecções de objetos em tempo real.

### 4. Resultados
O código irá capturar a imagem da webcam, aplicar o modelo YOLOv8 e mostrar as detecções de objetos em tempo real. No contexto do app de agendamento de vagas de estacionamento, as detecções podem ser usadas para identificar carros nas vagas e atualizar a disponibilidade das vagas automaticamente.

📸 Demonstração

![HackAçu](https://github.com/sthrmzy/YOLOv8-Object-Detection-for-Hack-A-/blob/main/img/B353A73F-3831-40B2-8521-E28950F4F7E3.jpeg)

Imagem acima mostra a detecção de objetos (como veículos) em tempo real, utilizando o modelo YOLOv8.

## 💡 Como Funciona

O sistema de agendamento de vagas de estacionamento utiliza a detecção de veículos para determinar se uma vaga está ocupada ou disponível. As imagens capturadas pela webcam são analisadas pelo modelo YOLOv8, que identifica veículos nas vagas de estacionamento. Com isso, o sistema pode atualizar a disponibilidade das vagas e permitir que os usuários façam o agendamento de uma vaga livre diretamente pelo aplicativo.

## 🤝 Contribuindo

Se você quiser contribuir para o projeto, fique à vontade para fazer um fork deste repositório e enviar pull requests. Fico aberto a sugestões e melhorias!

## 📅 Hack Açú

Este projeto foi criado como parte do Hack Açú, um hackathon focado em soluções inovadoras para problemas urbanos e de mobilidade. A ideia é melhorar a eficiência dos serviços de estacionamento, ajudando motoristas a encontrar vagas disponíveis e fazendo o processo de agendamento mais ágil e prático.

