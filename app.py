import gradio as gr
from rag.loader import load_documents
from rag.vectorstore import create_vectorstore, load_vectorstore
from rag.qa import get_qa_chain
from config import DOCUMENTS_DIR


DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)

qa_chain = None

vectorstore = load_vectorstore()
if vectorstore is not None:
    qa_chain = get_qa_chain(vectorstore)

def index_documents():
    global qa_chain

    # 1️⃣ Tenta carregar vectorstore existente
    vectorstore = load_vectorstore()
    if vectorstore is not None:
        qa_chain = get_qa_chain(vectorstore)
        return "ℹ️ Vector DB já existe. Usando base persistida."

    # 2️⃣ Se não existir, cria
    docs = load_documents(DOCUMENTS_DIR)
    if not docs:
        qa_chain = None
        return "❌ Nenhum documento encontrado."

    vectorstore = create_vectorstore(docs)
    qa_chain = get_qa_chain(vectorstore)

    return f"✅ {len(docs)} documentos indexados com sucesso."


def ask_question(question):
    global qa_chain

    if qa_chain is None:
        return "⚠️ Os documentos ainda não foram indexados."

    response = qa_chain.invoke({
        "question": question,
        "chat_history": []
    })

    return response["answer"]


with gr.Blocks() as demo:
    gr.Markdown("# 🧙‍♂️ Lore-Master J.R.R. Tolkien — Knowledge Assistant")

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("## 📂 Documentos")
            gr.Markdown(f"Coloque arquivos em: `{DOCUMENTS_DIR}`")
            index_btn = gr.Button("📚 Indexar a Lore da Terra-média")
            index_output = gr.Textbox(label="Status", interactive=False)
            index_btn.click(index_documents, outputs=index_output)

        with gr.Column(scale=2):
            gr.Markdown("## 💬 Pergunte")
            question = gr.Textbox(
                label="Pergunta",
                placeholder="Digite sua pergunta...",
                lines=2
            )
            answer = gr.Textbox(
                label="Resposta",
                lines=8
            )
            ask_btn = gr.Button("Perguntar")
            ask_btn.click(
                ask_question,
                inputs=question,
                outputs=answer
            )


if __name__ == "__main__":
    demo.launch(
    theme=gr.themes.Soft(),
    inbrowser=True,
    server_name="0.0.0.0",
    server_port=7860
)
