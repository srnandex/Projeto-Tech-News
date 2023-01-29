from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    return [(new["title"], new["url"]) for new in search_news(
        {"title": {"$regex": title, "$options": "i"}})]


# Requisito 7
def search_by_date(date):
    try:
        return [(new["title"], new["url"]) for new in search_news({
            "timestamp": {
                "$eq": datetime.fromisoformat(date).strftime("%d/%m/%Y")}})]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    return [(new["title"], new["url"]) for new in search_news({
        "tags": {"$elemMatch": {"$regex": tag, "$options": "i"}}})]


# Requisito 9
def search_by_category(category):
    return [(new["title"], new["url"]) for new in search_news({
        "category": {"$regex": category, "$options": "i"}})]
