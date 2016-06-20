# JSCheck
Crawling for JavaScript rendered HTML in websites

####Description:

Beautiful Soup doesn't work to get the full HTML contents  of a website. This is probably because that particular HTML content is not hard coded in the source code, but loads only after JavaScript renders. Beautiful Soup is not beautiful enough for JavaScript rendered HTML.

You could use Selenium. But the Scrapy-Splash package is lighter-weight vs Selenium for larger datasets.

This code will scan URLs listed in a separate file for a pre-defined string in HTML. Once it comes across a site containing the string, it will print out the URL. This code is useful to quickly search for presence of a javascript-rendered tag or iframe within many websites.  

####System requirements:

Because Docker is required, a Linux-based system or Mac works best. Windows would require going through a VM.

####Packages used:

Scrapy, Scrapy-Splash. Scrapy only runs in Python 2.

####Additional notes:

The wiki page should contain additional help notes for setting up scrapy & scrapy splash
