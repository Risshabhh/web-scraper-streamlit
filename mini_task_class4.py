# scraper.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

visited = set() 

def is_valid(url, base_netloc):
    try:
        parsed = urlparse(url)
        return (parsed.netloc == base_netloc or parsed.netloc == '') and parsed.scheme in ['http', 'https']
    except:
        return False

def scrape_website(base_url, depth=2):
    visited.clear()
    report_data = []
    base_netloc = urlparse(base_url).netloc

    def crawl(url, current_depth):
        if current_depth > depth or url in visited:
            return
        visited.add(url)
        try:
            resp = requests.get(url, timeout=5)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, 'html.parser')
                text = soup.get_text(separator='\n', strip=True)
                report_data.append(f"\n--- PAGE: {url} ---\n{text}\n")
                # Find sublinks
                for a in soup.find_all('a', href=True):
                    new_url = urljoin(url, a['href'])
                    if is_valid(new_url, base_netloc):
                        crawl(new_url, current_depth + 1)
        except Exception as e:
            print(f"Error scraping {url}: {e}")

    crawl(base_url, 0)
    return "\n".join(report_data)
