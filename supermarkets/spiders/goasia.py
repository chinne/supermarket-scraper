import scrapy


class GoasiaSpider(scrapy.Spider):
    name = "goasia"
    allowed_domain = ["https://goasia.net/onlineshop"]
    start_urls = ["https://goasia.net/onlineshop/?p=1"]

    # def start_requests(self)
    #     yield scrapy.Request(f'https://goasia.net/onlineshop/?p={self.page}')

    def parse(self, response):
        for page in range(1, 120):
            for products in response.css("div.product--info"):
                if products.css("span.buy-btn--cart-text::text").get():
                    available = "yes"
                else:
                    available = "sold out"
                yield {
                    "name": products.css("a.product--title").attrib["title"],
                    "price": products.css("span.price--default.is--nowrap::text")
                    .get()
                    .split()[0],
                    "available": available,
                    "link": products.css("a.product--title").attrib["href"],
                }

            next_page_url = f"https://goasia.net/onlineshop/?p={str(page)}"
            if next_page_url:
                request = scrapy.Request(url=next_page_url)
                yield request
