import json
import boto3
import hmac
import uuid
import hashlib
import base64
import os


USER_PASS_AUTH_FLOW = 'USER_PASSWORD_AUTH'
CUSTOM_AUTH_FLOW = 'CUSTOM_AUTH'
REFRESH_TOKEN = 'REFRESH_TOKEN'


def sign_me_in(contact, password):
    """SignIn
    
    """    
    try:
        response = cognito_client.initiate_auth(
                        ClientId='client_id',
                        AuthFlow='CUSTOM_AUTH',
                        AuthParameters= params = {
                            'USERNAME': contact,
                            'PASSWORD': password
                        }
                    )
    except cognito_client.exceptions.NotAuthorizedException:
        return None, "The username or password is incorrect"
    except Exception as e:
        print(e, '------------------ signin error  ---------------------')
        return None, "Unknown error"
    return response, None    

def lambda_handler(event, context):
    """SignIn Users
    
    """
    password = event.get('password', 'qwertyu')  # for custom auth random password will be used.
    contact = event.get('contact', 'qwert')

    response, error = sign_me_in(contact, password)
    
    if error:
        return {'statusCode': 400, 'detail': error}
       
    return {'statusCode': 200, 'detail': response}
