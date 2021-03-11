import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.x-kom.pl/p/488369-sluchawki-bezprzewodowe-sony-wh-1000xm3b-czarne.html"

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}

def get_price():
    page = requests.get(URL, headers=HEADERS)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(class_="sc-1bker4h-4").get_text()
    price = soup.find(class_="u7xnnm-4").get_text()

    price = price.replace(",", ".")
    price = price.replace(" ", "")

    price = float(price[:7])

    print(price)
    print(title)

    if price < 1100:
        send_mail(title, price)


def send_mail(title, price):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("meetit25@gmail.com", "jywoqnxsklkpnsae")

    subject = title

    body = "Cena spadla ponizej oczekiwanej" + URL

    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail('meetit25@gmail.com', 'jakub.cytrowski@gmail.com', msg)

    print("message sent!")

    server.close()

while(True):
    get_price()
    time.sleep(3600)