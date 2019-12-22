import scrapy

class CarolSpider(scrapy.Spider):
    name = "carols"
    start_urls = [ "https://www.koledypolskie.pl/spis-koled-pelna-lista" ]

    def parse(self, response):
        names = response.css("div.su-post h2.su-post-title a::text").getall();
        links = response.css("div.su-post h2.su-post-title a::attr(href)").getall();
        for i in range(len(links)):
            link = links[i]
            if link is not None:
                link = response.urljoin(link);
                request = scrapy.Request(link, callback=self.parseText);
                request.cb_kwargs['name'] = names[i];
                yield request

    def getTextFromResponse(self, response):
        parts = response.css("div.su-row ::text").getall()
        if not parts:
            selectors = response.css("div")
            for selector in selectors:
                if selector.css("::attr(id)").get() == 'element_id_to_print':
                    parts = selector.css("::text").getall()
                    print("PARTS:", parts)
        return parts

    def parseText(self, response, name):
        parts = self.getTextFromResponse(response)
        text = "";
        if not parts:
            print("\n\nERROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n", name, "\n\n",)
        for part in parts:
            text += part;
        yield dict(name = name, text = text)