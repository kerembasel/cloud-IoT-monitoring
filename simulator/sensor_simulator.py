import random, time, os, requests

# Docker/K8s içinde servis adıyla erişim için 'api' kullanacağız.
API_URL = os.getenv("API_URL", "http://api:5000/data")

while True:
    # Rastgele ölçümler üret
    data = {
        "temperature": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(40, 70), 2),
        "voltage": round(random.uniform(3.1, 3.3), 2)
    }
    print("Sending:", data, "->", API_URL, flush=True)
    try:
        # 2 sn'de bir ölçüm yolla
        requests.post(API_URL, json=data, timeout=2)
    except Exception as e:
        # API düşmüşse/log takibi için
        print("Post failed:", e, flush=True)
    time.sleep(2)
