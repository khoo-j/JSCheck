# JSCheck
Crawling for JavaScript rendered HTML in websites

####Description:

You are here because Beautiful Soup doesn't work to get the full HTML contents  of a website. This is probably because that particular HTML content is not hard coded in the source code, but loads only after JavaScript renders. Beautiful Soup is not beautiful enough for JavaScript rendered HTML.

You could use Selenium. But I have found the Scrapy-Splash package to be lighter-weight vs Selenium.

####System requirements:

Because Docker is required, a Linux-based system or Mac works best. Windows would require going through a VM.

####Packages used:

Scrapy, Scrapy-Splash. Scrapy only runs in Python 2.

####Additional notes:

The wiki page should contain additional help notes for setting up scrapy & scrapy splash
