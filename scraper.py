from bs4 import BeautifulSoup
import requests


# class for scraping data about listings on Zillow
class Scraper:
    def __init__(self):
        self.url = "https://appbrewery.github.io/Zillow-Clone/"
        self.response = requests.get(self.url)
        website_html = self.response.text
        self.soup = BeautifulSoup(website_html, "html.parser")

        self.links = [link.get("href") for link in self.soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")]
        self.prices = [price.text.split('/')[0].replace('+', '').split()[0] for price in self.soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")]
        self.addresses = [' '.join(address.string.split()).replace("|", "") for address in self.soup.find_all(name="address")]
        # print(self.links)
        # print(self.prices)
        # print(self.addresses)
