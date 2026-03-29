<p align="center">
  🔗 Shortify API
</p>


API de encurtamento de URLs desenvolvida com **FastAPI** e **Supabase**, com autenticação JWT e segurança via Row Level Security (RLS).

---

## 🌐 Deploy

🚀 API Online:
[https://url-shortener-qi68.onrender.com](https://url-shortener-qi68.onrender.com)

📄 Documentação (Swagger):
[https://url-shortener-qi68.onrender.com/docs](https://url-shortener-qi68.onrender.com/docs)

---

## 🧱 Arquitetura do Projeto

```
src/
├── dependencias/
│   ├── auth_dependency.py
│   ├── config.py
│   └── supabase_client.py
│
├── routes/
│   ├── auth.py
│   └── url.py
│
├── schemas/
│   ├── user.py
│   └── url.py
│
└── manage.py
```

---

## ⚙️ Tecnologias Utilizadas

* ⚡ FastAPI
* 🐍 Python
* 🗄️ Supabase (PostgreSQL + Auth)
* 🔐 JWT Authentication
* 🔒 Row Level Security (RLS)
* ☁️ Render (Deploy)

---

## 🔐 Autenticação

A API utiliza autenticação via JWT do Supabase.

### 🔑 Passos:

1. Faça login:

```http
POST /auth/login
```

2. Copie o `access_token`

3. No Swagger, clique em **Authorize** e insira:

```bash
Bearer SEU_TOKEN
```

---

## 📌 Endpoints

### 🔐 Auth

| Método | Endpoint         | Descrição         |
| ------ | ---------------- | ----------------- |
| POST   | `/auth/register` | Registrar usuário |
| POST   | `/auth/login`    | Login             |
| GET    | `/auth/profile`  | Perfil do usuário |

---

### 🔗 URLs

| Método | Endpoint               | Descrição                         |
| ------ | ---------------------- | --------------------------------- |
| GET    | `/urls/`               | Listar URLs do usuário            |
| POST   | `/urls/`               | Criar URL encurtada               |
| PUT    | `/urls/{url_id}`       | Atualizar URL                     |
| DELETE | `/urls/{url_id}`       | Deletar URL                       |
| GET    | `/urls/r/{short_code}` | 🔥 Redirecionar para URL original |


---

### ❤️ Health Check

| Método | Endpoint   | Descrição     |
| ------ | ---------- | ------------- |
| GET    | `/monitor` | Status da API |

---

## 🧪 Exemplo de Request

```json
{
  "original_url": "https://www.google.com",
  "expires_at": null
}
```

---

## 🔐 Segurança

* ✅ Autenticação via JWT
* ✅ RLS no Supabase (cada usuário acessa apenas seus dados)
* ✅ Validação de dados com Pydantic

---

## ⚙️ Variáveis de Ambiente

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
SUPABASE_SERVICE_KEY=your_supabase_service_key
```

---

## ▶️ Rodando Localmente

### Pré-requisitos

<p align="justify">Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:</p>

<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=git,python,vscode" />
</a>


### 1. Clone o repositório

```bash
git clone https://github.com/Gelzieny/url_shortener.git

cd url_shortener

# Windows
python -m venv venv && venv\Scripts\activate.bat && pip install -r requirements.txt


#Linux / MAC
python -m venv venv && source venv/bin/activate && pip install -r requirements.txt

uvicorn src.manage:app --reload
```

---

## 🚀 Funcionalidades

* ✅ Cadastro e login de usuário
* ✅ Geração de URLs encurtadas
* ✅ CRUD completo
* ✅ Proteção por usuário
* ✅ Deploy em produção

---

## 🔮 Próximas melhorias

* 🔗 Redirecionamento `/r/{short_code}`
* 📊 Contador de cliques
* ⏳ Expiração automática
* 🧑‍💼 Controle de roles (admin/user)

---

## 👨‍💻 Autor

Desenvolvido por **Gelzieny** 🚀

