from operator import itemgetter
from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_news():
    result = sorted(find_news(), key=itemgetter(
        'comments_count', "title"), reverse=True)
    if len(result) > 5:
        result = result[:5]

    return [(new_sorted["title"], new_sorted["url"])for new_sorted in result]


# Requisito 11
def top_5_categories():
    categories = Counter(new["category"] for new in find_news())

    result = sorted(
      [(category, categories[category]) for category in categories],
      key=lambda x: (x[0], -x[1]))

    return [tup[0] for tup in sorted(result, key=lambda x: -x[1])][:5]
