import datetime
from unicodedata import decimal

__author__ = 'cemkiy'

class bag_skeleton:
    def __init__(self):
        self.cokkie_text = ''
        self.ticket_id = ''
        self.total_number = '1'
        self.amount_bitcoin = '0.0'
        self.title = ''
        self.ticket_photo = ''
        self.date = datetime.datetime.now()

    def create_bag_item(self, ticket_id, total_number, amount_bitcoin, title, ticket_photo):
        self.cokkie_text = str(ticket_id)+'/'+str(total_number)+'/'+str(amount_bitcoin)+'/'+str(title)+'/'+str(ticket_photo)+'/'+str(self.date)+'/?'
        return self.cokkie_text

    def solved_bag_item(self, cookie_text):
        self.cokkie_text = cookie_text
        data_item_list = []
        data_item = ''

        for letter in self.cokkie_text:
            if letter is '/':
                data_item_list.append(data_item)
                data_item = ''
            elif letter == '[' or letter == ']' or letter == '?':
                pass
            else:
                data_item = data_item + letter

        try:
            self.ticket_id = data_item_list[0]
            self.total_number = data_item_list[1]
            self.amount_bitcoin = data_item_list[2]
            self.title = data_item_list[3]
            self.ticket_photo = data_item_list[4]
            self.date = data_item_list[5]
        except Exception as e:
            print e



# example = bag_skeleton()
# example.solved_bag_item('4/0/0.003/deneme/ticket_photos/Smoking-Pipe-l_bgYm60j.jpg/2014-12-14 13:03:49.318983/')

