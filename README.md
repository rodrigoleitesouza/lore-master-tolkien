# 🧙‍♂️ Lore-Master J.R.R. Tolkien

Um **assistente inteligente de lore** focado no universo de **J.R.R. Tolkien**, capaz de responder perguntas profundas sobre *O Senhor dos Anéis*, *O Silmarillion* e demais textos, utilizando **RAG (Retrieval-Augmented Generation)** com **LLMs locais via Ollama**.

> 📚 Pergunte sobre personagens, eventos, locais, linhas do tempo e curiosidades da Terra‑média — tudo baseado nos documentos que você indexar.

---

## ✨ Principais Funcionalidades

- 📖 **Indexação de documentos** (PDF, TXT, etc.) com embeddings
- 🧠 **RAG (Retrieval-Augmented Generation)** usando LangChain
- 🤖 **LLM local** via **Ollama** (sem depender de APIs externas)
- 🗂️ **Vector Database persistente** com ChromaDB
- 💬 **Interface web interativa** com Gradio
- 🐳 **Totalmente dockerizado** (Docker + Docker Compose)

---

## 🧩 Arquitetura (visão geral)

```
Usuário (Browser)
      ↓
   Gradio UI
      ↓
LangChain (QA + Memory)
      ↓
ChromaDB (Vector Store)
      ↓
Ollama (LLM local)
```

---

## 🚀 Como rodar a aplicação (passo a passo completo)

### 1️⃣ Pré‑requisitos

Antes de tudo, você precisa ter instalado:

- **Docker**
- **Docker Compose** (já vem junto nas versões recentes do Docker Desktop)

👉 Recomendado: **Docker Desktop (Windows / Mac)**

Download oficial:
- https://www.docker.com/products/docker-desktop/

Após instalar, **reinicie o computador**.

---

### 2️⃣ Verificar se o Docker está funcionando

Abra um terminal (PowerShell, CMD ou Terminal) e rode:

```bash
docker --version
docker compose version
```

Se ambos retornarem versão, está tudo certo ✅

---

### 3️⃣ Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/lore-master-tolkien.git
cd lore-master-tolkien
```

---

### 4️⃣ Estrutura esperada do projeto

```
lore-master-tolkien/
│
├─ app.py
├─ config.py
├─ requirements.txt
├─ Dockerfile
├─ docker-compose.yml
│
├─ rag/
│  ├─ embeddings.py
│  ├─ vectorstore.py
│  ├─ qa.py
│  ├─ llm.py
│  └─ memory.py
│
├─ data/
│  ├─ documents/   # coloque aqui os textos da lore
│  └─ chroma/      # base vetorial persistente
│
└─ README.md
```

---

### 5️⃣ Subir a aplicação com Docker Compose

Na raiz do projeto, execute:

```bash
docker compose up --build
```

📦 Isso irá:
- Construir a imagem da aplicação
- Subir o Ollama
- Subir o Lore‑Master
- Criar volumes persistentes

⚠️ **Na primeira execução pode demorar**, pois o Docker irá baixar dependências.

---

### 6️⃣ Baixar o modelo LLM no Ollama (passo obrigatório)

Em outro terminal, execute:

```bash
docker exec -it ollama ollama pull llama3.2
```

Esse passo garante que o modelo exista **dentro do container**.

Verifique com:

```bash
docker exec -it ollama ollama list
```

---

### 7️⃣ Acessar a aplicação

Abra o navegador e acesse:

👉 **http://localhost:7860**

Você verá a interface do **Lore-Master J.R.R. Tolkien** 🎉

---

### 8️⃣ Fluxo de uso

1. Coloque os arquivos da lore em:
   ```
   data/documents/
   ```
2. Clique em **Indexar documentos**
3. Aguarde o processamento
4. Faça perguntas no chat

---

## 🛠️ Comandos úteis

### Ver logs em tempo real

```bash
docker compose logs -f
```

### Parar a aplicação

```bash
docker compose down
```

### Reiniciar

```bash
docker compose restart
```

---

## ⚙️ Configurações principais

Arquivo: `config.py`

```python
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "llama3.2"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
```

Você pode trocar o modelo do Ollama facilmente (ex: `mistral`, `llama3`, etc.).

---

## 📌 Observações importantes

- O banco vetorial **é persistente** (fica em `data/chroma`)
- O modelo do Ollama **fica salvo em volume Docker**
- Nenhuma API externa é necessária
- Funciona totalmente offline após o setup

---

## 🧙‍♂️ Visão futura (ideias)

- 🔍 Citação de fontes
- 🧵 Histórico de conversas
- 🌍 Deploy público
- 📚 Múltiplos universos literários

---

## 🧡 Créditos

Projeto desenvolvido como estudo e aplicação prática de:
- LLMs locais
- RAG
- LangChain
- Docker

Inspirado na obra de **J.R.R. Tolkien**.

> *“Even the smallest person can change the course of the future.”* — Galadriel

