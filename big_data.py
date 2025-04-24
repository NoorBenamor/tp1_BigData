import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

articles = []


max_pages = 1000

search_query = "artificial intelligence"


scraped_pages = []

session = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def fetch_url(url, retries=3, delay=5):
    for attempt in range(retries):
        try:
            response = session.get(url, headers=headers, timeout=10)
            response.raise_for_status()  
            return response.text
        except requests.exceptions.RequestException as e:
            print(f" Error on attempt {attempt + 1} for {url}: {e}")
            time.sleep(delay + random.uniform(1, 3))  
    print(f"Failed to load {url} after {retries} attempts")
    return None


for page in range(1, max_pages + 1):
    url = f"https://pubmed.ncbi.nlm.nih.gov/?term={search_query.replace(' ', '+')}&page={page}"
    
    html_content = fetch_url(url)
    if not html_content:
        break  

    soup = BeautifulSoup(html_content, 'html.parser')

    scraped_pages.append(url)
    print(f"{page}. {url}")

    items = soup.find_all('article', class_='full-docsum')

    if not items:
        print(f"No more articles found on page {page}. Stopping.")
        break

    for item in items:
        try:
            title = item.find('a', class_='docsum-title').text.strip()
            link = "https://pubmed.ncbi.nlm.nih.gov" + item.find('a', class_='docsum-title')['href']
            authors = item.find('span', class_='docsum-authors full-authors').text.strip() if item.find('span', class_='docsum-authors full-authors') else "Unknown"
            journal = item.find('span', class_='docsum-journal-citation full-journal-citation').text.strip() if item.find('span', class_='docsum-journal-citation full-journal-citation') else "Unknown"
            date = item.find('span', class_='docsum-pubdate').text.strip() if item.find('span', class_='docsum-pubdate') else "Unknown"
            article_type = item.find('span', class_='publication-type').text.strip() if item.find('span', class_='publication-type') else "Unknown"

            articles.append({
                "Title": title,
                "Authors": authors,
                "Journal": journal,
                "Publication Date": date,
                "Article Type": article_type,
                "Link": link,
            })
        except Exception as e:
            print(f" Error extracting data: {e}")
            continue

   
    time.sleep(random.uniform(2, 5))


df = pd.DataFrame(articles)
df.to_csv("pubmed_articles.csv", index=False, encoding='utf-8-sig')

print("\n All data has been saved in pubmed_articles.csv")
