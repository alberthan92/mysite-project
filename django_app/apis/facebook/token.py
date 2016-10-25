from django.conf import settings
import requests
import json

__all__ = [
    'get_access_token',
    'debug_token',
    'get_user_info',
]

APP_ID = settings.FACEBOOK_APP_ID
SECRET_CODE = settings.FACEBOOK_SECRET_CODE
APP_ACCESS_TOKEN = '{app_id}|{secret_code}'.format(
                app_id=APP_ID,
                secret_code=SECRET_CODE,
            )

def get_access_token(code, redirect_uri):
    print('code : %s' % code)
    REDIRECT_URI = redirect_uri


    url_request_access_token = 'https://graph.facebook.com/v2.8/oauth/access_token?' \
                               'client_id={app_id}&' \
                               'redirect_uri={redirect_uri}&' \
                               'client_secret={secret_code}&' \
                               'code={code}'.format(
                                   app_id=APP_ID,
                                   redirect_uri=REDIRECT_URI,
                                   secret_code=SECRET_CODE,
                                   code=code,
                               )
    r = requests.get(url_request_access_token)
    dict_access_token = r.json()
    print(json.dumps(dict_access_token, indent=2))
    ACCESS_TOKEN = dict_access_token['access_token']
    print('access token : %s' % ACCESS_TOKEN)
    return ACCESS_TOKEN


def debug_token(access_token):
    ACCESS_TOKEN = access_token

    url_debug_user_id = 'https://graph.facebook.com/debug_token?' \
                          'input_token={it}&' \
                          'access_token={at}'.format(
                            it=ACCESS_TOKEN,
                            at=APP_ACCESS_TOKEN
                        )

    r = requests.get(url_debug_user_id)
    dict_debug = r.json()
    print(json.dumps(dict_debug, indent=2))
    USER_ID = dict_debug['data']['user_id']
    print('user id : %s' % USER_ID)
    return USER_ID


def get_user_info(user_id, access_token):
    ACCESS_TOKEN = access_token
    USER_ID = user_id
    url_request_user_info = 'https://graph.facebook.com/{user_id}?' \
                            'fields=id,email,first_name,last_name&' \
                            'access_token={access_token}'.format(
        user_id=USER_ID,
        access_token=ACCESS_TOKEN
    )

    r = requests.get(url_request_user_info)
    dict_user_info = r.json()
    print(json.dumps(dict_user_info, indent=2))
    return dict_user_info
