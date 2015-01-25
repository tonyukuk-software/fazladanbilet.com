__author__ = 'cemkiy'
import coinbase
from coinbase import *



class coinbase_api:
    def __init__(self):
        self.account = coinbase.CoinbaseAccount(oauth2_credentials=None, api_key='CWyFGgC8H0Gu9xrw', api_secret='msJ384h3BYw6tjbnEYWMiCddy5qyiNlI',
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

    def send_bitcoin(self, adress, amount, note):
        try:
            self.account.send(to_address=adress, amount=CoinbaseAmount(amount, 'BTC'), notes=note)
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


