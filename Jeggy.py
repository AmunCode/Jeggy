import bs4
import requests
import auctions
import searches
import xlwt
from xlwt import Workbook

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

B_Supply_Auctions = []

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

    B_Supply_Auctions.append(auctions.auction(ID, model[1:], gigs, grade, count, price, listing))
    print(B_Supply_Auctions[-1].specs())

selection = searches.search_for_b_grade(B_Supply_Auctions)

#tracer lines below to verify BSupply aution list is populated
#for item in B_Supply_Auctions:
#    if 'XR' in item.model:
#       print(item.specs())

#tracer lines below to verify Bsupply
#for item in selection:
#    if 'XR' in item.model:
#        print(item.specs())

def write_excel(b_supply_auctions):
    workbook = Workbook()
    sheet = workbook.add_sheet("BStock Supply Auctions")
    row = 0
    col = 0

    sheet.write(row, col, 'ID')
    col = col + 1
    sheet.write(row, col, 'Model')
    col = col + 1
    sheet.write(row, col, 'Gig')
    col = col + 1
    sheet.write(row, col, 'Grade')
    col = col + 1
    sheet.write(row, col, 'Count')
    col = col + 1
    sheet.write(row, col, 'Price')
    col = col + 1
    sheet.write(row, col, "Auction URL")
    row = row + 1
    col = 0

    for auction in b_supply_auctions:
        sheet.write(row, col, auction.ID)
        col = col + 1
        sheet.write(row, col, auction.model)
        col = col + 1
        sheet.write(row, col, auction.gig)
        col = col + 1
        sheet.write(row, col, auction.grade)
        col = col + 1
        sheet.write(row, col, auction.count)
        col = col + 1
        sheet.write(row, col, auction.price)
        col = col + 1
        sheet.write(row, col, auction.link)
        col = col + 1
        row = row + 1
        col = 0

    workbook.save('auctions.xls')


write_excel(B_Supply_Auctions)

select_login_data = {
    'client_id': '1b094c5f-c8a6-416c-8c62-4dc77ca88ce9',
    'code_challenge': '',
    'code_challenge_method': '',
    'metaData.device.name': 'Windows Chrome',
    'metaData.device.type': 'BROWSER',
    'nonce': '',
    'redirect_uri': 'https://selectmobile.bstock.com/sso/index/login/',
    'response_mode': '',
    'response_type': 'code',
    'scope': 'offline_access',
    'state': 'isRedirect',
    'tenantId': '17e51778-a4db-4dd3-b31e-1f990f373099',
    'timezone': 'America/New_York',
    'user_code': '',
    'showPasswordField': 'true',
    'loginId': '',              #change this to appropriate user
    'password': ''              #chane this to appropriate user
}
superior_login_data = {
    'client_id': '1b094c5f-c8a6-416c-8c62-4dc77ca88ce9',
    'code_challenge': '',
    'code_challenge_method': '',
    'metaData.device.name': 'Windows Chrome',
    'metaData.device.type': 'BROWSER',
    'nonce': '',
    'redirect_uri': 'https://superior.bstock.com/sso/index/login/',
    'response_mode': '',
    'response_type': 'code',
    'scope': 'offline_access',
    'state': 'isRedirect',
    'tenantId': '17e51778-a4db-4dd3-b31e-1f990f373099',
    'timezone': 'America/New_York',
    'user_code': '',
    'showPasswordField': 'true',
    'loginId': '',              #change this to appropriate user
    'password': ''              #chane this to appropriate user
}

