# Ecommerce API

API REST para gerenciamento de contas de um sistema de e‑commerce.

Base URL:

https://ecommerce-api-4k6g.onrender.com/api/v1/

------------------------------------------------------------------------

# Autenticação

A API utiliza **JWT (JSON Web Token)** para autenticação.

Após obter o token, ele deve ser enviado no header das requisições:

Authorization: Bearer SEU_TOKEN

------------------------------------------------------------------------

# Registrar Conta

Cria um usuário e uma conta no sistema.

Endpoint:

POST /api/v1/accounts/register/

URL completa:

https://ecommerce-api-4k6g.onrender.com/api/v1/accounts/register/

Content-Type:

multipart/form-data

## Parâmetros

| Campo | Tipo | Obrigatório | Descrição |
|------|------|-------------|-----------|
| username | string | sim | Nome de usuário |
| password | string | sim | Senha |
| name | string | sim | Nome da conta |
| phone | string | não | Telefone |
| address | string | não | Endereço |
| cnpj | string | não | CNPJ |
| image | file | não | Imagem da conta |

### Exemplo curl

curl -X POST
https://ecommerce-api-4k6g.onrender.com/api/v1/accounts/register/\
-F "username=loja123"\
-F "password=123456"\
-F "name=Loja Exemplo"\
-F "phone=11999999999"\
-F "address=Rua Teste 123"\
-F "cnpj=12345678000199"

------------------------------------------------------------------------

# Login / Obter Token

Endpoint usado para autenticar o usuário.

POST /api/v1/authentication/token/

URL:

https://ecommerce-api-4k6g.onrender.com/api/v1/authentication/token/

Content-Type:

application/json

## Body

{ "username": "loja123", "password": "123456" }

## Resposta esperada

{ "access": "TOKEN_DE_ACESSO", "refresh": "TOKEN_DE_REFRESH" }

------------------------------------------------------------------------

# Refresh Token

POST /api/v1/authentication/token/refresh/

Body:

{ "refresh": "SEU_REFRESH_TOKEN" }

------------------------------------------------------------------------

## Estrutura da Conta

| Campo | Tipo | Descrição |
|------|------|-----------|
| id | integer | ID da conta |
| name | string | Nome da empresa |
| phone | string | Telefone |
| address | string | Endereço |
| cnpj | string | CNPJ |
| avatar_url | string | URL do avatar |
| instagram_url | string | Instagram |
| facebook_url | string | Facebook |
| other_url | string | Outro link |
| color_palette | string | Paleta de cores |
| created_at | datetime | Data de criação |
| updated_at | datetime | Última atualização |

------------------------------------------------------------------------

# Fluxo básico de uso

1.  Registrar usuário POST /accounts/register/

2.  Fazer login POST /authentication/token/

3.  Usar token nas requisições Authorization: Bearer TOKEN

------------------------------------------------------------------------


# Produtos

Endpoints responsáveis por gerenciar produtos.

⚠️ Requer autenticação.

Authorization: Bearer SEU_TOKEN

A API retorna **somente produtos da conta do usuário autenticado**.

------------------------------------------------------------------------

# Criar Produto

POST /api/v1/products/

## Parâmetros

| Campo        | Tipo     | Obrigatório | Descrição                                   |
|---------------|----------|-------------|-----------------------------------------------|
| id           | integer  | Não         | ID do produto (gerado automaticamente)       |
| account      | integer  | Não         | Conta dona do produto (definida pelo backend)|
| name         | string   | Sim         | Nome do produto                              |
| category     | integer  | Sim         | ID da categoria do produto                   |
| description  | string   | Não         | Descrição do produto                         |
| price        | decimal  | Sim         | Preço do produto                             |
| stock        | integer  | Sim         | Quantidade disponível em estoque             |
| image_url    | string   | Não         | URL pública da imagem (somente leitura)      |
| image        | file     | Não         | Arquivo de imagem do produto                 |
| crop_x       | integer  | Não         | Posição X inicial para recorte da imagem     |
| crop_y       | integer  | Não         | Posição Y inicial para recorte da imagem     |
| crop_width   | integer  | Não         | Largura da área de recorte da imagem         |
| crop_height  | integer  | Não         | Altura da área de recorte da imagem          |
| created_at   | datetime | Não         | Data de criação do registro                  |
| updated_at   | datetime | Não         | Data da última atualização                   |

------------------------------------------------------------------------

# Listar Produtos

GET /api/v1/products/

------------------------------------------------------------------------

# Buscar Produto

GET /api/v1/products/{id}/

------------------------------------------------------------------------

# Atualizar Produto

PUT /api/v1/products/{id}/

ou

PATCH /api/v1/products/{id}/

------------------------------------------------------------------------

# Deletar Produto

DELETE /api/v1/products/{id}/

------------------------------------------------------------------------

# Estrutura do Produto

| Campo        | Tipo     | Descrição                                   |
|---------------|----------|-----------------------------------------------|
| id           | integer  | ID do produto                                 |
| account      | integer  | Conta dona do produto                         |
| name         | string   | Nome do produto                               |
| category     | string   | ID da categoria do produto                    |
| description  | string   | Descrição do produto                          |
| price        | decimal  | Preço do produto                              |
| stock        | integer  | Quantidade disponível em estoque              |
| image_url    | string   | URL pública da imagem do produto (read-only)  |
| crop_x       | integer  | Posição X inicial para recorte da imagem      |
| crop_y       | integer  | Posição Y inicial para recorte da imagem      |
| crop_width   | integer  | Largura da área de recorte da imagem          |
| crop_height  | integer  | Altura da área de recorte da imagem           |
| created_at   | datetime | Data de criação do registro                   |
| updated_at   | datetime | Data da última atualização                    |

------------------------------------------------------------------------

# Fluxo básico

1.  Registrar conta
2.  Fazer login
3.  Criar produtos
4.  Listar produtos

------------------------------------------------------------------------


# Tecnologias

-   Django
-   Django Rest Framework
-   JWT Authentication
