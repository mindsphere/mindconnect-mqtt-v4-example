import json
import paho.mqtt.client as mqtt
import os

# Carregar informações do arquivo JSON
with open('infos.json', 'r') as json_file:
    infos = json.load(json_file)["infos"]

BROKER = infos['BROKER'].replace("mqtts://", "")
PORT = infos['PORT']
TOPIC_PUB = infos['TOPIC_PUB']
USERNAME = infos['USERNAME']
PASSWORD = infos['PASSWORD']
CLIENT_ID = infos['CLIENT_ID']
TOPIC_SUB = infos['TOPIC_SUB']

CERT_PATH = "certs/"
CA_CERT = os.path.join(CERT_PATH, "DigiCertGlobalRootG2.crt.pem")
CLIENT_CERT = os.path.join(CERT_PATH, "debr_MQTTPython.pem")
CLIENT_KEY = os.path.join(CERT_PATH, "debr_MQTTPython.key")

class MQTTHandler:
    def __init__(self, on_message_callback):
        self.client = mqtt.Client(client_id=CLIENT_ID, protocol=mqtt.MQTTv311)
        self.client.username_pw_set(USERNAME, PASSWORD)
        self.client.tls_set(ca_certs=CA_CERT, certfile=CLIENT_CERT, keyfile=CLIENT_KEY)
        self.client.tls_insecure_set(False)
        self.client.on_connect = self.on_connect
        self.client.on_message = on_message_callback

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print('Conectado ao broker MQTT com sucesso.')
            # Inscreve-se no tópico especificado no JSON
            client.subscribe(TOPIC_SUB)
            print(f"Inscrito no tópico: {TOPIC_SUB}")
        else:
            print(f'Falha na conexão com o broker. Código de retorno: {rc}')

    def start(self):
        self.client.connect(BROKER, PORT, 60)
        self.client.loop_start()

    def publish(self, message):
        self.client.publish(TOPIC_PUB, message)
        print("Mensagem enviada via MQTT.")
