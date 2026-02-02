# 1️⃣ Imagem base com Python
FROM python:3.11-slim

# 2️⃣ Define diretório de trabalho dentro do container
WORKDIR /app

# 3️⃣ Copia arquivos de dependência
COPY requirements.txt .

# 4️⃣ Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copia o restante do projeto
COPY . .

# 6️⃣ Expõe a porta do Gradio
EXPOSE 7860

# 7️⃣ Comando para iniciar a aplicação
CMD ["python", "app.py"]
