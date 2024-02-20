from scraper import Scraper
from compiler import Compiler


scraper = Scraper()
compiler = Compiler()

# enter all the listings data from scrapers intro google form
for n in range(len(scraper.addresses)):
    compiler.fill_form(scraper.addresses[n], scraper.prices[n], scraper.links[n])
