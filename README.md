# 🤖 Rag-chatbot-Luat_Trat_tu_atgt_duong_bo

Dự án thử nghiệm xây dựng một Chatbot hỏi đáp theo kiến trúc **RAG cơ bản (Core RAG)** dựa trên dữ liệu văn bản **Luật Trật tự, An toàn giao thông đường bộ Việt Nam (Luật số 36/2024/QH15)**.

---

## 🛠️ Công nghệ sử dụng
- **Framework:** LangChain
- **LLM:** Gemini 2.5 Flash (Google AI Studio)
- **Embedding Model:** `vietnamese-bi-encoder` (BKAI)
- **Vector Database:** FAISS

---

## 📂 Cấu trúc thư mục
```text
Rag-chatbot-Luat_Trat_tu_atgt_duong_bo/
│
├── documents/papers/
│   └── 36-2024-qh15.docx       # File dữ liệu luật gốc (được bảo mật)
│
├── src/                        # Thư mục mã nguồn con
│   ├── config.py               # Lưu prompt và cấu hình chunking
│   ├── data_ingestion.py       # Đọc và phân tách văn bản
│   ├── vector_store.py         # Khởi tạo Vector DB
│   └── rag_chain.py            # Lắp ráp RAG pipeline
│
├── .env                        # Chứa GOOGLE_API_KEY (không đẩy lên GitHub)
├── .gitignore                  # Chỉ định các tệp Git cần bỏ qua
├── main.py                     # File chạy chính chương trình (CLI)
└── requirements.txt            # Danh sách thư viện cài đặt
