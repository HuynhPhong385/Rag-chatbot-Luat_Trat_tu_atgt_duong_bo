from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from src.config import LEGAL_PROMPT_TEMPLATE

def build_rag_chain(vectorstore):
    """Kết nối Retriever, Prompt và Gemini LLM thành chuỗi xử lý"""
    # Cấu hình bộ rút trích dữ liệu (lấy top 4 đoạn liên quan nhất)
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4} 
    )

    prompt = PromptTemplate(
        template=LEGAL_PROMPT_TEMPLATE, 
        input_variables=["context", "question"]
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.0,
        max_output_tokens=1024
    )
    print("Khởi tạo bộ não LLM Gemini thành công!")

    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain