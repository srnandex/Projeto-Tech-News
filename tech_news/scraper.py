import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    selector = Selector(html_content)
    return {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css(".entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".author a::text").get(),
        "comments_count": selector.css(".post-comments-simple h5::text")
        .get() or 0,
        "summary": selector.xpath("string(//p)").get().strip(),
        "tags": selector.css(".post-tags a::text").getall(),
        "category": selector.css(".meta-category span.label::text").get(),
    }


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com"
    news = []

    while len(news) < amount:
        html_content = fetch(url)
        link_news_by_page = scrape_updates(html_content)

        for link in link_news_by_page:
            if len(news) < amount:
                new = scrape_news(fetch(link))
                news.append(new)
                url = scrape_next_page_link(html_content)
        if not url:
            break

    create_news(news)
    return news
