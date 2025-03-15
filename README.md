# CLI Iterativa com Claude

Esta é uma aplicação de linha de comando (CLI) interativa que utiliza a API do Claude para processar comandos e fornecer respostas inteligentes. A aplicação é construída em Python e utiliza várias bibliotecas para facilitar a interação com o usuário e a API.

## Pré-requisitos

Antes de executar a aplicação, certifique-se de ter os seguintes itens instalados:

- Python 3.7 ou superior
- Pip (gerenciador de pacotes do Python)

## Instalação

1. Clone este repositório para o seu ambiente local:
    ```sh
    git clone <URL_DO_REPOSITORIO>
    cd <NOME_DO_REPOSITORIO>
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências necessárias:
    ```sh
    pip install -r requirements.txt
    ```

## Configuração

1. Substitua `"sua-chave-api-aqui"` pela sua chave de API do Claude no arquivo `app.py`:
    ```python
    client = Anthropic(api_key="sua-chave-api-aqui")
    ```

## Execução

Para iniciar a aplicação, execute o seguinte comando no terminal:
```sh
python app.py
```

## Uso

- Digite comandos na linha de comando interativa.
- Para sair da aplicação, digite `sair`.

## Estrutura do Projeto

```
/
├── app.py          # Código principal da aplicação
├── journey.md      # Anotações e perguntas sobre a aplicação
└── README.md       # Este arquivo
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a MIT License.