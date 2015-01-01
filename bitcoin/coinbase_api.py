__author__ = 'cemkiy'
import coinbase
from coinbase import *



#API Key: FsziO6obdo5YJaZc

#API Secret: BSNlZmyjEY9HB704WODeZDaS5NVSs3oL

class coinbase_api:
    def __init__(self):
        self.account = coinbase.CoinbaseAccount(oauth2_credentials=None, api_key='FsziO6obdo5YJaZc', api_secret='BSNlZmyjEY9HB704WODeZDaS5NVSs3oL',
                 allow_transfers=True)


    def get_transactions(self):
        try:
            return self.account.transactions()
        except Exception as e:
            print e
            return False

    def get_transaction_by_id(self, trans_id):
        try:
            return self.account.get_transaction(trans_id)
        except Exception as e:
            print e
            return False

    def send_bitcoin(self, to_adress, amount, note):
        try:
            btc_amount = CoinbaseAmount(amount, 'BTC'),
            self.account.send(to_adress, btc_amount, note)
        except Exception as e:
            print e
            return False

    def get_orders(self):
        try:
            return self.account.orders()
        except Exception as e:
            print e
            return False

    def get_order_by_id(self, order_id):
        try:
            return self.account.get_order(order_id)
        except Exception as e:
            print e
            return False

    def create_button(self, amount, order_id):
        expected_button = CoinbasePaymentButton(
            id=str(order_id),
            name=str(order_id),
            price=CoinbaseAmount(amount, 'BTC'),
            custom=str(order_id),
            auto_redirect=True,
            description='',
            include_address=False,
            include_email=False,
            style='buy_now_large',
            text='Pay With Bitcoin',
            type='buy_now',
            variable_price=False,
            success_url='http://www.fazladanbilet.com/bitcoin/success_url/' + str(order_id),
            cancel_url='http://www.fazladanbilet.com/bitcoin/cancel',
        )
        button = self.account.create_button(expected_button)
        return button

        #api = coinbase_api()
        #button = api.create_button('id', 'name', 'custom')
        #print button[0]


