# API de Cartão

Esta é uma API para gerenciar números de cartão. Ela permite que os usuários insiram números de cartão individualmente ou através de um arquivo TXT, e consultem se um número de cartão existe na base de dados.

## Instalação

1. Clone este repositório.
2. Crie um arquivo chamdado `.env` e adicione as seguintes linhas:
```
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=postgres
```
2. Tenha instalado o 'Docker' (https://docs.docker.com/get-docker/).
3. Rode `docker compose up -d --build`. Isso irá iniciar os containers.
4. Abra o navegador e acesse `http://localhost:8000/`.

## Uso

### Autenticação

Todos os endpoints requerem autenticação. Você pode se autenticar usando o endpoint `/api/token/`, que aceita um nome de usuário e senha e retorna um token de acesso.

### Criação de Usuário
Você pode criar um novo usuário usando o endpoint `/api/user/create`, que aceita um nome de usuário e senha e retorna o usuário criado.

### Inserir Cartão

Você pode inserir um número de cartão usando o endpoint `POST /api/card/insert`. Você pode enviar um número de cartão como JSON no corpo da requisição ou enviar um arquivo TXT como parte de uma requisição multipart/form-data.

### Consultar se Existe um Cartão

Você pode consultar se um número de cartão existe na base de dados usando o endpoint `GET /api/card/validate`. Você deve fornecer o número do cartão como um parâmetro de consulta. Então receberá um uuid como resposta, caso o cartão exista.

## Documentação

[Swagger UI](http://localhost:8000/api/schema/swagger-ui/)

## Melhorias e Consideracões

- Leitura das linhas do arquivo TXT para inserir cartões, pode ser otimizado com uso de threads e regex.
- Pode ser usado kubernetes para deploy da aplicação e assim pode ser escalável.
- Pode ser usado um banco de dados preparado para incriptação de dados.
- Pode ser usado um sistema de logs para registrar as requisições e respostas de forma mais eficiente.
- Pode ser contruido testes usando o `pytest`.
