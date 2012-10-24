from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
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
        if index_level in [1, 2, 3]:
            # get second level urls to crawl
            self.save_to_file_system(index_level, response)
            relative_urls = self.get_follow_links(index_level, hxs)
            if relative_urls is not None:
                for url in relative_urls:
                    yield Request(url, callback=self.parse)
            pass
        elif index_level == 4:
            pass
    
    def determine_level(self, response):
        """
        determine the index level of current response, so we can decide wether to continue crawl or not.
        level 1: people/[a-z].html
        level 2: people/[A-Z][\d+].html
        level 3: people/[a-zA-Z0-9-]+.html
        level 4: profile link or search link
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
        if level in [1, 2, 3]:
            fileName = self.get_clean_file_name(level, response)
            fn = path.join(self.settings["DOWNLOAD_FILE_FOLDER"], str(level), fileName)
            self.log("Saving to %s" % fn, level=log.DEBUG)
            with open(fn, "w") as f:
                f.write(response.body)
        elif level == 4:
            # deal with search page or true personal profile page
            pass
    
    def get_clean_file_name(self, level, response):
        if level in [1, 2, 3]:
            fn = response.url.split("/")[-1]
            return fn
        elif level == 4:
            pass
        
    def get_follow_links(self, level, hxs):
        if level in [1,2,3]:
            relative_urls = hxs.select("//ul[@class='directory']/li/a/@href").extract()
            relative_urls = ["http://linkedin.com" + x for x in relative_urls]
            return relative_urls
        elif level == 4:
            return []
