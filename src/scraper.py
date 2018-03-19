import scrapy
from scrapy.http import Request
import gi

gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.init("last_unread_msgs_spider")

class MyWebSpider(scrapy.Spider):
    name = "last_unread_msgs_spider"
    start_urls = ['http://instrumentyklawiszowe.com/index.php?action=login']

    def parse(self, response):
        self.log("##################################### start")

        return scrapy.FormRequest.from_response(
            response,
            callback=self.after_login,
            formdata={'user': 'self.login_param', 'passwrd': 'self.password_param'}
        )

    def after_login(self, response):
        if 'Hasło niewłaściwe' in response.body.decode():
            self.log("Login failed!")
            return
        else:
            self.log("Login successful")
            return Request(url="http://instrumentyklawiszowe.com/",
               callback=self.parse_main_page)

    def parse_main_page(self, response):
        if 'REGULAMIN FORUM' in response.body.decode():
            self.log("++++ done!")

            Message = Notify.Notification.new(
                "IK_Spider",
                "Hi, I'm logged!",
                "dialog-information"
            )

            Message.show()

        else:
            self.log("#### not done!")



        # SET_SELECTOR = '.set'
        # for brickset in response.css(SET_SELECTOR):
        #
        #     NAME_SELECTOR = 'h1 a ::text'
        #     yield {
        #         'name': brickset.css(NAME_SELECTOR).extract_first(),
        #     }
