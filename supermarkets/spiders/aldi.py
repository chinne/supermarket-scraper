# -*- coding:utf-8 -*-
import scrapy


class AldiSpider(scrapy.Spider):
    name = "aldi"
    allowed_domains = ["www.aldi-nord.de"]
    start_urls = ["https://www.aldi-nord.de/angebote.html"]

    def parse(self, response):
        """a method that will be called to handle the response downloaded for each of the requests made. The response parameter is an instance
        of TextResponse that holds the page content and has further helpful methods to handle it.
        The parse() method usually parses the response, extracting the scraped data as dicts and also finding new URLs to follow and creating new requests (Request) from them."""
        # page = response.url.split("/")[-2]
        # articles = response.xpath('//*[@class="mod-article-tile__content"]')
        print("responsen", response.text)
        article = response.xpath(
            '//*[@class="mod-article-tile__title"]/text()'
        ).extract()
        price = response.xpath('//*[@class="price__main"]/text()').extract()
        description_short = response.xpath(
            '//*[@class="mod-article-tile__info"]/p/text()'
        ).extract()
        # print(articles)
        price_list = price[0::2]
        product_list = article[1::2]
        for i, _ in enumerate(price_list):
            # print(articl)
            # print(price)
            product = (
                article.xpath('//*[@class="mod-article-tile__title"]/text()').extract(),
            )
            price = article.xpath('//*[@class="price__main"]/text()').extract()
            print(product_list[i].strip())
            yield {
                "Produkt": product_list[i].strip(),
                "Beschreibung": description_short[i].strip(),
                "Preis": price_list[i].strip(),
            }
