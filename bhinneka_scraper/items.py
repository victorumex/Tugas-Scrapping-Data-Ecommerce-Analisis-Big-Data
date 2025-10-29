import scrapy
from itemloaders.processors import TakeFirst, MapCompose

# menghilangkan 'Rp', '.', dan spasi
def clean_price(value):
    if value:
        return value.replace('Rp', '').replace('.', '').strip()
    return value

class BhinnekaScraperItem(scrapy.Item):
    name = scrapy.Field(
        output_processor=TakeFirst() 
    )
    price = scrapy.Field(
        input_processor=MapCompose(clean_price),
        output_processor=TakeFirst() 
    )
    link = scrapy.Field(
        output_processor=TakeFirst() 
    )