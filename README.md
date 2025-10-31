# STRATASEC_TEST API

Este é um projeto de teste desenvolvido com Django e Django Rest Framework.

O projeto consiste em uma API para gerenciar salas de aula, fornecendo operações básicas para gestão de alunos e materiais pedagógicos.

## Pré-requisitos

Para rodar este projeto localmente, você precisará ter as seguintes ferramentas instaladas em sua máquina:

-   [**Python (versão 3.8 ou superior)**](https://www.python.org/downloads/ "null")
    
-   [**Git**](https://www.google.com/search?q=https://git-scm.com/downloads "null") (para clonar o repositório)
    

## Como Rodar o Projeto (Passo a Passo)

Siga estas instruções para configurar e executar o projeto em seu ambiente local.

### 1. Clonar o Repositório

Primeiro, abra seu terminal (Prompt de Comando, PowerShell, ou Terminal) e clone o repositório para sua máquina:

```
git clone [https://github.com/Leonardo-P-Monteiro/STRATASEC_TEST.git](https://github.com/Leonardo-P-Monteiro/STRATASEC_TEST.git)

```

### 2. Acessar a Pasta

Navegue para a pasta que você acabou de baixar:

```
cd STRATASEC_TEST

```

### 3. Criar e Ativar o Ambiente Virtual

É uma boa prática usar um ambiente virtual (`.venv`) para isolar as bibliotecas (dependências) deste projeto do restante do seu sistema.

```
# 1. Crie o ambiente virtual (ele usará o Python da sua máquina como base)
python -m venv .venv

# 2. Ative o ambiente virtual

```

**Para Windows (CMD / PowerShell):**

```
.venv\Scripts\activate

```

**Para Linux ou macOS:**

```
source .venv/bin/activate

```

_Após ativar, você verá `(.venv)` aparecer no início da linha do seu terminal._

### 4. Instalar as Dependências

Com o ambiente virtual ativado, instale todas as bibliotecas que o projeto precisa. O arquivo `requirements.txt` (que está no repositório) lista todas elas:

```
pip install -r requirements.txt

```

### 5. Aplicar as Migrações do Banco de Dados

Este projeto usa um banco de dados SQLite (que não precisa de instalação extra). Este comando irá criar o arquivo do banco (`db.sqlite3`) e preparar as tabelas necessárias:

```
python manage.py migrate && python manage.py makemigrations

```

### 6. Executar o Servidor

Tudo pronto! Agora, inicie o servidor de desenvolvimento do Django:

```
python manage.py runserver

```

### 7. Acessar a API

Você verá no seu terminal que o servidor está rodando. Abra seu navegador ou ferramenta de API (como Postman ou Insomnia) e acesse:

**`http://127.0.0.1:8000/`**

Ou acesse diretamente a página da API:

**`http://127.0.0.1:8000/api/schema/swagger-ui/`**

## Tecnologias Utilizadas

-   [Python](https://www.python.org/ "null")
    
-   [Django](https://www.djangoproject.com/ "null")
    
-   [Django Rest Framework](https://www.django-rest-framework.org/ "null")
    
-   [SQLite3](https://www.sqlite.org/index.html "null")
