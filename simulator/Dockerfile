FROM python:3.10
WORKDIR /sim
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY sensor_simulator.py .
CMD ["python", "sensor_simulator.py"]
