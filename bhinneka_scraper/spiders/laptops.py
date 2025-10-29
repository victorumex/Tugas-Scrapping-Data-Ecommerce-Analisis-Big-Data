# bhinneka_scraper/spiders/laptops.py

import scrapy
from scrapy.loader import ItemLoader 
# Pastikan nama class Item di items.py adalah BhinnekaScraperItem
from bhinneka_scraper.items import BhinnekaScraperItem 

class LaptopsSpider(scrapy.Spider):
    name = "laptops"
    allowed_domains = ["bhinneka.com"]
    # Ini URL yang Anda berikan
    start_urls = ["https://www.bhinneka.com/category-technology-communication"]

    def parse(self, response):
        
        # 1. Gunakan selector KONTAMINER PRODUK yang baru dan benar
        # Kita akan mengambil setiap tag <a> dengan class 'product-wrapper'
        # Ini ada di dalam carousel, tapi kita bisa ambil semua produknya sekaligus
        
        products = response.css('a.product-wrapper')
        
        # Ini akan mencatat ke log berapa banyak produk yang ditemukan
        self.logger.info(f"Berhasil! Menemukan {len(products)} produk di halaman {response.url}")

        for product in products:
            # 'selector=product' sekarang merujuk ke tag <a class="product-wrapper">
            loader = ItemLoader(item=BhinnekaScraperItem(), selector=product)

            # 2. Ambil NAMA dari div.product-title di DALAM kontainer
            loader.add_css('name', 'div.product-title::text')
            
            # 3. Ambil HARGA dari span.oe_currency_value di DALAM kontainer
            loader.add_css('price', 'div.price span.oe_currency_value::text')
            
            # 4. Ambil LINK dari atribut 'href' kontainer itu sendiri (karena kontainernya <a>)
            loader.add_css('link', '::attr(href)') 
            
            yield loader.load_item()