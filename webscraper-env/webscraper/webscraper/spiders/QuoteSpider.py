import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes" #The name of the spider to be called                   
    start_urls = [
        'https://quotes.toscrape.com/page/1/',
        'https://quotes.toscrape.com/page/2/',
    ]
    #parse is called to handle the response downloaded for each of the requests made.
    #parse usually parses the response, extracting the scraped data as dicts and finding new URLs to follow to and creating new requests from them
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')