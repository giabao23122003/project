
import os
import json
import gradio as gr
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
from langchain.chains import RetrievalQA

# Thiết lập API Key (bạn nên dùng biến môi trường)
os.environ["OPENAI_API_KEY"] = "your-api-keykey"  # Thay bằng API key thật

# Bước 1: Load dữ liệu JSON
with open("cam_nang_tuyen_sinh_2.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

documents = [Document(page_content=entry["content"], metadata={"title": entry["title"]}) for entry in raw_data]

# Bước 2: Tách văn bản
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(documents)

# Bước 3: Tạo vector store với FAISS
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)

# Bước 4: Tạo RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(temperature=0, model="gpt-4"),
    retriever=vectorstore.as_retriever(search_type="similarity", k=3)
)

# Bước 5: Hàm xử lý câu hỏi từ người dùng
def chatbot_fn(query):
    return qa_chain.run(query)

# Giao diện Gradio
gr.Interface(
    fn=chatbot_fn,
    inputs="text",
    outputs="text",
    title="🤖 Chatbot Tư Vấn Tuyển Sinh - HUIT",
    description="Nhập câu hỏi về phương thức xét tuyển, học bổng, ngành học,..."
).launch()
