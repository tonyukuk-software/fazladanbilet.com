__author__ = 'cemkiy'

import requests

key = 'key-2361ddc59bfd7a45df0acdac47b84390'
sandbox = 'sandboxe1e55da3f7a7423ba6d16a58c3ffbee8.mailgun.org'
recipient = 'se.cemkiy@gmail.com'

request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
request = requests.post(request_url, auth=('api', key), data={
    'from': 'hello@example.com',
    'to': recipient,
    'subject': 'Hello',
    'text': 'Hello from Mailgun'
})

print 'Status: {0}'.format(request.status_code)
print 'Body:   {0}'.format(request.text)
