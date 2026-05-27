from langchain_community.document_loaders import DirectoryLoader, UnstructuredFileLoader 
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from src.config import DATA_PATH, CHUNK_SIZE, CHUNK_OVERLAP, MARKDOWN_SEPARATORS

def load_and_split_documents():
    """Đọc tệp tin docx từ thư mục cấu hình và tiến hành cắt nhỏ"""
    print("Đang tải tài liệu từ thư mục...")
    loader = DirectoryLoader(
        path=DATA_PATH,
        glob="**/*.docx",
        loader_cls=UnstructuredFileLoader,
        show_progress=True,
        use_multithreading=True
    )
    docs = loader.load()
    print(f"Đã tải xong {len(docs)} tài liệu thô.")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        add_start_index=True,
        strip_whitespace=True,
        separators=MARKDOWN_SEPARATORS
    )
    
    splits = text_splitter.split_documents(docs)
    print(f"Đã phân cắt thành {len(splits)} đoạn nhỏ (chunks).")
    return splits