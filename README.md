# EN-US 🇺🇸

# JSON Editor and Publisher via MQTT

## 📋 Project Description

This project is an interactive Python application that enables the creation, editing, and management of complex **JSONs** based on a hierarchical structure, including aspects, types, and assets. It also allows the sending of the generated **JSON** to an **MQTT** broker with TLS certificate authentication, and viewing messages received from a subscribed topic.

## 🔧 Features

### Main Features:
1. **JSON Management**:
   - Add, edit, and view aspects, types, and assets.
   - Automatic configuration of mappings in the `mappingModel` field.

2. **MQTT Connection**:
   - Connect to a secure MQTT broker with username/password and TLS certificates.
   - Send messages to an MQTT topic.
   - Subscribe and receive messages from an MQTT topic.

3. **User-Friendly Graphical Interface**:
   - Developed in **Tkinter** to facilitate use.
   - Intuitive buttons for each action.

## 🚀 Technologies Used

- **Python**:
  - [Tkinter](https://docs.python.org/3/library/tkinter.html): Graphical interface.
  - [paho-mqtt](https://www.eclipse.org/paho/): MQTT connection.
  - [JSON](https://docs.python.org/3/library/json.html): JSON data manipulation.
- **MQTT with TLS**: Additional security for communication.

## 📂 Project Structure

```
project/
├── mqtt_handler.py      # Manages MQTT connection logic
├── interface.py         # Manages the graphical interface and JSON manipulation
├── infos.json           # MQTT connection settings
├── data.json            # Output file with the generated JSON
├── mqttv4/certs/        # TLS Certificates
│   ├── ca.pem           # CA Certificate
│   ├── client.pem       # Client Certificate
│   └── client.key       # Private key of the client
```

## 🛠️ Environment Setup

### Prerequisites:
- Python 3.8 or higher.
- Install the necessary libraries:
  ```bash
  pip install paho-mqtt
  ```

### Configuration of `infos.json`:
Edit the `infos.json` file to include your MQTT broker information:
```json
{
    "infos": {
        "BROKER": "mqtts://your-broker-here.com",
        "PORT": 8883,
        "TOPIC": "your/publish/topic",
        "TOPIC_SUB": "your/subscription/topic",
        "USERNAME": "your-username",
        "PASSWORD": "your-password",
        "CLIENT_ID": "your-client-id"
    }
}
```

## 📋 Usage Instructions

### 1. Configure Tenant
- Click on the **"Configure Tenant"** button and enter the tenant name

### 2. Add Aspects
- Click on **"Add Aspect"**.
- Fill in the ID, description, and the variables associated with the aspect (name, type, and unit).

### 3. Add Types (Types)
- Click on **"Add Type"**.
- Fill in the ID, description, and associate previously created aspects with the type.

### 4. Add Assets (Assets)
- Click on **"Add Asset"**.
- Fill in the asset name and select an existing type.

### 5. Generate Mappings
- Click on **"Generate Mappings"**.
- The system automatically associates the variables of the aspects with the assets.

### 6. View JSON
- Click on **"View JSON"** to check the current structure.

### 7. Send Message
- Click on **"Send Message"** to publish the JSON on the configured topic.

## 🔒 Security

This project uses:
- **TLS 1.2** to ensure security in communication.
- **`.pem`** certificates for authentication.

## 🐞 Troubleshooting

1. **MQTT Connection Error**:
   - Check the `BROKER`, `PORT`, `USERNAME` and `PASSWORD` in `infos.json`.
   - Ensure that the certificates in the `mqttv4/certs/` directory are valid.

2. **Error Generating Mappings**:
   - Make sure that there are correctly configured aspects, types, and assets before generating mappings.
-----------------------------------------------------------------------------------------------------------------------------------

# PT-BR 🇧🇷
# Editor e Publicador de JSON via MQTT

## 📋 Descrição do Projeto

Este projeto é uma aplicação interativa em Python que permite criar, editar e gerenciar **JSONs complexos** baseados em uma estrutura hierárquica, incluindo aspectos, tipos e ativos (aspects, types e assets). Além disso, ele permite enviar o JSON gerado para um broker **MQTT** com suporte a autenticação e certificados TLS, e visualizar as mensagens recebidas de um tópico assinado.

## 🔧 Funcionalidades

### Principais Funcionalidades:
1. **Gerenciamento de JSON**:
   - Adicionar, editar e visualizar aspectos, tipos e ativos.
   - Configuração automática de mapeamentos no campo `mappingModel`.

2. **Conexão MQTT**:
   - Conectar-se a um broker MQTT seguro com autenticação por usuário/senha e certificados TLS.
   - Enviar mensagens para um tópico MQTT.
   - Inscrever-se e receber mensagens de um tópico MQTT.

3. **Interface Gráfica Amigável**:
   - Desenvolvida em **Tkinter** para facilitar o uso.
   - Botões intuitivos para realizar cada ação.

## 🚀 Tecnologias Utilizadas

- **Python**:
  - [Tkinter](https://docs.python.org/3/library/tkinter.html): Interface gráfica.
  - [paho-mqtt](https://www.eclipse.org/paho/): Conexão MQTT.
  - [JSON](https://docs.python.org/3/library/json.html): Manipulação de dados JSON.
- **MQTT com TLS**: Segurança adicional para comunicação.

## 📂 Estrutura do Projeto

```
project/
├── mqtt_handler.py      # Gerencia a lógica de conexão MQTT
├── interface.py         # Gerencia a interface gráfica e manipulação do JSON
├── infos.json           # Configurações de conexão MQTT
├── dados.json           # Arquivo de saída com o JSON gerado
├── mqttv4/certs/        # Certificados TLS
│   ├── ca.pem           # Certificado CA
│   ├── client.pem       # Certificado do cliente
│   └── client.key       # Chave privada do cliente
```

## 🛠️ Configuração do Ambiente

### Pré-requisitos:
- Python 3.8 ou superior.
- Instale as bibliotecas necessárias:
  ```bash
  pip install paho-mqtt
  ```

### Configuração do `infos.json`:
Edite o arquivo `infos.json` para incluir as informações do seu broker MQTT:
```json
{
    "infos": {
        "BROKER": "mqtts://seu-broker-aqui.com",
        "PORT": 8883,
        "TOPIC": "seu/topico/publicacao",
        "TOPIC_SUB": "seu/topico/assinatura",
        "USERNAME": "seu-usuario",
        "PASSWORD": "sua-senha",
        "CLIENT_ID": "seu-client-id"
    }
}
```

## 📋 Instruções de Uso

### 1. Configuração do Tenant
- Clique no botão **"Configurar Tenant"** e insira o nome do tenant.

### 2. Adicionar Aspectos
- Clique em **"Adicionar Aspect"**.
- Preencha o ID, descrição e as variáveis associadas ao aspect (nome, tipo e unidade).

### 3. Adicionar Tipos (Types)
- Clique em **"Adicionar Type"**.
- Preencha o ID, descrição e associe aspectos já criados ao tipo.

### 4. Adicionar Ativos (Assets)
- Clique em **"Adicionar Asset"**.
- Preencha o nome do ativo e selecione um tipo já existente.

### 5. Gerar Mapeamentos
- Clique em **"Gerar Mapeamentos"**.
- O sistema associa automaticamente as variáveis dos aspectos aos ativos.

### 6. Visualizar JSON
- Clique em **"Visualizar JSON"** para conferir a estrutura atual.

### 7. Enviar Mensagem
- Clique em **"Enviar Mensagem"** para publicar o JSON no tópico configurado.

## 🔒 Segurança

Este projeto usa:
- **TLS 1.2** para garantir segurança na comunicação.
- Certificados **`.pem`** para autenticação.

## 🐞 Solução de Problemas

1. **Erro de Conexão MQTT**:
   - Verifique o `BROKER`, `PORT`, `USERNAME` e `PASSWORD` no `infos.json`.
   - Certifique-se de que os certificados no diretório `mqttv4/certs/` são válidos.

2. **Erro ao Gerar Mapeamentos**:
   - Certifique-se de que há aspectos, tipos e ativos corretamente configurados antes de gerar os mapeamentos.
