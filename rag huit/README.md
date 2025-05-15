
# 🎓 Chatbot Tư Vấn Tuyển Sinh - HUIT (RAG + LangChain + FAISS)

## 📌 Mô tả
Dự án này xây dựng một chatbot AI sử dụng mô hình Retrieval-Augmented Generation (RAG) để tư vấn tuyển sinh dựa trên dữ liệu thực tế từ Trường Đại học Công Thương TP.HCM. Chatbot có khả năng truy xuất thông tin ngữ nghĩa từ dữ liệu JSON và tạo phản hồi thông minh dựa trên mô hình ngôn ngữ lớn (OpenAI GPT).

## 🔧 Công nghệ sử dụng
- **LangChain**: Xây dựng pipeline RAG và agent.
- **OpenAI GPT-4**: Mô hình ngôn ngữ tạo phản hồi.
- **FAISS**: Vector Database dùng cho truy vấn ngữ nghĩa.
- **Gradio**: Giao diện người dùng đơn giản.
- **Python**

## 📂 Dataset
Dữ liệu nằm trong file `cam_nang_tuyen_sinh_2.json`, bao gồm thông tin tuyển sinh, ngành học, chính sách học phí, học bổng, điều kiện xét tuyển,...

## 🚀 Cách chạy dự án

### 1. Cài đặt môi trường
```bash
pip install langchain openai faiss-cpu tiktoken gradio
```

### 2. Khai báo OpenAI API Key
```python
import os
os.environ["OPENAI_API_KEY"] = "your-api-key-here"
```

### 3. Chạy ứng dụng Gradio
```bash
python app.py
```

## 💡 Ứng dụng
- Trợ lý tuyển sinh tự động cho trường đại học
- Hệ thống hỏi đáp văn bản (Document QA)
- Mẫu tích hợp RAG vào dữ liệu tùy chỉnh

## 📄 License
MIT License.
