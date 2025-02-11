import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

# 目标网站
base_url = "https://awscc4demo.mcttechnology.cn/"
visited_urls = set()
all_urls = []

def get_all_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            full_url = urljoin(base_url, link['href'])
            if full_url not in visited_urls and base_url in full_url:
                visited_urls.add(full_url)
                all_urls.append(full_url)
                print(f"Found: {full_url}")
                get_all_links(full_url)  # 递归爬取
    except Exception as e:
        print(f"Error fetching {url}: {e}")

# 开始爬取
get_all_links(base_url)

# 将结果保存为表格
df = pd.DataFrame(all_urls, columns=["URL"])
df.to_csv("website_pages.csv", index=False)
print("网站页面已保存到 website_pages.csv")