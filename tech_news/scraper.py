import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, headers={"user-agent": "Fake user-agent"})

        if response.status_code == 200:
            return response.text

    except requests.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    return Selector(html_content).css(".cs-overlay-link::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    return Selector(html_content).css(".next::attr(href)").get()


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
