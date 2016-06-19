# Code adapted from: https://github.com/scrapy-plugins/scrapy-splash
# Code adapted from: https://blog.scrapinghub.com/2015/03/02/handling-javascript-in-scrapy-with-splash/

"""Steps:
1. Start up docker with terminal command: docker run -p 8050:8050 scrapinghub/splash
2. Test scrapy splash is working via visiting webite localhost:8050
2. Start up another terminal command and set PATH to anaconda2
3. Activate scrapy virtual env
4. CD to botcheck folder
5. Ensure file with URLs to crawl is in the root folder of botcheck
6. Run crawljs spider with command scrapy crawl crawljs > <output file name.csv>"""

# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy_splash import SplashRequest

searchjs = "<string to search for>"


class botcheckSpider(CrawlSpider):
	name = "crawljs"
    	allowed_domains = ["<domain to stay within>"]
	start_urls = []
		
	with open('<file with list of URLs to crawl>') as f:
		for sites in f:
			if (sites.startswith("http://") or sites.startswith("https://")):
				start_urls.append(sites)

	def start_requests(self):
		for url in self.start_urls:
			yield SplashRequest(url, self.parse_item, args={'wait': 1.0})
			
	def parse_item(self, response):
		content = response.body
		if searchtag in content:
			print (response.url)
