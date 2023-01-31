import scrapy

class DBSpider(scrapy.Spider):
    name = "db" #The name of the spider to be called                   
    start_urls = [
        'https://finance.yahoo.com/quote/DBX/financials',
        'https://finance.yahoo.com/quote/DBX/history',
    ]
    #parse is called to handle the response downloaded for each of the requests made.
    #parse usually parses the response, extracting the scraped data as dicts and finding new URLs to follow to and creating new requests from them
    def parse(self, response):
        page = response.url.split("/")[5]
        filename = f'db-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')