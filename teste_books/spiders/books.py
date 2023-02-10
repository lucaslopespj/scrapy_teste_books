import scrapy


class BooksSpider(scrapy.Spider):
    base_url = "https://books.toscrape.com/catalogue/"
    name = "books"
    start_urls = ["http://books.toscrape.com/catalogue/page-1.html"]

    def parse(self, response):
        titulos = response.xpath('//li[@class="col-xs-6 col-sm-4 col-md-3 col-lg-3"]//h3/a/@title').extract()
        prices = response.xpath('//div[@class = "product_price"]/p[@class = "price_color"]/text()').extract()
        
        for i in range(len(titulos)):
            yield {
                'name':titulos[i],
                'price':prices[i]
            }

        url = response.xpath('//li[@class = "next"]/a/@href').extract()

        if url == []:
            return

        url = self.base_url + url[0]

        # print('###################################################')
        # print(url)
        
        yield scrapy.Request(url=url, callback=self.parse)



        