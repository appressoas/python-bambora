""" Python 3 Bambora Checkout code example. """

import json
import requests

# Test tokens and merchant number 
ACCESSTOKEN = 'TOKEN'
MERCHANTNUMBER = 'MERCHANT'
SECRETTOKEN = 'SECRET'

auth_user = '{}@{}'.format(ACCESSTOKEN, MERCHANTNUMBER)
auth_password = SECRETTOKEN
checkout_url = 'https://api.v1.checkout.bambora.com/sessions'

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

post_data = {
    'language': 'no-NB',
    'customer': {
        'phonenumbercountrycode': '47',
        'phonenumber': '93492558',
        'email': 'magne@appresso'
    },
    'order': {
        'id': 'TestDonation123',
        'amount': '1000',
        'currency': 'NOK',
    },
    'url': {
        'accept': 'https://example.org/accept',
        'cancel': 'https://example.org/cancel',
        'callbacks': {
            'url': 'https://example.org/callback',
        }
    }
}

result = requests.post(
    url=checkout_url,
    auth=(auth_user, auth_password),
    data=json.dumps(post_data),
    headers=headers
)
print(result.json())
