from bs4 import BeautifulSoup
import requests
# import csv
import json

# get html
url = "https://www.amazon.com.br/gp/bestsellers/books"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

# get all produtos
books = soup.find_all(id="gridItemRoot")

# create csv title
# csv_headers = ['Rank', 'Title', 'Author', 'Price']
# with open('amazon_books.csv', 'w', encoding='utf-8', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(csv_headers)


arqs = []

for book in books:

    rank = book.find('span', class_='zg-bdg-text').text[1:]
    children = book.find('div', class_='zg-grid-general-faceout').div
    title = children.contents[1].text
    author = children.contents[2].text
    price = children.contents[-1].text[3:]

    # gerar arquivo csv
    # with open('amazon_books.csv', 'a', encoding='utf-8', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow([rank, title, author, price])

    arq = {"Rank": rank, "Title": title, "Author": author, "Price": price, }
    arqs.append(arq)


with open("arq.json", "w") as aj:
    json.dump(arqs, aj, indent=4, ensure_ascii=False, sort_keys=True)
# print(arqs)
