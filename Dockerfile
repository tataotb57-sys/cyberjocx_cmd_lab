# 1. الصورة الأساسية (Python نسخة خفيفة)
FROM python:3.9-slim

# 2. تحديد مجلد العمل داخل الـ Container
WORKDIR /app

# 3. تثبيت برنامج ping داخل الـ Container
RUN apt-get update && apt-get install -y iputils-ping && rm -rf /var/lib/apt/lists/*

# 4. تثبيت المكتبات المطلوبة من requirements.txt
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 5. نسخ باقي الملفات (app.py و flag.txt)
COPY . /app/

# 6. فتح البورت 5000
EXPOSE 5000

# 7. تشغيل التطبيق
CMD ["python", "app.py"]
