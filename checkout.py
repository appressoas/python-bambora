""" Python 3 Bambora Checkout code example. """

import json
import requests

# Set correct test tokens and merchant number 
ACCESSTOKEN = 'ACCESSTOKENTEST'
MERCHANTNUMBER = 'MERCHANTNUMBERTEST'
SECRETTOKEN = 'SECRETTOKEN'

auth_user = '{}@{}'.format(ACCESSTOKEN, MERCHANTNUMBER)
auth_password = SECRETTOKEN
sessions_url = "https://api.v1.checkout.bambora.com/sessions"

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
    url=sessions_url,
    auth=(auth_user, auth_password),
    data=json.dumps(post_data),
    headers=headers
)

result_data = result.json()
checkout_url = result_data.get('url')

print(checkout_url)
