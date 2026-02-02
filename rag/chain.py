from langchain.chains import ConversationalRetrievalChain
from rag.memory import create_memory


def create_qa_chain(llm, vectorstore):
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 4}
    )

    memory = create_memory()

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=False
    )

    return qa_chain
