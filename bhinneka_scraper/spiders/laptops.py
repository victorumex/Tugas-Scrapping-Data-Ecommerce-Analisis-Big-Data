import scrapy
from scrapy.loader import ItemLoader 
from bhinneka_scraper.items import BhinnekaScraperItem 

class LaptopsSpider(scrapy.Spider):
    name = "laptops"
    allowed_domains = ["bhinneka.com"]
    start_urls = ["https://www.bhinneka.com/category-technology-communication"]

    def parse(self, response):        
        products = response.css('a.product-wrapper')
        self.logger.info(f"Berhasil! Menemukan {len(products)} produk di halaman {response.url}")

        for product in products:
            # 'selector=product' sekarang merujuk ke tag <a class="product-wrapper">
            loader = ItemLoader(item=BhinnekaScraperItem(), selector=product)
            
            # Ambil nama dari div.product-title di DALAM kontainer
            loader.add_css('name', 'div.product-title::text')
            
            # Ambil harga dari span.oe_currency_value di DALAM kontainer
            loader.add_css('price', 'div.price span.oe_currency_value::text')

            # Ambil link dari atribut 'href' kontainer itu sendiri (karena kontainernya <a>)
            loader.add_css('link', '::attr(href)') 
            
            yield loader.load_item()