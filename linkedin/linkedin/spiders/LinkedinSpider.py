from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy import log
from linkedin.items import LinkedinItem
from os import path

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

    def parse(self, response):
        """
        default parse method, rule is not useful now
        """
        hxs = HtmlXPathSelector(response)
        index_level = self.determine_level(response)
        if index_level == 1:
            # get second level urls to crawl
            self.save_to_file_system(index_level, response)
            pass
        elif index_level == 2:
            # get third level urls to crawl
            pass
        elif index_level == 3:
            pass
        elif index_level == 4:
            pass
        i = LinkedinItem()
        #i['domain_id'] = hxs.select('//input[@id="sid"]/@value').extract()
        #i['name'] = hxs.select('//div[@id="name"]').extract()
        #i['description'] = hxs.select('//div[@id="description"]').extract()
        return i
    
    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        index_level = self.determine_level(response)
        if index_level == 1:
            # get second level urls to crawl
            self.save_to_file_system(index_level, response)
            # TODO yield new request
            pass
        elif index_level == 2:
            # get third level urls to crawl
            # TODO yield new request
            pass
        elif index_level == 3:
            # TODO yield new request
            pass
        elif index_level == 4:
            pass
        i = LinkedinItem()
        #i['domain_id'] = hxs.select('//input[@id="sid"]/@value').extract()
        #i['name'] = hxs.select('//div[@id="name"]').extract()
        #i['description'] = hxs.select('//div[@id="description"]').extract()
        return i

    
    def determine_level(self, response):
        """
        determine the index level of current response, so we can decide wether to continue crawl or not.
        first level: people/[a-z].html
        second level: people/[A-Z][\d+].html
        third level: people/?.html
        fourth level: profile link or search link
        """
        import re
        url = response.url
        if re.match(".+/[a-z]\.html", url):
            return 1
        elif re.match(".+/[A-Z]\d+.html", url):
            return 2
        elif re.match(".+/people/[a-zA-Z0-9-]+.html", url):
            return 3
        # TODO seperate search page and personal profile page.
        return 4
    
    def save_to_file_system(self, level, response):
        """
        save the response to related folder
        """
        if level in [1,2,3]:
            fileName = self.get_clean_file_name(level, response)
            fn = path.join(self.settings["DOWNLOAD_FILE_FOLDER"],"first_level",fileName)
            self.log("Saving to %s" % fn, level=log.DEBUG)
            with open(fn,"w") as f:
                f.write(response.body)
        elif level == 4:
            # deal with search page or true personal profile page
            pass
    
    def get_clean_file_name(self, level, response):
        if level in [1,2,3]:
            fn = response.url.split("/")[-1]
            return fn
        elif level == 4:
            pass