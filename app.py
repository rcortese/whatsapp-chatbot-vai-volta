import os
from dotenv import load_dotenv
from evolutionapi import EvolutionAPI
from llama3 import Llama3

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Inicialize o modelo Llama3 usando a API
llama3_api_url = os.getenv('LLAMA3_API_URL')
llama3_api_token = os.getenv('LLAMA3_API_TOKEN')
llama3_model = Llama3(api_url=llama3_api_url, api_token=llama3_api_token)

# Inicialize a EvolutionAPI
evolution_api = EvolutionAPI(api_key=os.getenv('EVOLUTION_API_TOKEN'), base_url=os.getenv('EVOLUTION_API_URL'))

def handle_message(message):
    response = llama3_model.generate_response(message)
    return response

# Configurar o webhook do WhatsApp
@evolution_api.on_message
def on_message(message):
    response = handle_message(message.text)
    evolution_api.send_message(message.from_, response)

if __name__ == "__main__":
    evolution_api.run(port=5000)
