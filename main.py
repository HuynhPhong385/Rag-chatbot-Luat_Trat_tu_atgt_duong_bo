from dotenv import load_dotenv
from src.data_ingestion import load_and_split_documents
from src.vector_store import create_vector_store
from src.rag_chain import build_rag_chain

def main():
    # 1. Nạp biến môi trường từ file .env đầu tiên
    load_dotenv()
    
    print("=== CHƯƠNG TRÌNH KHỞI CHẠY RAG CHATBOT LUẬT ATGT ===")
    
    # 2. Xử lý dữ liệu đầu vào
    splits = load_and_split_documents()
    
    # 3. Tạo cơ sở dữ liệu Vector
    vectorstore = create_vector_store(splits)
    
    # 4. Tạo chuỗi RAG Chain
    rag_chain = build_rag_chain(vectorstore)
    
    print("\nChatbot đã sẵn sàng. Bạn có thể đặt câu hỏi về Luật 36/2024/QH15!")
    print("(Gõ 'exit' hoặc 'quit' để thoát chương trình)\n")
    
    # 5. Vòng lặp hỏi đáp liên tục
    while True:
        question = input("Nhập câu hỏi của bạn: ")
        if question.strip().lower() in ['exit', 'quit']:
            print("Tạm biệt bạn!")
            break
            
        if not question.strip():
            continue
            
        print("Chatbot đang tra cứu dữ liệu pháp luật...")
        try:
            answer = rag_chain.invoke(question)
            print(f"\n Chatbot trả lời:\n{answer}\n")
            print("-" * 50)
        except Exception as e:
            print(f"❌ Có lỗi xảy ra trong quá trình xử lý: {e}\n")

if __name__ == "__main__":
    main()