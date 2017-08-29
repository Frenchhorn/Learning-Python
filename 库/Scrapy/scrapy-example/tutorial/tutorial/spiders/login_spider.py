import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login'

    def start_request(self):
        return [scrapy.FormRequest('http://www.example.com/login',
                                    formdata={'user': 'john', 'pass': 'secret'},
                                    callback=self.logged_in)]

    def logged_in(self, response):
        # here you would extract links to follow and return Requests for
        # each of tem, with another callback
        pass
