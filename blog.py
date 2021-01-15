from bs4 import BeautifulSoup
import requests
from csv import writer


url = "https://www.rithmschool.com/blog"

res = requests.get(url)

response = BeautifulSoup(res.text, "html.parser")

articles = response.find_all("article")

with open("blog_scapping.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Title", "DateTime", "Url"])

    for article in articles:
        title = article.find("a").get_text()
        url = article.find("a")['href']
        dateTime = article.find("time")["datetime"]
        print(type(dateTime))
        csv_writer.writerow([title, dateTime, url])
