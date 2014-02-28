from mock import patch

from django.test import TestCase

from ..utils import send_sms


class SendSMSTest(TestCase):
    def test_send_sms(self):
        text = 'Test text',
        recipient = '447123456789'
        sender = '447987654321'
        user = 'Test'
        password = 'Myv3rystr0ngp4sswurd'

        url = 'https://www.txtlocal.com/sendsmspost.php'
        payload = {
            'selectednums': recipient,
            'message': text,
            'uname': user,
            'pword': password,
            'from': sender,
            'json': 1,
        }

        with patch('requests.post') as post:
            post.return_value.json.return_value = {
                'CreditsAvailable': 25,
                'CreditsRequired': 3,
                'CreditsRemaining': 22,
            }

            send_sms(
                text=text, recipient_list=[recipient], sender=sender,
                username=user, password=password,
            )

            post.assert_called_once_with(url, data=payload)
