__author__ = 'barisariburnu'

import requests
from django.conf import settings

class Mailgun():

    def __init__(self):
        self._access_key = "key-78dd2b5cd01dd08c1d5400419f1a834c"
        self._server_name = "sandbox3cab865ec1944738b20b22069a08f010.mailgun.org"
        self._api_url = "https://api.mailgun.net/v2/%s/" % self._server_name

    def send_message(self, mTo, mSubject, mText, mHtml):
        return requests.post(
            "https://api.mailgun.net/v2/sandbox3cab865ec1944738b20b22069a08f010.mailgun.org",
            auth=("api", "key-78dd2b5cd01dd08c1d5400419f1a834c"),
            data={"from": "Excited User <me@sandbox3cab865ec1944738b20b22069a08f010.mailgun.org>",
                  "to": mTo,
                  "subject": mSubject,
                  "text": mText,
                  "html": mHtml})

    def get_unsubscribes(self):
        return requests.get(
            self._api_url + "/unsubscribes",
            auth=("api", self._access_key))

    def unsubscribe (self, mMail):
        return  requests . post (
            self._api_url + "/unsubscribes" ,
            auth = ( "api" ,  self._access_key ),
            data = { 'address' : mMail })

yeni = Mailgun()
yeni.send_message("barisariburnu@gmail.com","Konu","Icerik","<html>HTML version of the body</html>")