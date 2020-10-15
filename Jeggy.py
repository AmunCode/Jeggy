import bs4
import requests
import auctions

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

Auctions = []

for page in URLs:
    # print(page)
    # print(URLs[i])
    auctionPage = requests.get(page)
    # print(page)

    soup1 = bs4.BeautifulSoup(auctionPage.text, 'lxml')
    # print(soup1)

    titleArr = soup1.title.string.split(',')
    model = titleArr[0]
    # print(model[1:])

    gigs = titleArr[1]
    # print(gigs[1:])

    # grade = soup1.title.string.split(',')[6]
    # print(grade[1:])
    for part in titleArr:
        if 'Grade' in part:
            grade = part
        elif 'Salvage' in part:
            grade = 'Salvage'
        elif 'New Condition' in part:
            grade = 'New'
        if 'Unit' in part:
            count = part

    price = soup1.find(id='unit_per_price_span').string[1:7]
    price = price.strip('/')

    ID = page.split('/')[-2]

    listing = page

    Auctions.append(auctions.auction(ID, model[1:], gigs, grade, count, price, listing))

for i in Auctions:
    print(i.specs())