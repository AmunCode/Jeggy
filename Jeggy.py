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

URLs = []
for page in Pages:
    addOn = str(page)
    page_res = requests.get('https://bstocksupply.com/cell-phones?p=' + addOn)
    page_bs = bs4.BeautifulSoup(page_res.text, features='lxml')

    # scrapes the current page for all auctions listed on the page
    for link in page_bs.find_all('a'):
        if link.has_attr('href'):
            if 'auctions' in link.attrs['href']:
                #print(link.attrs['href'])  # tracer line --remove from live code
                URLs.append(link.attrs['href'])
URLs = list(dict.fromkeys(URLs))
