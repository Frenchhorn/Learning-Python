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


class Login2Spider(scrapy.Spider):
    '''
    It is usual for web sites to provide pre-populated form fields through <input type="hidden"> elements,
    such as session related data or authentication tokens (for login pages).
    '''
    name = 'example.com'
    start_urls = ['http://www.example.com/users/login.php']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'john', 'password': 'secret'},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.logger.error("Login failed")
            return

        # continue scraping with authenticated session...
