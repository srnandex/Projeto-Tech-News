from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.analyzer.search_engine import (
  search_by_title,
  search_by_date,
  search_by_category,
  search_by_tag
)
import sys


def create_news():
    get_tech_news(input("Digite quantas notícias serão buscadas:"))


def get_title():
    search_by_title(input("Digite o título:"))


def get_date():
    search_by_date(input("Digite a data no formato aaaa-mm-dd:"))


def get_tag():
    search_by_tag(input("Digite a tag:"))


def get_category():
    search_by_category(input("Digite a categoria:"))


def get_top_5_news():
    top_5_news()


def get_top_5_categories():
    top_5_categories()


def end_script():
    print("Encerrando script")


def option_director(option):
    menu = [
      create_news,
      get_title,
      get_date,
      get_tag,
      get_category,
      get_top_5_news,
      get_top_5_categories,
      end_script
    ]
    try:
        if not 0 <= int(option) <= 7:
            print("Opção inválida", file=sys.stderr)
        else:
            menu[int(option)]()

    except ValueError:
        print("Opção inválida", file=sys.stderr)


text_options = """Selecione uma das opções a seguir:\n
         0 - Popular o banco com notícias;\n
         1 - Buscar notícias por título;\n
         2 - Buscar notícias por data;\n
         3 - Buscar notícias por tag;\n
         4 - Buscar notícias por categoria;\n
         5 - Listar top 5 notícias;\n
         6 - Listar top 5 categorias;\n
         7 - Sair.\n"""


# Requisito 12
def analyzer_menu():
    print(text_options)

    option = input()

    return option_director(option)
