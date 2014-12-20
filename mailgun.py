__author__ = 'cemkiy'


import requests

class mailgun:
    def __init__(self):
        self.key = 'key-2361ddc59bfd7a45df0acdac47b84390'
        self.sandbox = 'sandboxe1e55da3f7a7423ba6d16a58c3ffbee8.mailgun.org'
        self.recipient = 'info@fazladanbilet.com'

    def send_mail(self, email_to, text):
        request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(self.sandbox)
        request = requests.post(request_url, auth=('api', self.key), data={
            'from': self.recipient,
            'to': email_to,
            'subject': 'fazladanbilet.com',
            'text': text
        })
        output = 'Status: {0}'.format(request.status_code) + 'Body:   {0}'.format(request.text)
        print output

    def send_mail_with_html(self, email_to, html):
        request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(self.sandbox)
        request = requests.post(request_url, auth=('api', self.key), data={
            'from': self.recipient,
            'to': email_to,
            'subject': 'fazladanbilet.com',
            'html': html
        })
        output = 'Status: {0}'.format(request.status_code) + 'Body:   {0}'.format(request.text)
        print output

# template = get_template("mail_activation.html")
# context = Context({'username': 'cem'})
# content = template.render(context)
# mailgun_operator = mailgun()
# mailgun_operator.send_mail_with_html(member_user_auth.email, content)