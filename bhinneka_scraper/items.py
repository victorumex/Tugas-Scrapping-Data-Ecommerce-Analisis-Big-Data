# bhinneka_scraper/items.py

import scrapy
from itemloaders.processors import TakeFirst, MapCompose

# Fungsi untuk membersihkan harga (menghilangkan 'Rp', '.', dan spasi)
def clean_price(value):
    if value:
        return value.replace('Rp', '').replace('.', '').strip()
    return value

class BhinnekaScraperItem(scrapy.Item):
    name = scrapy.Field(
        output_processor=TakeFirst() 
    )
    price = scrapy.Field(
        input_processor=MapCompose(clean_price), # Terapkan pembersihan harga
        output_processor=TakeFirst() 
    )
    link = scrapy.Field(
        output_processor=TakeFirst() 
    )