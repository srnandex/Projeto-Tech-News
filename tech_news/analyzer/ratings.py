from operator import itemgetter
from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news = find_news()
    result = sorted(news, key=itemgetter(
        'comments_count', "title"), reverse=True)
    if len(result) > 5:
        result = result[:5]

    return [(new_sorted["title"], new_sorted["url"])for new_sorted in result]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
