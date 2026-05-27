from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.utils import DistanceStrategy

def create_vector_store(splits):
    """Xây dựng Vector DB từ các đoạn text đã cắt"""
    print("Đang khởi tạo Embedding Model (BKAI)...")
    embeddings = HuggingFaceEmbeddings(
        model_name="bkai-foundation-models/vietnamese-bi-encoder"
    )
    
    print("Đang chuyển hóa text thành Vector và nạp vào FAISS...")
    vectorstore = FAISS.from_documents(
        documents=splits,
        embedding=embeddings,
        distance_strategy=DistanceStrategy.COSINE
    )
    print("Xây dựng kho dữ liệu Vector FAISS thành công!")
    return vectorstore