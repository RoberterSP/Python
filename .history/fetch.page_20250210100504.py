import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

def get_all_links(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]
        return links
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return []

def export_to_excel(links, filename):
    wb = Workbook()
    ws = wb.active
    ws.title = "Website Links"
    for index, link in enumerate(links, start=1):
        ws.cell(row=index, column=1, value=link)
    wb.save(filename)

# 示例用法
url = 'https://awscc4demo2.mcttechnology.cn/'  # 替换为你要抓取的网站 URL
links = get_all_links(url)
export_to_excel(links, 'website_links.xlsx')
print(f"Total links: {len(links)}")
