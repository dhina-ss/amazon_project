from bs4 import BeautifulSoup
import requests
import pandas as pd
import json

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
data = []

df = pd.read_csv('Amazon Scraping.csv')
j = 1
for i in df.values:
    print(j)
    amazon_url = f'https://www.amazon.{i[3]}/dp/{i[2]}'
    page = requests.get(amazon_url,headers = headers).text
    soup = BeautifulSoup(page, 'lxml')
    if soup.find(id = 'productTitle'):
        if soup.find(id = 'landingImage'):
            title = soup.find(id = 'productTitle').text.strip()
            print('\nProduct Title : ',title)
            img = soup.find(id = 'landingImage')
            img = img['src']
            print('Product Image URL : ',img)
            price = soup.find(class_ = 'a-offscreen').text
            print('Price of the Product : ',price)
            details = soup.find_all(id = 'productDescription')
            for i in details:
                detail = i.text
                print('Product Details : ',detail,'\n')
            dict = {'Title':title, 'Image':img, 'Price':price, 'Details':detail}
            data.append(dict)
        else:
            pass
    else:
        print(amazon_url,' Not Available')
    j += 1

jsonString = json.dumps(data)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()