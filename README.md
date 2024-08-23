# WhatsApp Chatbot para Loja de Moda Circular

Este projeto implementa um chatbot de WhatsApp integrado a uma API de LLM (Large Language Model) para atendimento de clientes de uma loja de moda circular. O chatbot é capaz de responder a perguntas frequentes, agendar horários de atendimento e fornecer suporte ao cliente.

## Funcionalidades

- Respostas automáticas a perguntas frequentes usando GPT-J.
- Agendamento de horários de atendimento.
- Suporte ao cliente via WhatsApp usando Evolution API.

## Tecnologias Utilizadas

- Python
- Flask
- Docker
- API do Evolution
- API do GPT-J (EleutherAI)

## Pré-requisitos

- Python 3.9 ou superior
- Conta no Evolution API
- Chave de API do GPT-J (EleutherAI)
- Docker

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/rcortese/whatsapp-chatbot-vai-volta.git
    cd whatsapp-chatbot-vai-volta
    ```

2. Crie um arquivo `.env` no diretório raiz do projeto com as seguintes variáveis de ambiente:

    ```plaintext
    EVOLUTION_API_TOKEN=your_evolution_api_token
    GPT_J_API_KEY=your_gpt_j_api_key
    ```

3. Construa a imagem Docker:

    ```bash
    docker build -t whatsapp-chatbot .
    ```

4. Rode o container Docker, passando o arquivo `.env`:

    ```bash
    docker run -d -p 5000:5000 --env-file .env whatsapp-chatbot
    ```

## Uso

1. Configure o webhook no painel de administração do Evolution API para apontar para o seu servidor (por exemplo, `http://your-server-ip:5000/webhook`).

2. Envie mensagens pelo WhatsApp para testar o chatbot e verifique se ele responde corretamente.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
