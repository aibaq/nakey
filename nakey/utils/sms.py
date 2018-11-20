from django.conf import settings
import logging
import requests

logger = logging.getLogger(__name__)


def send_sms(number, text):
    '''
    Module for sending sms.
    '''
    try:
        text = text.encode('utf-8')
        params = {
            'login': settings.SMS_LOGIN,
            'password': settings.SMS_PASSWORD,
            'type': 'message',
            'sender': settings.SMS_SENDER,
            'recipient': number,
            'text': text
        }
        response = requests.get(settings.SMS_URL, params=params)
        return response.json()
    except Exception as e:
        logger.error(e)
        return None
