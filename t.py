import requests

url = "https://t.me/GGBGS"
response = requests.get(url).content

# print(response)
# u = response[
#     response.index('src="https://cdn4.telegram-cdn.org/file') : response.index("></a>")
# ]
# print(u)

print(response.index("https://images.app.goo.gl/cjgkgwL9Rai7CRbV7"))
