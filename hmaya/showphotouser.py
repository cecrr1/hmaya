import requests

chat_id = "6207674867
urlp = "https://t.me/GGBGS"
url = f"https://t.me/GGBGS"

req = requests.get(url).json()
print(req)
