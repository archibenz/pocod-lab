import time, urllib.request
URL = "http://webserver:8000/index.html"
for attempt in range(1, 6):
    try:
        with urllib.request.urlopen(URL, timeout=5) as r:
            print(f"[клиент] попытка {attempt}: HTTP {r.status}")
            print("[клиент] тело ответа:", r.read().decode().strip())
            break
    except Exception as e:
        print(f"[клиент] попытка {attempt}: сервер ещё не готов ({e})")
        time.sleep(2)
