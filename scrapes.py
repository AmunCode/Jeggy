import requests
import bs4
import concurrent.futures
import auctions
import pandas
import datetime as dt
import time

start_time = time.time()

BSTOCK_USER_NAME = 'gregory@1804group.com'
BSTOCK_PW = 'bstock#1031'
AUTH_URL = 'https://auth.bstock.com/oauth2/authorize'
SELECT_COLUMNS = ['ID', 'Make', 'Model', 'Grade', 'Count', 'Price', 'Description', 'Network', 'Capacity', 'Auction URL']
select_auction_items = []
select_login_data = {
    'client_id': '1b094c5f-c8a6-416c-8c62-4dc77ca88ce9',
    'code_challenge': '',
    'code_challenge_method': '',
    'metaData.device.name': 'Windows Chrome',
    'metaData.device.type': 'BROWSER',
    'nonce': '',
    'redirect_uri': 'https://bstock.com/selectmobile/sso/index/login/',
    'response_mode': '',
    'response_type': 'code',
    'scope': 'offline_access',
    'state': 'isRedirect',
    'tenantId': '17e51778-a4db-4dd3-b31e-1f990f373099',
    'timezone': 'America/New_York',
    'user_code': '',
    'showPasswordField': 'true',
    'loginId': BSTOCK_USER_NAME,                 #change this to appropriate user
    'password': BSTOCK_PW                        #change this to appropriate user
}

superior_login_data = select_login_data
superior_login_data['redirect_uri'] = 'https://bstock.com/superior/sso/index/login/'


def write_scrape_data(auction_objects_list, auction_selected):
    auction_specs_list = []
    for item in auction_objects_list:
        auction_specs_list.append(item.specs().split(','))
    data_frame = pandas.DataFrame(auction_specs_list, columns=SELECT_COLUMNS)
    now = dt.datetime.now()

    writer = pandas.ExcelWriter(f'{now.month}{now.day}{now.year}-{now.hour}h{now.minute}m Auction Data.xls')
    data_frame.to_excel(writer, sheet_name=f"{auction_selected} Auctions", index=False)
    writer.save()


def scrape(auction_selected: str):
    with requests.session() as current_session:
        global select_auction_items
        # check the auction_selected and log into the appropriate auctions.
        if 'superior' in auction_selected:
            current_session.post(AUTH_URL, data=superior_login_data)
            auction_page_prefix = 'https://bstock.com/superior/auction/auction/list/?limit=96&p='
            superior_auction_items = []
            print('superior login')
        elif 'select' in auction_selected:
            auction_page_prefix = 'https://selectmobile.bstock.com/?limit=96&p='
            current_session.post(AUTH_URL, select_login_data)
            select_auction_items = []
            print('select login')
        else:
            print("Target auction not support")

        # Pull the main landing page and convert it over to a bs object (easier to parse)
        auction_landing_page = current_session.get('https://selectmobile.bstock.com/?limit=96')
        auction_landing_page_bs = bs4.BeautifulSoup(auction_landing_page.text, 'lxml')

        # list to hold the pages with all the auction tiles
        auction_pages_list = []

        for link in auction_landing_page_bs.find_all('a'):
            if link.has_attr('href'):
                if 'p=' in link.attrs['href']:
                    # add given link to list of all auctions
                    auction_pages_list.append(link.string)
                    print(link.string)

        # remove duplicate elements from auction_pages_list
        auction_pages_list = set(auction_pages_list)

        # initialized a list to hold the individual auction URLs
        auction_urls = []

        for page in auction_pages_list:
            suffix = str(page)
            auction_page = current_session.get(auction_page_prefix + suffix)
            # print(auction_page_prefix + suffix)
            auction_page_bs = bs4.BeautifulSoup(auction_page.text, 'lxml')
            # scrape current page ofr individual auction URL that are tiled on the page
            for link in auction_page_bs.find_all('a'):
                if link.has_attr('href'):
                    if 'auction' and 'view' in link.attrs['href']:
                        auction_urls.append(link.attrs['href'])

        # remove duplicate elements from auction_urls
        auction_urls = list(dict.fromkeys(auction_urls))

        ######################################################################################
        ########################## Multi-thread ##############################################

        # for page in auction_urls:
        def download_manifest(t_page):
            # print(f"Thread {threading.get_ident()} entering manifest download function with {t_page}.")
            temp = []
            manifest_is_downloaded = False
            while not manifest_is_downloaded:
                auction_lot_page = current_session.get(t_page)
                auction_lot_page_bs = bs4.BeautifulSoup(auction_lot_page.text, 'lxml')
                manifest_url_candidate = str(auction_lot_page_bs.find_all('div', attrs={"class": "auction-manifest"}))
                manifest_url_candidate.split()

                # locate the url of the manifest for the auction
                manifest_url = ''
                characters_to_remove = "',;"
                for part in manifest_url_candidate.split():
                    if 'csv' in part:
                        manifest_url = part
                        for character in characters_to_remove:
                            manifest_url = manifest_url.replace(character, "")

                manifest = current_session.get(manifest_url)
                manifest_bs = bs4.BeautifulSoup(manifest.content, 'lxml')
                downloaded_manifest = manifest_bs.text

                # Parse the downloaded manifest for individual item data
                start_index = 0
                num_of_items = 0
                manifest_parts = downloaded_manifest.split(',')  # items listed on manifest
                if 'superior' in auction_selected:
                    num_of_items = int((len(manifest_parts)-10)/10)
                    start_index = 10
                elif 'select' in auction_selected:
                    num_of_items = int((len(manifest_parts) - 8) / 7)
                    start_index = 7

                auction_id = t_page.split('/')[-2]
                price = float(auction_lot_page_bs.find(id='unit_per_price_span').string[1:])
                link = t_page
                loop_counter = 1

                while loop_counter <= num_of_items:
                    temp_index = (start_index * loop_counter)
                    temp.append(auctions.SelectAuction(temp_index, manifest_parts, auction_id, price, link))
                    loop_counter = loop_counter + 1
                if len(temp) > 0:
                    manifest_is_downloaded = True
            return temp

        with concurrent.futures.ThreadPoolExecutor() as executor:
            auction_lists = executor.map(download_manifest, auction_urls)

        for listing in auction_lists:
            try:
                for item in listing:
                    select_auction_items.append(item)
            except TypeError:
                pass

        write_scrape_data(select_auction_items, auction_selected)

        print("--- %s seconds ---" % (time.time() - start_time))

        # for page in auction_urls:
        #     # print(page)
        #     auction_lot_page = current_session.get(page)
        #     auction_lot_page_bs = bs4.BeautifulSoup(auction_lot_page.text, 'lxml')
        #     manifest_url_candidate = str(auction_lot_page_bs.find_all('div', attrs={"class": "auction-manifest"}))
        #     manifest_url_candidate.split()
        #
        #     characters_to_remove = "',;"
        #     manifest_url = ''
        #     for part in manifest_url_candidate.split():
        #         if 'csv' in part:
        #             manifest_url = part
        #             for character in characters_to_remove:
        #                 manifest_url = manifest_url.replace(character, "")
        #
        #     print(manifest_url)
        #
        #     manifest = current_session.get(manifest_url)
        #     manifest_bs = bs4.BeautifulSoup(manifest.content, 'lxml')
        #     downloaded_manifest = manifest_bs.text
        #
        #     manifest_parts = downloaded_manifest.split(',')  # items listed on manifest
        #     if 'superior' in auction_selected:
        #         num_of_items = int((len(manifest_parts)-10)/10)
        #         start_index = 10
        #     elif 'select' in auction_selected:
        #         num_of_items = int((len(manifest_parts) - 8) / 7)
        #         start_index = 7
        #
        #     auction_id = page.split('/')[-2]
        #     price = float(auction_lot_page_bs.find(id='unit_per_price_span').string[1:])
        #     link = page
        #
        #     loop_counter = 1
        #     while loop_counter <= num_of_items:
        #         temp_index = (start_index * loop_counter)
        #         select_auction_items.append(auctions.SelectAuction(temp_index, manifest_parts, auction_id, price, link))
        #         loop_counter = loop_counter + 1
        #
        # for page in select_auction_items:
        #     print(page.specs())
        #
        # print("--- %s seconds ---" % (time.time() - start_time))
        # write_scrape_data(select_auction_items, auction_selected)


#scrape("select auctions")

