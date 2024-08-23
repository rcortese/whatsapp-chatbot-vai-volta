from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Configurações das APIs usando variáveis de ambiente
GPT_J_API_URL = os.getenv('GPT_J_API_URL')
GPT_J_API_KEY = os.getenv('GPT_J_API_KEY')
EVOLUTION_API_URL = os.getenv('EVOLUTION_API_URL')
EVOLUTION_API_TOKEN = os.getenv('EVOLUTION_API_TOKEN')

# Função para obter resposta do GPT-J
def get_gpt_j_response(prompt):
    headers = {
        'Authorization': f'Bearer {GPT_J_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'prompt': prompt,
        'max_tokens': 150
    }
    response = requests.post(GPT_J_API_URL, headers=headers, json=data)
    return response.json()['choices'][0]['text'].strip()

# Função para enviar mensagem pelo Evolution API
def send_evolution_message(to, message):
    headers = {
        'Authorization': f'Bearer {EVOLUTION_API_TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {
        'jid': to,
        'message': message
    }
    response = requests.post(EVOLUTION_API_URL, headers=headers, json=data)
    return response.json()

@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_message = request.json
    message_text = incoming_message['message']['text']
    sender = incoming_message['message']['from']

    # Processa a mensagem recebida e obtém a resposta do GPT-J
    gpt_j_response = get_gpt_j_response(message_text)

    # Envia a resposta pelo Evolution API
    send_evolution_message(sender, gpt_j_response)

    return jsonify({'status': 'success', 'response': gpt_j_response})

if __name__ == '__main__':
    app.run(port=5000)
