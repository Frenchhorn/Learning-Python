# Using scrapy shell
https://www.analyticsvidhya.com/blog/2017/07/web-scraping-in-python-using-scrapy/

https://docs.scrapy.org/en/latest/topics/commands.html

## Open the scrapy shell
`scrapy shell`

## Crawl the website
`fetch("https://www.reddit.com/r/gameofthrones/")`

## See the page in browser
`view(response)`

## Whole html
`response.text`

## Get the (the first one) title html (use css selector), return string
`response.css('title').extract_first()`

## Get the title html (all), return list
`response.css('title').extract()`

## Get the title text
`response.css('title::text').extract_first()`

`response.css('title::text')[0].extract()`

## Get the attr
`response.css('span::attr(class)').extract_first()`

## Use re
```python
>>> response.css('title::text').re(r'Quotes.*')
['Quotes to Scrape']
>>> response.css('title::text').re(r'Q\w+')
['Quotes']
>>> response.css('title::text').re(r'(\w+) to (\w+)')
['Quotes', 'Scrape']
```


# Writing custom spiders
## Creating a scrapy project
`scrapy startproject ourfirstscraper [project_dir]`

That will create a Scrapy project under the `project_dir` directory. If `project_dir` wasn't specified,
`project_dir` will be the same as `myproject`

## Creating a spider
`scrapy genspider redditbot www.reddit.com/r/gameofthrones/`

## Start a spider 
`scrapy crawl redditbot`

## Exporting scraped data as csv (settings.py)
`FEED_FORMAT = "csv"`

`FEED_URI = "reddit.csv"`

or `scrapy crawl redditbot -o test.json`
