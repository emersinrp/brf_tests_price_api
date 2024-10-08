# brf_tests_price_api

    Este projeto é uma suíte de testes de performance para as APIs Financial Price B2B e Financial Price B2C da BRF. Ele foi desenvolvido utilizando o Locust para simulação de carga e testes de estresse, garantindo a robustez e a escalabilidade das APIs em diferentes condições de uso.

**Estrutura do Projeto:**

```plaintext
BRF_TESTS_PRICE_API/
│
├── helpers/
│   ├── price_payload.py              # Payload e variáveis para a API B2B
│   ├── price_payload_b2c.py          # Payload e variáveis para a API B2C
│   ├── rules.py                      # Regras de comportamento dos testes
│   ├── token_manager.py              # Gerenciamento de token OAuth2
│
├── logs/
│   ├── locust_errors.log             # Logs de erros durante os testes
│   ├── locust_success.log            # Logs de sucessos durante os testes
│
├── venv_price_tests/                 # Ambiente virtual do Python (não incluído no repositório)
├── .env                              # Variáveis de ambiente sensíveis (não incluído no repositório)
├── .gitignore                        # Arquivos e pastas ignorados pelo Git
├── locustfile.py                     # Arquivo principal de execução do Locust
├── README.md                         # Documentação do projeto
├── requirements.txt                  # Dependências do Python para o projeto
```

**Pré-requisitos:**

    Python 3.7+
    Locust 2.0+
    Ambiente virtual do Python (recomendado)

**Instalação:**

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/brf_tests_price_api.git
    cd brf_tests_price_api
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv_price_tests
    source venv_price_tests/bin/activate  # Para Linux/macOS
    .\venv_price_tests\Scripts\activate  # Para Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Crie o arquivo .env na raiz do projeto com o seguinte conteúdo:
    ```bash
    HOST=https://ygg-qas.brf.cloud
    TOKEN_URL=https://ygg-qas.brf.cloud/token
    CLIENT_ID=your_client_id
    CLIENT_SECRET=your_client_secret
    API_CLIENT_ID=operation
    API_CLIENT_SECRET=your_api_client_secret
    API_SCOPE=openid
    COOKIE=ApplicationGatewayAffinity=7417a8c51e01832ea79a1e44106f7be4; ApplicationGatewayAffinityCORS=7417a8c51e01832ea79a1e44106f7be4
    ```

**Estrutura dos Arquivos:**

    helpers/price_payload.py: Contém o payload e as variáveis utilizadas para os testes da API Financial Price B2B.

    helpers/price_payload_b2c.py: Contém o payload e as variáveis utilizadas para os testes da API Financial Price B2C.

    helpers/rules.py: Define o comportamento dos testes. Contém as tarefas get_price_b2b_task e get_price_b2c_task, que são executadas pelo Locust.

    helpers/token_manager.py: Responsável por gerenciar o token de autenticação, com renovação automática antes da expiração.

    logs/: Diretório onde os logs de sucesso e erros são armazenados durante a execução dos testes.

**Executando os Testes:**

    locust -f locustfiles/locustfile_operation_order.py
    locust --headless -f locustfiles/locustfile_operation_order.py --users 1 --spawn-rate 1
    locust --headless -f locustfiles/locustfile_operation_order.py --tags test1 --users 1 --spawn-rate 1
    locust -f ./locustfiles/locustfile_operation_order.py
    locust -f locustfiles/ --users 10 --spawn-rate 1
    
    -u 10: Define o número de usuários simultâneos.
    -r 2: Define a taxa de criação de novos usuários (2 usuários por segundo).
    --run-time 1m: Define a duração do teste (1 minuto).


**Execução com Interface Web:**

Para executar os testes com a interface web do Locust:

    locust -f locustfile.py
    Acesse http://localhost:8089 em seu navegador para configurar e iniciar os testes.


**Logs:**

    Os logs são armazenados na pasta logs/:

    locust_success.log: Armazena os logs de requisições bem-sucedidas, incluindo o nome da requisição, tempo de resposta e status code.
    locust_errors.log: Armazena os logs de requisições com falhas, incluindo nome da requisição, tempo de resposta, status code, payload enviado e resposta recebida.


**Contribuição:**

    Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou um pull request.

