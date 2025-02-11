import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_page_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links

def main():
    url = 'https://awscc4demo2.mcttechnology.cn/'  # 替换为你要抓取的网站URL
    links = get_page_links(url)
    print(f"Total links: {len(links)}")

    # 将链接列表转换为DataFrame
    df = pd.DataFrame(links, columns=['Link'])

    # 将DataFrame导出到CSV文件
    df.to_csv('website_links.csv', index=False)
    print("CSV file created: website_links.csv")

if __name__ == "__main__":
    main()
