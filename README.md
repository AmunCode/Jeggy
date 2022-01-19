# Jeggy
Auctions scraper to pull and analyze BSstock auction inventory manifests for purchashing opportunities

- Automates a time consuming task from hours down to minutes
- OOP example: turns each item of each auction into an object. 
- Multi-threading to speed up scraping process. 

## Prerequisites
`request`
`bs4`
`concurrent.futures`
`pandas`
`datetime`
`time`

## To run
Download all files into one folder andhave python 3.7 installed. Update username and password in the scrapes.py file. 

run:
`python main.py`

## Demo Images
Very simple interface with dropdown menu selection. 
![Opening Menu](https://user-images.githubusercontent.com/55643060/150057725-dc15fa99-da7a-4481-8a09-0cd3e919df7f.png)

Output to excel based on filter preferences.
![Filtered Excel Output Menu](https://user-images.githubusercontent.com/55643060/150058491-51645fe3-c36a-4ad5-8df7-8ba699af7a2e.png)
