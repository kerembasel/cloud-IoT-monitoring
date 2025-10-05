# cloud-IoT-monitoring
IoT dashboard project with Flask, Kubernetes, and Grafana JSON API
Cloud IoT Monitoring Dashboard
A complete **IoT Monitoring System** built using **Flask**, **Kubernetes**, and **Grafana**.

This project simulates real-time IoT sensor data (temperature, humidity, and voltage) being sent via a Flask REST API, visualized dynamically in Grafana through the JSON API plugin.

---

##  Tech Stack

- **Backend:** Flask (Python REST API)
- **Database:** MongoDB *(optional)*
- **Monitoring Dashboard:** Grafana (JSON API plugin)
- **Deployment:** Kubernetes (K8s) on local cluster
- **Frontend:** Grafana Gauges and Time Series panels

---

##  How It Works?

1. The Flask API (`iot-api`) generates and serves simulated IoT data at `/data`.
2. Grafana connects to this endpoint using the **JSON API data source**.
3. The dashboard displays live values for:
   -  Temperature  
   -  Humidity  
   -  Voltage
4. Everything runs inside a Kubernetes namespace called `iot`.

---

##  Example Architecture

---
kubectl get svc -n iot

NAME         TYPE        CLUSTER-IP      PORT(S)
grafana      NodePort    10.104.60.52    3000:32000/TCP
iot-api      ClusterIP   10.101.33.140   5000/TCP
mongo        ClusterIP   10.110.252.180  27017/TCP
