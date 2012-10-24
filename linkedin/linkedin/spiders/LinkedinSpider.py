from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from linkedin.items import LinkedinItem

class LinkedinspiderSpider(CrawlSpider):
    name = 'LinkedinSpider'
    allowed_domains = ['linkedin.com']
    start_urls = [
                  "http://www.linkedin.com/directory/people/a.html",
                  "http://www.linkedin.com/directory/people/b.html",
                  "http://www.linkedin.com/directory/people/c.html",
                  "http://www.linkedin.com/directory/people/d.html",
                  "http://www.linkedin.com/directory/people/e.html",
                  "http://www.linkedin.com/directory/people/f.html",
                  "http://www.linkedin.com/directory/people/g.html",
                  "http://www.linkedin.com/directory/people/h.html",
                  "http://www.linkedin.com/directory/people/i.html",
                  "http://www.linkedin.com/directory/people/j.html",
                  "http://www.linkedin.com/directory/people/k.html",
                  "http://www.linkedin.com/directory/people/l.html",
                  "http://www.linkedin.com/directory/people/m.html",
                  "http://www.linkedin.com/directory/people/n.html",
                  "http://www.linkedin.com/directory/people/o.html",
                  "http://www.linkedin.com/directory/people/p.html",
                  "http://www.linkedin.com/directory/people/q.html",
                  "http://www.linkedin.com/directory/people/r.html",
                  "http://www.linkedin.com/directory/people/s.html",
                  "http://www.linkedin.com/directory/people/t.html",
                  "http://www.linkedin.com/directory/people/u.html",
                  "http://www.linkedin.com/directory/people/v.html",
                  "http://www.linkedin.com/directory/people/w.html",
                  "http://www.linkedin.com/directory/people/x.html",
                  "http://www.linkedin.com/directory/people/y.html",
                  "http://www.linkedin.com/directory/people/z.html"
                  ]

    rules = (
        #Rule(SgmlLinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        i = LinkedinItem()
        #i['domain_id'] = hxs.select('//input[@id="sid"]/@value').extract()
        #i['name'] = hxs.select('//div[@id="name"]').extract()
        #i['description'] = hxs.select('//div[@id="description"]').extract()
        return i
