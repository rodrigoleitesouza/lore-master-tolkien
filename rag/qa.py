from langchain.chains import ConversationalRetrievalChain
from rag.memory import create_memory
from rag.llm import get_llm
from rag.prompts import get_prompt


def get_qa_chain(vectorstore):
    llm = get_llm()
    memory = create_memory()
    prompt = get_prompt()

    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 4}),
        memory=memory,
        combine_docs_chain_kwargs={
            "prompt": prompt
        },
        return_source_documents=False
    )
