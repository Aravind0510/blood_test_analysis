import requests
from bs4 import BeautifulSoup

def search_articles(analysis_result):
    query = f"health tips for {analysis_result['Cholesterol']} cholesterol and {analysis_result['Glucose']} glucose"
    search_url = f"https://www.google.com/search?q={query}"

    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    for link in soup.find_all('a', href=True):
        if "url?q=" in link['href']:
            article_url = link['href'].split("url?q=")[1].split("&sa=")[0]
            articles.append(article_url)

    return articles[:5]  # Return top 5 articles
