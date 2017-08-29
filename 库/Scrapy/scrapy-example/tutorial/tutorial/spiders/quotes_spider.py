import scrapy


class QuotesSpider(scrapy.Spider):
    # 启动一个爬虫，在与scrapy.cfg同目录下 `scrapy crawl quotes_1`
    name = 'quotes_1'     # 标识符，定义一个项目中唯一的爬虫名字

    def start_requests(self):
        '''
        必须返回可迭代对象，可以是list或者生成器
        '''
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        '''
        获得response后的默认处理方法
        通常会返回一个字典或者创建一个新的请求
        '''
        page = response.url.split('/')[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


class Quotes2Spider(scrapy.Spider):
    name = 'quotes_2'
    # start_urls 是start_requests的快捷方式，会自动创建Request对象，使用回调parse方法
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)


class Quotes3Spider(scrapy.Spider):
    name = 'quotes_3'
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            '''
            提取数据，可以使用`scrapy crawl quotes_3 -o test.json` 输出到文件
            文件格式可以是json, jl (即JSON Lines), csv
            '''
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

            '''
            获取下一页的url
            如果存在url，返回一个新的请求
            '''
            next_page = response.css('li.next a::attr(href)').extract_first()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)


class Quotes4Spider(scrapy.Spider):
    name = 'quotes_4'
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

            next_page = response.css('li.next a::attr(href)').extract_first()
            if next_page is not None:
                # 创建新请求的快捷方式，支持相对路径URL
                # Scrapy 1.4版本以后才有这个方法
                yield response.follow(next_page, callback=self.parse)
            # 也可以选择传一个选择器
            '''
            for href in response.css('li.next a'):
                yield response.follow(a, callback=self.parse)
            '''


class AuthorSpider(scrapy.Spider):
    '''
    Scrapy 默认会自动去重，可以在 DUPEFILTER_CLASS 处设置
    '''
    name = 'author'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # 作者详情链接
        author_pages =  response.css('.author + a::attr(href)').extract()
        for author_page in author_pages:
            if author_page is not None:
                href = response.urljoin(author_page)
                yield scrapy.Request(href, callback=self.parse_author)

        # 下一页
        next_page =  response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            href = response.urljoin(next_page)
            yield scrapy.Request(href, callback=self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            # 去除两边的空格
            return response.css(query).extract_first().strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }


class Quotes5Spider(scrapy.Spider):
    '''
    使用参数设置爬虫
    scrapy crawl quotes_5 -o humor.json -a tag=humor
    '''
    name = 'quotes_5'

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)        # 或者直接使用self.tag
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            href = response.urljoin(next_page)
            yield scrapy.Request(href, callback=self.parse)
