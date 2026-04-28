from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


VECTOR_DB_PATH = "vector_store/faiss_index"


def load_retriever():
    print("Loading embedding model...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )

    print("Loading FAISS index...")
    vectorstore = FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    # top 3 kết quả gần nhất
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever


if __name__ == "__main__":
    retriever = load_retriever()

    while True:
        query = input("\nBạn hỏi: ").strip()

        if query.lower() in ["exit", "quit"]:
            break

        docs = retriever.invoke(query)

        print("\n=== TOP MATCHES ===\n")

        for i, doc in enumerate(docs, 1):
            print(f"[{i}] SOURCE:", doc.metadata.get("source"))
            print("-" * 60)
            print(doc.page_content[:700])
            print("\n" + "=" * 80)