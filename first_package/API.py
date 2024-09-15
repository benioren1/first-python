import requests
url = "https://newsapi.org/v2/everything?q=milk&apiKey=42f3a0aae0fa4737bb5aefb52345a093"
result = requests.get(url)
print(result.json())