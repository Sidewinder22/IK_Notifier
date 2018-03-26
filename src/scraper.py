import scrapy
from scrapy.http import Request
import gi

gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.init("last_unread_msgs_spider")

class MyWebSpider(scrapy.Spider):
    name = "last_unread_msgs_spider"
    start_urls = ['http://instrumentyklawiszowe.com/index.php']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            callback=self.after_login,
            formdata={'user': self.login_param, 'passwrd': self.password_param}
        )

    def after_login(self, response):
        if 'Hasło niewłaściwe' in response.body.decode():
            self.log("Login failed!")
            return

        if 'Nazwa użytkownika nie istnieje.' in response.body.decode():
            self.log("User doesn't exist!")
            return

        self.log("Login successful")
        return Request(url="http://instrumentyklawiszowe.com/index.php?action=unread",
           callback=self.process_page)


    def process_page(self, response):
        self.log("process_page")
        SET_SELECTOR = '.windowbg2'
        NAME_SELECTOR = 'span a ::text'

        for thing in response.css(SET_SELECTOR):

            label =  thing.css(NAME_SELECTOR).extract_first(),
            result = ''
            print (label)
            if label[0]:
                print(label[0])
                result += label[0]
                result += ', '

            Message = Notify.Notification.new(
                "Forum IK.com - nowe wątki",
                # "kom",
                result,
                "dialog-information"
            )

            Message.show()
