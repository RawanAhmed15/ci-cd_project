# 1. هنبدأ بنسخة بايثون جاهزة وخفيفة
FROM python:3.9-slim

# 2. هنحدد فولدر جوه الكونتينر نشتغل فيه
WORKDIR /app

# 3. هننسخ ملف المكتبات ونطبها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. هننسخ كل الملفات اللي في الفولدر (الكود والداتا) للكونتينر
COPY . .

# 5. هنفتح البورت بتاع الأبلكيشن (Streamlit بيشتغل على 8501)
EXPOSE 8501

# 6. أمر تشغيل الأبلكيشن أول ما الكونتينر يقوم
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]