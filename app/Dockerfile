# Resmi Python imajı
FROM python:3.10

# Container çalışırken aktif dizin
WORKDIR /app

# Bağımlılıkları önce kopyala (layer cache daha verimli olsun)
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Uygulama kodunu kopyala
COPY . .

# Dış dünya ile konuşacağımız port (belirtmek iyi pratiktir)
EXPOSE 5000

# Container açılınca Flask server'ı başlat
CMD ["python", "server.py"]
