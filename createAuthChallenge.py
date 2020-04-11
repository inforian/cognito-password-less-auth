import json
import random
import os

 


def lambda_handler(event, context):
    """Create Challenge and then Send Notification
    """

    print(event, '-------------- start ---------------')
    
    response = event.get('response')
    request = event.get('request')
    session = request.get('session')

    if (not session) or len(session) == 0:
        print(event, '--------create Challenge-------------')
        secretLoginCode = # << create your otp here>>
        
        # send Notification
        contact = request.get('userAttributes').get('email')
        # << call your notify fn here>>
        
    else:
        print(event, '--------Used existing Challenge-------------')
        previousChallenge = session[0]
        secretLoginCode = previousChallenge.get('challengeMetadata')

    response.update({
        'privateChallengeParameters': {'answer': secretLoginCode},
        'challengeMetadata': secretLoginCode,
        'publicChallengeParameters': {
            'answer': secretLoginCode
        }
    })    

    print(event, '--------end-------------')
    
    return event
