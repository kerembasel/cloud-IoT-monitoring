FROM python:3.10
WORKDIR /sim
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY sensor_simulator.py .
# Sürekli veri üreten script
CMD ["python", "sensor_simulator.py"]
