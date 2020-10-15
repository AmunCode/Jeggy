import bs4
import requests

bs_supply_site = requests.get('https://bstocksupply.com/cell-phones?')
bs = bs4.BeautifulSoup(bs_supply_site.text, features='lxml')

print(bs.title)

pages=[]
for link in bs.find_all('a'):
    if link.has_attr('href'):
        if 'p=' in link.attrs['href']:
            #print(link.string)
            pages.append(link.string)
Pages = list(dict.fromkeys(pages)) #remove duplicates from pages that will be scrapped

for page in pages:
    addOn = str(page)
    print('https://bstocksupply.com/cell-phones?p='+addOn)