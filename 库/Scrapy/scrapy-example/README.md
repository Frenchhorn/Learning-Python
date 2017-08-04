# using scrapy shell
https://www.analyticsvidhya.com/blog/2017/07/web-scraping-in-python-using-scrapy/

## open the scrapy shell
`scrapy shell`

## crawl the website
`fetch("https://www.reddit.com/r/gameofthrones/")`

## see the page in browser
`view(response)`

## whole html
`response.text`

## get the (the first one) title html (use css selector), return string
`response.css('title').extract_first()`

## get the title html (all), return list
`response.css('title').extract()`

## get the title text
`response.css('title::text').extract_first()`

## get the attr
`response.css('span::attr(class)').extract_first()`


# writing custom spiders

## creating a scrapy project
`scrapy startproject ourfirstscraper`

## creating a spider
`scrapy genspider redditbot www.reddit.com/r/gameofthrones/`

## start a spider 
`scrapy crawl redditbot`

## exporting scraped data as csv (settings.py)
`FEED_FORMAT = "csv"`

`FEED_URI = "reddit.csv"`


# download images

## enable images pipeline
`ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}`

`IMAGES_STORE = 'tmp/images/'`

## set the url to the field image_urls
`scraped_info['image_urls'] = ['https://static.runoob.com/images/icon/go.png']`