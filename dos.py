import requests
import time

url = "https://share.net.ru/api/Posts/range?skip=100&limit=100&currentUserId=500000"

while True:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Запрос успешен! Получено данных:", len(response.json()))
        else:
            print(f"Ошибка запроса: {response.status_code}")
    except Exception as e:
        print("Произошла ошибка при запросе:", e)
    
    time.sleep(5)  # Ждем 5 секунд перед следующим запросом
